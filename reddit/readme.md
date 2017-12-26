### Reddit

- scrapy shell

```
fetch("https://www.reddit.com/r/gameofthrones/")
view(response)
print response.text

# create a spider
scrapy genspider redditbot www.reddit.com/r/gameofthrones/

scrapy crawl redditbot
```

- Exporting the data FEED_FORMAT / FEED_URI

	settings.py


### Scraping an E-Commerce site

	scrapy genspider shopclues www.shopclues.com/mobiles-featured-store-4g-smartphone.html
	fetch("http://www.shopclues.com/mobiles-featured-store-4g-smartphone.html")
	scrapy shell 'http://www.shopclues.com/mobiles-featured-store-4g-smartphone.html'

