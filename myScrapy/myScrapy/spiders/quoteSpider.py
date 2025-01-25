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
        all_div_datas = response.css("div.quote")
        title = all_div_datas.css("span.text::text").extract()
        author = all_div_datas.xpath("./span//small[@class='author']/text()").extract()
        tags = all_div_datas.css("div.tags a.tag::text").extract()
        print("len >>> ", len(all_div_datas), " >>> ", len(title), " >>> ", len(author), " >>> ", len(tags))
        self.__pr__(title, author, tags)
        yield {
            "title": title,
            "author": author,
            "tags": tags
        }


"""
    ******************************
    ['“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”']
    ******************************
    ['Albert Einstein']
    ******************************
    ['change', 'deep-thoughts', 'thinking', 'world']
    ******************************
"""
