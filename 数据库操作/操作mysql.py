#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
r'''
    Python 操作Mysql模块的安装  
    linux
            yum install MySQL-python
    window：
            http://files.cnblogs.files/wupeiqi/py-mysql-win.zip
'''

r'''
       引入MySQLdb该模块不支持python3.0,该模块需要在Python2.0下使用  Python3.X 可以使用pymysql 进行数据库操作

        import MySQLdb
        conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='1234',db='mydb')
        cur=conn.cursor() #连接上mysql 看游标处于哪个数据库,现在处于 mydb 数据库
        reCount = cur.exeute('SELECT * FROM MYTABLE') #执行sql 语句
        reCount = cur.exeute('insert into MYTABLE(name,age,gender) VALUES(%S,%d,%s)',('hd',22,'男'))#执行插入语句
        li=[
              ('hd',22,'男'),
              ('nn',27,'女'),
              ('hd',22,'男'),
              ('hd',22,'男'),
              ('hd',22,'男'),
              ('hd',22,'男'),
              ('hd',22,'男'),
            ]
        reCount = cur.exeutemany('insert into MYTABLE(name,age,gender) VALUES(%s,%d,%s)',li) #可以一次可以插入多条语句
        exeuct 也可以执行update
        res = cur.fetchone() 查询一条数据
        res = cur.fetchall() #查询出所有的数据
        res = cur.fetchmany(3) #查询三条数据
        reCount.commit() #提交数据
        cur.close() #关闭链接
        conn.close()#关闭连接

    回滚和事物:
        conn.rollback() #事物回滚！ 出错的时候执行事务回滚,回滚到本次所有sql语句执行之前的结果。
        conn.commit() 事物提交
'''

#pymysql Python3.X下进行mysql数据操作

import pymysql
#打开数据库
db = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='dbgas',charset='utf8')
#使用cursor() 方法创建一个游标cursor
cursor = db.cursor()

#如果执行的是sql插入语句，则需要使用Try来获取错误,因为插入的时候可能会出现错误
try:
    sql = '''
          insert into 用户表
            '''
    #cursor.execute(sql)
    #没有出错执行提交语句
    #db.commit()#提交数据

    r'''
        在执行插入语句的时候也可以使用参数
 '''
   # cursor.execute('insert into log values(%s,%s,%s)'%('1','2','3')) #这样也可以插入语句
except:
    pass
    #db.rollback()#出错就执行回滚

r'''
    数据库查询操作
    python查询mysql使用fetchone()方法获取单挑数据，使用fetchall() 方法获取多条数据
    fetchone(): 该方法获取下一个查询结果集，结果集是一个对象
    fetchall(): 接受全部的返回结果行
    rowcount:这是一个只读属性,返回执行execute()方法影响的行数
'''
#例
cursor.execute('select * from 用户表')
result = cursor.fetchall()
for row in result:
    print(row)

#关闭数据库
db.close()
