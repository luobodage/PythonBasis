# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img_url = scrapy.Field()
    movie_title = scrapy.Field()
    movie_time = scrapy.Field()
    movie_origin = scrapy.Field()
    movie_category = scrapy.Field()
    movie_language = scrapy.Field()
    movie_subtitles = scrapy.Field()
    movie_releaseDate = scrapy.Field()
    movie_length = scrapy.Field()
    movie_starring = scrapy.Field()
    movie_label = scrapy.Field()
    movie_introduction = scrapy.Field()
