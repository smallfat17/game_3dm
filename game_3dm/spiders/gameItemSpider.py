import scrapy
from scrapy_redis.spiders import RedisSpider
from ..items import Game3DmItem

class itemSpider(RedisSpider):
    name = 'game_item_3dm'
    allowed_domains = ['www.3dmgame.com']
    redis_key = 'game_url'

    def parse(self, response):
        for sel in response.xpath("//div[@class='Sale_list']/div[@class='lis']"):
            item = Game3DmItem()
            item['Cname'] = sel.xpath("div[@class='bt']/a/text()").extract()[0]
            item['Ename'] = sel.xpath("div[@class='bt']/span/text()").extract()
            item['developer'] = sel.xpath("ul/li[1]/text()").extract()[0].split("：")[1]
            item['publisher'] = sel.xpath("ul/li[2]/text()").extract()[0].split("：")[1]
            item['pub_date'] = sel.xpath("ul/li[3]/span/text()").extract()[0]
            # item['pub_date'] = item['pub_date'].replace('年','-').replace('月','-')+'01' if '年' in item['pub_date'] else item['pub_date']
            # item['pub_date'] = item['pub_date']+'-01' if item['pub_date'].count('-')==1 else item['pub_date']
            item['game_type'] = sel.xpath("ul/li[4]/text()").extract()[0].split("：")[1]
            item['station'] = sel.xpath("ul/li[5]/text()").extract()[0].split("：")[1]
            item['lang'] = sel.xpath("ul/li[6]/text()").extract()[0].split("：")[1]
            item['label'] = str(sel.xpath("ul/li[7]/a/text()").extract())
            print(item)
            yield item
