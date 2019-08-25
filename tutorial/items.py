# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
    pass
class NewsTitle(scrapy.Item):
    link = scrapy.Field()
    name = scrapy.Field()
    data_id= scrapy.Field()
class News(scrapy.Item):
    link = scrapy.Field()
    name = scrapy.Field()
class tiki(scrapy.Item):
    pic=scrapy.Field()
    title=scrapy.Field()
    did=scrapy.Field()
    link=scrapy.Field()
class QuoteItem(scrapy.Item):
    author=scrapy.Field()
    quote=scrapy.Field()