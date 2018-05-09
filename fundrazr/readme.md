### Use scrapy to build dataset

- scrapy startproject fundrazr

- Finding good start URLs using Inspect on Google Chrome

	start_urls
	https://fundrazr.com/find?category=Health
	Next page
	https://fundrazr.com/find?category=Health&page=2

- Scrapy Shell for finding Individual Campaign Links

	use XPath to extract the Individual Campaign Link
	view(response)
	response.xpath(
		"//h2[contains(@class, 'title headline-font')]/a[contains(@class, 'campaign-link')]//@href"
	).extract()

- Inspecting Individual Campaigns

	scrapy shell 'https://fundrazr.com/savemyarm'
	title
	response.xpath("//div[contains(@id, 'campaign-title')]/descendant::text()").extract()[0]
	amount-raised
	response.xpath("//span[contains(@class,'stat')]/span[contains(@class, 'amount-raised')]/descendant::text()").extract()
	goal
	response.xpath("//div[contains(@class, 'stats-primary with-goal')]//span[contains(@class, 'stats-label hidden-phone')]/text()").extract()
	currency type
	response.xpath("//div[contains(@class, 'stats-primary with-goal')]/@title").extract()
	campaign end date:
	response.xpath("//div[contains(@id, 'campaign-stats')]//span[contains(@class,'stats-label hidden-phone')]/span[@class='nowrap']/text()").extract()
	number of contributors
	response.xpath("//div[contains(@class, 'stats-secondary with-goal')]//span[contains(@class, 'donation-count stat')]/text()").extract()
	story
	response.xpath("//div[contains(@id, 'full-story')]/descendant::text()").extract()
	url
	response.xpath("//meta[@property='og:url']/@content").extract()

- Items / The main goal in scraping is to extract structured data from unstructured sources, typically, web pages. Scrapy spiders can return the extracted data as Python dicts.

	$ scrapy crawl fundrazr.com -o MonthDay_Year.csv

### How to crawl the web politely with scrapy
- Do not harm the website

#### A polite crawler
- Respect robots.txt
- Never degrade a website’s performance
- Identifie its creator with contact information
- DOWNLOAD_DELAY / AUTOTHROTTLE_ENABLED / HTTPCACHE_ENABLED
- Don’t Crawl, use the API
