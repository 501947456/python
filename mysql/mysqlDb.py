
#!/usr/bin/env python
## -*- coding:utf-8 -*-

'''
    Description: ---MySQL类
'''

import MySQLdb

class ClassDb:
    def connect(self, **args):
        ## 连接数据库
        self.host = args['host']
        self.port = args['port']
        self.user = args['user']
        self.passwd = args['passwd']
        self.db = args['db']
        self.charset = args['charset']
        try:
            self.conn = MySQLdb.connect(host=self.host,port=self.port,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
            self.cursor = self.conn.cursor(cursorclass = MySQLdb.cursors.DictCursor) ## 查询结果以字典形式显示
        except Exception,err:
            print str(err)

    def execute(self, sql):
        ## 执行SQL语句, 传入sql语句
        try:
            self.cursor.execute(sql)
        finally:
            pass
        self.conn.commit()

    def fetchall(self):
        ## 返回查询的所有数据内容,数据类型:元组
        return self.cursor.fetchall()

    def fetchone(self):
        ## 返回查询的单条数据内容,数据类型:字典
        return self.cursor.fetchone()
