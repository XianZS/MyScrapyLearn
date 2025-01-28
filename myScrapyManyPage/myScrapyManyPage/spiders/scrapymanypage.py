# -*- coding: UTF-8 -*-
"""
    @Project : MyScrapyLearn 
    @File    : scrapymanypage.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/28 10:37 
    @NowThing: 一次性爬取多个页面，运行这个代码，可以得到某著名算法网站的题目总数和题目概要
"""
import scrapy
from ..items import MyscrapymanypageItem


class ScrapyManyPageSpider(scrapy.Spider):
    name = "xxx"
    start_urls = [
        "https://www.acwing.com/problem/",
    ]
    index: int = 0
    url_list: list = ["/problem/"]

    # 主页面处理
    def parse(self, response, *args, **kwargs):
        a_all = response.xpath("//a/@href").extract()
        # 题目列表
        topic_url: list = []
        # 下一个题目页面的链接：str
        next_url: str = ""
        # 下一个题目页面的状态：bool 是否已经得到下一页面的链接
        next_judge: bool = False
        for a in a_all:
            # 筛选当前页面的题目列表
            if a.startswith("/problem/content/"):
                topic_url.append(a)
                continue
            # 得到下一个页面的题目
            if a.startswith("/problem/") and not next_judge:
                if a in self.url_list:
                    continue
                self.url_list.append(a)
                next_url = a
                next_judge = True

        print("next_url >>> ", next_url)
        for a_url in topic_url:
            yield response.follow(a_url, callback=self.show_info)
        if next_judge and self.index < 200:
            yield response.follow(next_url, callback=self.parse)

    # 单个题目处理页面
    def show_info(self, response, *args, **kwargs):
        title = response.xpath("//div[@class='nice_font problem-content-title']/text()").extract()
        self.index += 1
        print("index title >>> ", title[0].strip(), " ; index >>> ", self.index)

    # def parse1(self, response, *args, **kwargs):
    #     items = MyscrapymanypageItem()
    #     all_div_quotes = response.css("div.quote")
    #     for quotes in all_div_quotes:
    #         title = quotes.css("span.text::text").extract()
    #         author = quotes.css(".author::text").extract()
    #         tag = quotes.css(".tag::text").extract()
    #         items["title"] = title
    #         items["author"] = author
    #         items["tag"] = tag
    #         yield items
    #     next_page = response.xpath("//li[@class='next']/a/@href").get()
    #     if next_page is not None:
    #         # f"/page/{number}/"
    #         yield response.follow(next_page, callback=self.parse)
    #     self.index += 1
    #     print("[-=-=-= index =-=-=-]")
    #     print("index >>> ", self.index)
    #     # index >>> 10
