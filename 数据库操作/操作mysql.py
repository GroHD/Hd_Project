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
       引入MySQLdb该模块不支持python3.0,该模块需要在Python2.0下使用

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

