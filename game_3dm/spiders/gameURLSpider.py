import scrapy
import pandas as pd
import redis



class gameURLSpider(scrapy.Spider):
    name = 'game_3dm_url'
    allowed_domains = ['www.3dmgame.com']
    # redis_key = 'game_url'
    dates = pd.date_range("2010-01", periods=(12 * 8), freq='M')
    years = dates.year.astype('str')
    months = pd.Series(dates.month).apply(lambda x: '0' + str(x) if len(str(x)) == 1 else str(x))
    dates = years + months
    start_urls = ['https://www.3dmgame.com/release/pc{}/'.format(date) for date in dates]

    def __init__(self):
        self.r = redis.Redis(host='localhost',port=6379,db=0,password='123456')

    def parse(self, response):
        self.r.lpush('game_url',response.url)
        if response.xpath("//li[@class='next']") !=[]:
            yield scrapy.Request(response.xpath("//li[@class='next']/a/@href"),callback=self.parse)
        print(response.url)
