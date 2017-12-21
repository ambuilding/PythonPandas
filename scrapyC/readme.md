### Spider

- name, start requests, parse,

- Run spider

	scrapy crawl quotes

- A shortcut to the start_requests method

- Extracting data

	```
	scrapy shell 'http://quotes.toscrape.com/page/1/'

	# Selecting elements using CSS with the response object
	response.css('title')
	response.css('title::text').extract()
	response.css('title').extract()

	response.css('title::text').extract_first()
	response.css('title::text')[0].extract()
	# using .extract_first() avoids an IndexError
	# returns None when it doesn’t find any element matching the selection.

	# re() to extract using regular expressions
	response.css('title::text').re(r'Quotes.*')

	view(response)

	# using XPath expressions - more power
	# learn XPath, it will make scraping much easier
	response.xpath('//title')
	response.xpath('//title/text()').extract_first()
	```

- Extracting quotes and authors

	```
	scrapy shell 'http://quotes.toscrape.com'
	response.css("div.quote")
	quote = response.css("div.quote")[0]
	title = quote.css("span.text::text").extract_first()
	title

	# Iterate over all the quotes elements
	# Put them together into a Python dictionary
	for quote in response.css("div.quote"):
		text = quote.css("span.text::text").extract_first()
		author = quote.css("small.author::text").extract_first()
		tags = quote.css("div.tags a.tag::text").extract()
		print(dict(text=text, author=author, tags=tags))
	```

- Extracting data in our spider
- A Scrapy spider typically generates many dictionaries containing the data extracted from the page.

- Storing the scraped data

	scrapy crawl quotes -o quotes.json
	scrapy crawl quotes -o quotes.jl

- Following links

	response.css('li.next a').extract_first()
	response.css('li.next a::attr(href)').extract_first()

- A shortcut for creating Requests

	```
	Unlike scrapy.Request, response.follow supports relative URLs directly - no need to call urljoin.
	Note that response.follow just returns a Request instance;
	you still have to yield this Request.

	pass a selector to response.follow instead of a string
	this selector should extract necessary attributes

	For <a> elements there is a shortcut:
	response.follow uses their href attribute automatically
	```

- By default, Scrapy filters out duplicated requests to URLs already visited, avoiding the problem of hitting servers too much because of a programming mistake. This can be configured by the setting DUPEFILTER_CLASS.

- Using spider arguments

	```
	# make the spider fetch only quotes with a specific tag
	# building the URL based on the argument
	scrapy crawl quotes -o quotes-humor.json -a tag=humor
	```

### There's a lesson:
- For most scraping code, you want it to be resilient to errors due to things not being found on a page,
- so that even if some parts fail to be scraped, you can at least get some data.

