#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
r'''
    Redis 
        Redis 可以持久化但是需要配置,默认是非持久化的，当系统重启之后就没有该数据了。
        Redis 是一个key-value 存储系统,和memcached类似，它支持存储的value类型相对更多，包括string,list set,zset和hash。这些数据类型都支持push/pop , add/remove 及取交集并集和差及更丰富的操作，并且这些都是原子性的。
        为了保证效率,数据都是缓存在内存中。区别的是redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文件，并且在此基础上实现了master-slave同步
        
    安装redis:
        wget http://download.redis.io/releases/redis-3.2.8.tar.gz
        tar xzf redis-3.0.6.tar.gz
        cd redis-3.0.6
        make
        
    启动服务端:
        src/redis-server     
        #再启动服务的时候,默认需要关闭保护  src/redis-server --protected-mode no  这样就可以关闭数据
        
    启动客户端:
        src/redis-cli
        redis> set foo bar  //存数据
        OK
        redis> get foo //取数据
        "bar"
        
        #还可以设置失效时间
        redis> set food yuxiangrousi   ex  5    #该数据5秒钟后就会失效
        
        redis> save  #保存内存数据到磁盘,重启服务器不会失去数据
        
'''
#基本操作
import  redis

r = redis.Redis(host='192.168.0.11') #连接redis 服务器
#print(r.get('name'))
#all_keys = r.keys() #拿到所有的key
r.set("age","男")#第一个参数是key  第二个参数是value  第三个参数是过期时间,如果没有第三个参数则一直保存到服务器内存中
print(str(r.get("age"),'utf8'))
r'''
    连接池:
        redis-py 使用connection pool 来管理对一个redis server的所有连接,避免每次建立。
        
        pool = redis.ConnectionPool(host='192.168.0.11',port=6397) #创建一个连接池
        
        r = redis.Redis(connection_pool = pool) #创建链接
        r.set('foo','Bar') #存数据
        print(r.get('foo')) #取数据
        
        
    set(name,value,ex=None,px=None,nx=Flase,xx=False)
        
    在Redis中设置值，默认,不存在则创建,存在则修改
    
        参数:
                ex  过期时间(秒)
                px  过期时间(毫秒)
                nx  如果设置为True,则只有name不存在时,当前set操作才执行
                xx  如果设置为True,则只有name存在时,当前set操作才执行

    setnx(name,value)
        设置值,只有name不存在时m执行操作(添加)
    setex(name,value,time)
        设置值,设置过期时间
            time 过期时间(数字秒或timedalta对象)
            
    mset(*args,**kwargs)
        批量设置值：
            如:
                mset(k1='v1',k2='v2')
                或
                mset({'k1':'v1','k2':'v2'})
                
    get(name)
        取值
        
    mget(keys,*args)
        批量获取值:
            如:
                mget('ylr','name')
                或
                mget([ylr,'name'])
    getset(name,value)
        设置新值并获取原来的值
        
    getrange(key,start,end)
        获取子序列(根据字节获取,非字符)
            参数:
                name,Redis的name
                start,起始位置(字节)
                end,结束位置(字节)
                
r.set('id', '123456789')

print(r.getrange('id', 1, 6))  # 拿到id的值从第1个开始到第6个结束 拿到的结果就是234567
'''
r'''
    setrange(name,offset,value)
        修改字符串内容,从制定字符串索引开始向后替换(新值太长时,则向后添加)
        参数:
            offset  字符串的索引，字节(一个汉字三个字节)
            vaelue  要设置的值
            
    setbit(name,offset,value)
        对name对应值的二进制表示的位进行操作
        参数:
            name:redis的name
            offset, 位的索引(将值变换成二进制后再进行索引)
            value  只能是1或0
            
    例:
        setbit('id',1,1) #把id中的value值的二进制 的第1位修改为1
        
'''

