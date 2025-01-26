# -*- coding: UTF-8 -*-
"""
    @Project : MyScrapyLearn 
    @File    : saveSpider.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/26 14:05 
    @NowThing: 保存 save 数据
"""
import scrapy
from ..items import MyscrapyItem


class SaveSpider(scrapy.Spider):
    name = 'saveSpider'
    start_urls = [
        "https://quotes.toscrape.com"
    ]

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
