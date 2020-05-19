# -*- coding: utf-8 -*-
import scrapy


class DongcaiSpider(scrapy.Spider):
    name = 'dongcai'
    allowed_domains = [''eastmoney.com'']
    start_urls = ['http://'eastmoney.com'/']

    def parse(self, response):
        pass
