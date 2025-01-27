# -*- coding: UTF-8 -*-
"""
    @Project : MyScrapyLearn 
    @File    : mySql.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/27 14:45 
    @NowThing: 
"""
import mysql.connector


class MySql:
    def __init__(self):
        # 连接到 MySQL 数据库
        self.conn = mysql.connector.connect(
            # 数据库主机地址
            host="39.100.73.172",
            # 数据库用户名
            user="social",
            # 数据库密码
            passwd="YangHaiTao3135",
            # 数据库名称
            database="social",
            # 设置字符编码为 utf8mb4
            charset='utf8mb4'
        )

        self.cursor = self.conn.cursor()

    def createTable(self, tableName, *args):
        self.cursor.execute(f"create table if not exists {tableName} ({','.join(args)});")


mySql = MySql()
mySql.createTable("myTable", "name text", "age int", "address text")
