# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .database import DataBase


class MyscrapyPipeline:
    def __init__(self):
        # 创建临时数据存储源：some
        self.some = DataBase("some")

    def open_spider(self, spider):
        print("========== 爬虫开始了 ============")
        print("++++++++++ 初始化表操作 ++++++++++")
        judge = self.some.createTable("myNewDataBaseThings", "author text", "tags text", "title text")
        print("judge:", judge)

    def process_item(self, item, spider):
        print("++++++++++ 插入表操作 ++++++++++")
        try:
            self.some.insertTable("myNewDataBaseThings",
                                  ','.join(item["author"]), ','.join(item["tags"]), ','.join(item["title"]))
        except Exception as e:
            print("item:", item)
            print("e:", e)
        return item

