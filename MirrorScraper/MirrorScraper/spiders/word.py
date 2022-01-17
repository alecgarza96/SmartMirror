import scrapy


class WordSpider(scrapy.Spider):
    name = 'word'
    allowed_domains = ['www.merriam-webster.com/word-of-the-day']
    start_urls = ['http://www.merriam-webster.com/word-of-the-day/']

    def parse(self, response):
    	word = response.xpath('//div[@class="word-and-pronunciation"]/h1/text()').get()
    	definition = response.xpath("//div[@class='wod-definition-container']/p/text()").getall()
    	yield { "word": word,
    	        "definition": definition }
