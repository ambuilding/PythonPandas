import csv
import json
import click
import requests
from time import sleep
from datetime import datetime, timedelta

proxies = {
    'http': "socks5://127.0.0.1:1080",
    'https': "socks5://127.0.0.1:1080",
}

# the base URL
MEDIUM = 'https://medium.com'

# clean ])}while(1);</x> up and turn the JSON into a Python dictionary.
def clean_json_response(response):
    return json.loads(response.text.replace('])}while(1);</x>', '', 1))

# Pull the user ID from a given username
# Then query the /_/api/users/<user_id>/following endpoint
# get the list of usernames from the following list
def get_user_id(username):

    print('Retrieving user ID...')

    url = MEDIUM + '/@' + username + '?format=json'
    response = requests.get(url, proxies=proxies)
    response_dict = clean_json_response(response)

    return response_dict['payload']['user']['userId']

# pagination / limit / to
# a loop
def get_list_of_followings(user_id):

    print('Retrieving users from Followings...')

    next_id = False
    followings = []

    while True:

        if next_id:
            # If this is not the first page of the followings list
            url = MEDIUM + '/_/api/users/' + user_id + '/following?limit=8&to=' + next_id
        else:
            # If this is the first page of the followings list
            url = MEDIUM + '/_/api/users/' + user_id + '/following'

        response = requests.get(url, proxies=proxies)
        response_dict = clean_json_response(response)
        payload = response_dict['payload']

        for user in payload['value']:
            followings.append(user['username'])

        try:
            # If the "to" key is missing, we've reached the end
            # of the list and an exception is thrown
            next_id = payload['paging']['next']['to']
        except:
            break

    return followings

# take a list of usernames
# return a list of post IDs for the latest posts
def get_list_of_latest_posts_ids(usernames):

    print('Retrieving the latest posts...')

    post_ids = []

    for username in usernames:
        url = MEDIUM + '/@' + username + '/latest?format=json'
        response = requests.get(url, proxies=proxies)
        response_dict = clean_json_response(response)

        try:
            posts = response_dict['payload']['references']['Post']
        except:
            posts = []

        if posts:
            for key in posts.keys():
                post_ids.append(posts[key]['id'])

    return post_ids

# takes a list of post IDs and returns a list of post responses
def get_post_responses(posts):

    print('Retrieving the post responses...')
    responses = []

    for post in posts:
        url = MEDIUM + '/_/api/posts/' + post + '/responses'
        response = requests.get(url, proxies=proxies)
        response_dict = clean_json_response(response)
        responses += response_dict['payload']['value']
        sleep(0.5) # This is the most intensive operation for the Medium servers

    return responses

# Filtering the responses
# Checks if a response was created in the last 30 days
def check_if_recent(response):
    limit_date = datetime.now() - timedelta(days=30)
    creation_epoch_time = response['createdAt'] / 1000
    creation_date = datetime.fromtimestamp(creation_epoch_time)

    if creation_date >= limit_date:
        return True

# Checks if a response is over a certain number of recommends
def check_if_high_recommends(response, recommend_min):
    if response['virtuals']['recommends'] >= recommend_min:
        return True


# get the username of the author of each response
def get_user_ids_from_responses(responses, recommend_min):
    print('Retrieving user IDs from the responses...')

    user_ids = []

    for response in responses:
        recent = check_if_recent(response)
        high = check_if_high_recommends(response, recommend_min)

        if recent and high:
            user_ids.append(response['creatorId'])

    return user_ids

def get_usernames(user_ids):
    print('Retrieving usernames of interesting users...')

    usernames = []

    for user_id in user_ids:
        url = MEDIUM + '/_/api/users/' + user_id
        response = requests.get(url, proxies=proxies)
        response_dict = clean_json_response(response)
        payload = response_dict['payload']
        usernames.append(payload['value']['username'])

    return usernames

# Add list of interesting users to the interesting_users.csv and add a timestamp
def list_to_csv(interesting_users_list):
    with open('interesting_users.csv', 'a') as file:
        writer = csv.writer(file)

        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        interesting_users_list.insert(0, now)

        writer.writerow(interesting_users_list)

# put them all together
def get_interesting_users(username, recommend_min):
    print('Looking for interesting users for %s...' % username)

    user_id = get_user_id(username)
    usernames = get_list_of_followings(user_id)
    posts = get_list_of_latest_posts_ids(usernames)
    responses = get_post_responses(posts)
    users = get_user_ids_from_responses(responses, recommend_min)

    return get_usernames(users)

@click.command()
@click.option('-n', '--name', default='explorewo', help='Medium username')
@click.option('-r', '--min-recommendations', default=10, help='Minimum number of recommendations per response')

def main(name, min_recommendations):
    interesting_users = get_interesting_users(name, min_recommendations)
    print(interesting_users)
    list_to_csv(interesting_users)

if __name__ == '__main__':
    main()
