# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MoviePipeline:
    def process_item(self, item, spider):
        with open('datamovie.csv', 'a+') as f:
            f.write(item['img_url'] + ',' + item['movie_title'] + ',' + item['movie_time'] + ',' + item[
                'movie_origin'] + ',' + item['movie_category'] + ',' + item['movie_language'] + ',' + item[
                        'movie_subtitles'] + ',' + item['movie_releaseDate'] + ',' + item['movie_length'] + ',' + item[
                        'movie_starring'] + ',' + item['movie_label'] + ',' + item['movie_introduction'] + '\n')
            return item
