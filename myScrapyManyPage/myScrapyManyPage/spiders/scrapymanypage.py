# -*- coding: UTF-8 -*-
"""
    @Project : MyScrapyLearn 
    @File    : scrapymanypage.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/28 10:37 
    @NowThing: 一次性爬取多个页面
"""
import scrapy
from ..items import MyscrapymanypageItem


class ScrapyManyPageSpider(scrapy.Spider):
    name = "mpSpider"
    start_urls = [
        "https://quotes.toscrape.com",
    ]
    index: int = 0

    def parse(self, response, *args, **kwargs):
        items = MyscrapymanypageItem()
        all_div_quotes = response.css("div.quote")
        for quotes in all_div_quotes:
            title = quotes.css("span.text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css(".tag::text").extract()
            items["title"] = title
            items["author"] = author
            items["tag"] = tag
            yield items
        next_page = response.xpath("//li[@class='next']/a/@href").get()
        # next_page2 = response.css("li.next a::attr(href)").get()
        # print("-=-=-=-=" * 10)
        # print(next_page, next_page2)
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        self.index += 1
        print("[-=-=-= index =-=-=-]")
        print("index >>> ", self.index)
