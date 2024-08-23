# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy

class HunterItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    links = scrapy.Field()
    plain_body = scrapy.Field()
    # chunks = scrapy.Field()
    pass