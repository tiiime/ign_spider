# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IgnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cover = scrapy.Field()
    title = scrapy.Field()
    platform = scrapy.Field()
    type = scrapy.Field()
    details = scrapy.Field()
    date = scrapy.Field()
    score = scrapy.Field()
    scorePhrase = scrapy.Field()
