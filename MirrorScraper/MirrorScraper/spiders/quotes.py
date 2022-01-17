import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['https://www.brainyquote.com/quote_of_the_day']
    start_urls = ['https://www.brainyquote.com/quote_of_the_day/']

    def parse(self, response):
    	xpath = '/html/body/main/div[1]/div[2]/div/div/div/a[1]/div/text()'
    	yield { 'quote_of_the_day': response.xpath('/html/body/main/div[1]/div[2]/div/div/div/a[1]/div/text()').get()}

