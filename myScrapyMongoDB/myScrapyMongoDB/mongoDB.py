# -*- coding: UTF-8 -*-
"""
    @Project : MyScrapyLearn 
    @File    : mongoDB.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/27 18:07 
    @NowThing: 
"""
import pymongo


class MyMongoDB:
    def __init__(self):
        """
        初始化MyMongoDB类的实例。

        该方法创建一个MongoDB客户端连接，并选择要使用的数据库和集合。

        Attributes:
            conn (pymongo.MongoClient): MongoDB客户端连接对象。
            collection (pymongo.collection.Collection): 选择的集合对象。
        """
        # host = '39.100.73.172'
        # username = 'social'
        # password = 'YangHaiTao3135'
        # port = '27017'
        # db = 'social'
        # 创建一个MongoDB客户端连接，指定主机和端口
        # self.conn = pymongo.MongoClient('mongodb://{0}:{1}@{2}:{3}/?authSource={4}&authMechanism=SCRAM-SHA-1'.
        #                                 format(username, password, host, port, db))
        self.conn = pymongo.MongoClient(
            host='39.100.73.172',
            port=27017,
            username='social',
            password='YangHaiTao3135',
            authSource='social',
        )
        # 选择名为'social'的数据库
        db = self.conn['social']
        # 选择名为'test_table'的集合
        self.collection = db["test2"]

    def insert_one_things(self, **kwargs):
        print(kwargs)
        res = self.collection.insert_one(kwargs)
        print(res.inserted_id)

    def insert_many_things(self, *args, **kwargs):
        print(args[0])
        res = self.collection.insert_many(args[0])
        print(res.inserted_ids)


myMongoDB = MyMongoDB()
myMongoDB.insert_one_things(name="XianZS", age=20)
myMongoDB.insert_many_things([
    {"name": "jom", "age": 20},
    {"name": "kom", "age": 21},
    {"name": "lom", "age": 22},
])
