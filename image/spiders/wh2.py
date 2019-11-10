# -*- coding: utf-8 -*-
import scrapy


class Wh2Spider(scrapy.Spider):
    name = 'wh2'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['http://wallhaven.cc/toplist/?page=2']

    def parse(self, response):
        ul = response.xpath("//a[@class='preview']/@href").extract()  # .extract是提取爬取的数据的意思 .extract_first()是提取结果的第一个值
        # for i in range(len(ul)):  # 此处报错 Spider must return Request, BaseItem, dict or None, got 'str' in <GET https://wallhaven.cc/toplist/?page=2>
        #     ul1 = ul[i]
        #     yield ul1
        for i in range(len(ul)):
            item = {"url": ul[i]}
            yield item
