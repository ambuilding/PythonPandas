## Find interesting users on Medium

- API endpoint

	```
	https://medium.com/_/api/users/<userId>
	User: userId / name/ username / twitterScreenName / facebookAccountId
	https://medium.com/_/api/users/<userId>/profile
	userMeta: interestTags / authorTags
	https://medium.com/_/api/users/<userId>/following
	payload / value /

	JSON response
	Except for a string of characters at the beginning of the response
	])}while(1);</x>

	5a2e47aa48be
	```

- get all the users from the following list

	```
	find the URL for JSON feed by ?format=json / get userId
	Pull the userId from a given username
	Query the endpoint / userId

	# pagination
	?limit=8&to=<next_id>

	get the latest posts from each user
	https://medium.com/@<username>/latest?format=json
	payload /references / Post

	get all the responses from each post
	https://medium.com/_/api/posts/<post_id>/responses

- Filter the responses

	response = / payload / value /
	response / createdAt
	response / virtuals / recommends
	response / creatorId


- get the username(author) of each response

	https://medium.com/_/api/posts/90180824ee3c/responses
	https://medium.com/_/api/posts/81f48b52875c/responses?filter=best

