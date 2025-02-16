# -*- coding: UTF-8 -*-
"""
    @Project : MyScrapyLearn 
    @File    : quoteSpider.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/25 21:04 
    @NowThing: 
"""
import scrapy
from ..items import MyscrapyItem


class QuoteSpider(scrapy.Spider):
    name = "quoteSpider"
    start_urls = [
        "https://quotes.toscrape.com"
    ]

    @staticmethod
    def __pr__(*args):
        print("*" * 30)
        for arg in args:
            print(arg)
            print("*" * 30)

    def parse(self, response, *args, **kwargs):
        items = MyscrapyItem()
        all_div_datas = response.css("div.quote")
        for div_data in all_div_datas:
            title = div_data.css("span.text::text").extract()
            author = div_data.xpath("./span//small[@class='author']/text()").extract()
            tags = div_data.css("div.tags a.tag::text").extract()
            items["title"] = title
            items["author"] = author
            items["tags"] = tags
            yield items



