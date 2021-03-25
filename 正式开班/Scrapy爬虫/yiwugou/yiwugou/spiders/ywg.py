import scrapy


class YwgSpider(scrapy.Spider):
    name = 'ywg'
    allowed_domains = ['http://www.yiwugo.com/']
    start_urls = ['http://www.yiwugo.com/']

    def parse(self, response):
        print(response.text)
