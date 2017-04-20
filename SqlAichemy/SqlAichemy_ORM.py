#!/usr/bin/env python
#-*-coding:utf-8-*-
r'''
    SqlAlchmey是python 编程语言下的一款ORM框架,该框架建立在数据库API之上，使用关系对象映射进行数据库操作，简而言之就是:将对象转换成SQL,然后使用数据库API执行SQL并获取执行结果

    步骤1：
        先下载安装sqlalchemy包,然后from sqlalchemy 这个包进行使用

执行原生态的sql

from sqlalchemy import create_engine


#执行sql插入语句
engine = create_engine("mysql+mysqldb://root:123@127.0.0.1:3306/mydb")
engine.execute(
    'insert into ts_test(a,b) values(%(id)s,%(name)s)',
    id=999,name='v1'
)
#执行sql查询语句
result = engine.execute('select * from ts_test')
result.fetchall()  #取出结果
'''

r'''
执行orm 映射的sql
'''
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey
#执行MetaData 后返回一个实力
metadata = MetaData()

user = Table('TableName',metadata,
            Column('ID',Integer,primary_key=True), #主键
            Column('Name',String(20)) #姓名

            )
#mysql+mysqldb”指定了使用 MySQL-Python 来连接，“root”和“123”分别是用户名和密码，“localhost”是数据库的域名，“test”是使用的数据库名（可省略），“charset”指定了连接时使用的字符集（可省略）
#create_engine() 会返回一个数据库引擎，echo 参数为 True 时，会显示每条执行的 SQL 语句，生产环境下可关闭
engine = create_engine("mysql+mysqldb://root:123456//localhost:3306/test?charset=utf8",max_overflow=5,echo=True)

metadata.create_all() #创建表