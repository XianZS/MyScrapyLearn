# -*- coding: UTF-8 -*-
"""
    @Project : MyScrapyLearn 
    @File    : qutoes_spider.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/24 19:50 
    @NowThing: scrapy 开始学习
"""
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response, *args, **kwargs):
        print(self.name)
        print("--- CSS选择器 ---")
        title = response.css("title::text").extract()
        print(title)
        # Quotes to Scrape
        yield {
            "titleText": title
        }
