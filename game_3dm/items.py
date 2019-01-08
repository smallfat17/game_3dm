# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Game3DmItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Cname = scrapy.Field()
    Ename = scrapy.Field()
    developer = scrapy.Field()
    publisher = scrapy.Field()
    pub_date = scrapy.Field()
    game_type = scrapy.Field()
    station = scrapy.Field()
    lang = scrapy.Field()
    label = scrapy.Field()
    pass
