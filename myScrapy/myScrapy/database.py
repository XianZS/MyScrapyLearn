# -*- coding: UTF-8 -*-
"""
    @Project : MyScrapyLearn 
    @File    : database.py
    @IDE     : PyCharm 
    @Author  : XianZS
    @Date    : 2025/1/26 17:57 
    @NowThing: 数据库操作文件
"""
import sqlite3

class DataBase:
    """
    向外暴露数据库操作类 DataBase
    该类用于连接和操作SQLite数据库。
    Attributes:
        conn (sqlite3.Connection): 数据库连接对象。
        curr (sqlite3.Cursor): 数据库游标对象。
    """

    def __init__(self, dataBaseName):
        """
        初始化数据库连接

        Args:
            dataBaseName (str): 数据库名称。
        """
        # 连接到指定的SQLite数据库
        self.conn = sqlite3.connect(f"./data/{dataBaseName}.db")
        # 创建一个游标对象，用于执行SQL语句
        self.curr = self.conn.cursor()

    def createTable(self, tableName, *args):
        """
        创建一个新的表

        Args:
            tableName (str): 表名
            *args (str): 表的列名和数据类型，例如 "id INTEGER", "name TEXT"
        """
        strs = f"create table if not exists {tableName} ({','.join(args)});"
        try:
            self.curr.execute(strs)
            self.conn.commit()  # 提交事务
            return True
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
            return False

    def insertTable(self, tableName, *args):
        """
        向表中插入数据

        Args:
            tableName (str): 表名
            *args (str): 要插入的数据，例如 "1", "John Doe", "john.doe@example.com"
        """
        args = [f"'{arg}'" for arg in args]
        # args = [f"'{arg}'" if isinstance(arg, str) else str(arg) for arg in args]
        strs = f"insert into {tableName} values({','.join(args)});"
        # print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        # print("strs : ", strs)
        self.curr.execute(strs)
        self.conn.commit()

    def dropTable(self, tableName):
        """
        删除表

        Args:
            tableName (str): 要删除的表名
        """
        strs = f"drop table {tableName};"
        print("strs : ", strs)
        self.curr.execute(strs)

    def close(self):
        """
        关闭数据库连接
        """
        self.conn.close()


if __name__ == "__main__":
    # 创建一个DataBase类的实例，连接到名为"myData"的数据库
    dataBase = DataBase("myData")
    dataBase.createTable("myTable", "title text", "author text", "tags text")
    dataBase.insertTable("myTable", "test", "test", "test")
    dataBase.dropTable("myDataBaseThings")
    dataBase.close()
