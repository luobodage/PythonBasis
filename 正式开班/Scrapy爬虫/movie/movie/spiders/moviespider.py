import re

import scrapy

from movie.items import MovieItem
import lxml.etree as le

class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['ygdy8.net']
    start_urls = []

    for i in range(1, 10):
        start_urls.append(f'https://www.ygdy8.net/html/gndy/china/list_4_{i}.html')

    def parse(self, response, **kwargs):

        # title = response.xpath('//*[@class="ulink"][2]/text()').extract()
        href = response.xpath('//*[@class="ulink"][2]/@href').extract()

        for i in href:
            url = 'https://www.ygdy8.net' + i
            print(url)
            yield scrapy.Request(url, callback=self.parse1)

    def parse1(self, response):
        item = MovieItem()
        # print(response.text)
        html = response.body
        lxml = le.HTML(html)
        # print(html)
        # re_img = re.search(r"\bhttps://(.*?)jpg", html)
        # img_url = re_img.group()
        #
        # title = re.search(r"\b<br />◎(.*?)。<br />", html)
        # movie_title = title.group()
        movie_title = lxml.xpath('//*[@id="Zoom"]/span/p[1]/text()')
        # movie_time = str(response.xpath('//*[@id="Zoom"]/span/p/text()[3]').extract_first())
        # movie_origin = str(response.xpath('//*[@id="Zoom"]/span/p[1]/text()[4]').extract_first())[6:]
        # movie_category = str(response.xpath('//*[@id="Zoom"]/span/p[1]/text()[5]').extract_first())[6:]
        # movie_language = str(response.xpath('//*[@id="Zoom"]/span/p[1]/text()[6]').extract_first())[6:]
        # movie_subtitles = str(response.xpath('//*[@id="Zoom"]/span/p[1]/text()[7]').extract_first())[6:]
        # movie_releaseDate = str(response.xpath('//*[@id="Zoom"]/span/p[1]/text()[8]').extract_first())[6:]
        # movie_length = str(response.xpath('//*[@id="Zoom"]/span/p[1]/text()[9]').extract_first())[6:]
        # movie_starring = str(response.xpath('//*[@id="Zoom"]/span/p[1]/text()[10]').extract_first())[6:]
        # movie_label = str(response.xpath('//*[@id="Zoom"]/span/p[1]/text()[15]').extract_first())[6:]
        # movie_introduction = str(response.xpath('//*[@id="Zoom"]/span//p[1]text()[16]').extract_first())[6:]
        # item['img_url'] = img_url
        item['movie_title'] = movie_title
        # item['movie_time'] = movie_time
        # item['movie_origin'] = movie_origin
        # item['movie_category'] = movie_category
        # item['movie_language'] = movie_language
        # item['movie_subtitles'] = movie_subtitles
        # item['movie_releaseDate'] = movie_releaseDate
        # item['movie_length'] = movie_length
        # item['movie_starring'] = movie_starring
        # item['movie_label'] = movie_label
        # item['movie_introduction'] = movie_introduction
        print(item)
        yield item
