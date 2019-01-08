# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class Game3DmPipeline(object):

    def __init__(self):
        self.db = MongoClient('192.168.254.131').game_3dm
        self.db.authenticate('gameUser','123456')
        self.collection = self.db.game

    def process_item(self, item, spider):
        self.game.insert(dict(item))
        return item
