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
        
        
        getbit('id',1) #获取id所属的value里的值得第一个
        
        
    delete('id') #删除id
    
    
    bitcount(name,start=None,end=None) 
        获取name中对应的二进制表中的1的个数:
        参数:
            name  redis name
            start  位起始位置
            end  位结束为止
            
    strlen(name) 
        返回name对应值的字节长度(一个汉子3个字节)
        
    incr(name,amouunt=1)
     自增name对应的值,当name不存在时,则创建name=amount,否则,自增。
     
     参数:
        name Redis的name
        amount,自增数（必须是整数）
        
    r.incr('cont',1)
    r.incr('cont',1)
    r.incr('cont',1)
    r.get('count') #获取到的是7
    
    decr(name,amount=1)
        自减name对应的值,当name不存在时,则创建name=amount,否则自减
        参数:
            name,Redis的name
            amount,自减数(整数)
            
    append(key,value)
        在Redis的name对应的值后面追加内容
        参数:
            key  redis的name
            value  要追加的字符串内容
            
    
    Hash操作:
        hset(name,key,value)
            name对应的hash中设置一个键值对(不存在则创建,否则修改)
            参数:
                name redis的name
                key name对应的hash中的key
                value name对应的hash中的value
                
        r.hset('person','name',"hd") #添加
        
        hmset(name,*keys);
            name 对应的hash中设置一个字典:
                name redis中的name
                keys 存入的字典
                
        r.hmset('Person',{"name":"hd","age":"29","sex":"nan"})
        
        r.hget("person","name") #拿到字典中的name值
        r.hgetall('person')  获取全部的值
        
        r.hlen('name')
            获取name对应的hash中的键值对的个数
        r.hkeys(name)
            获取name对应的hash中所有的key的值
            
        r.hvalue(name)
            获取name对应的hash中所有的value的值
            
        r.hexiste(name,key)
            检查name对应的hash是否存在当前传入的key
            
        r.hdel(name,*keys)
            将name对应的hash中制定的key的键值对删除
            
        r.hscan(name,cursor=0,match=None,count=None)
        增量式迭代获取数据,对于数据量大的数据非常有用,hscan可以实现分片的获取数据,并非一次将数据加载到内存中
        参数:
            name  redis的name
            cursor 游标(给予游标分批获取数据)
            match,匹配指定key,默认None 表示匹配所有key
            count 每次分片最少获取个数,默认None表示采用Redis的默认分片个数
            
        例:
            cursor1,data1 = r.hscan('xx',cursor=0,match=None,ccount=None)
            cursor2,data1 = r.hscan('xx',cursor=cursor1,match=None,ccount=None)
            ......
            
    List操作:
        redis中的List在内存中按照一个name对应一个List来存储的：
            
        lpush(name,values)
            在name对应的list中添加元素,每个新的元素都添加到列表的最左边
            如:
                r.lpush('poo',11,22,33,44)
                保存为:
                    44,33,22,11
                扩展：
                    r.rpush(name,values) 表示从右向左的操作
        lrange(name,start,end)
            根据name获取redis里的列表
            参数:
                name redis里的name
                start 开始的下标0
                end  结束的下标-1
                
        llen(name)
            name对应的list元素的个数
        linsert(name,where,refvalue,value)
            在name对应的列表的某一个值前或后插入一个心智
            参数:
                name redis的name
                where "BEFORD"或"AFTER"
                refvalue 标杆值,既:在它前或后插入数据  这个是对应的值
                value:要插入的值
                
        r.lset(name,index,value)
            在name对应的列表的index位置设置成value值
            参数:
                name redis的name
                index  列表对应的下标
                value 要插入的值
                
                
    Set才做,Set集合就是不允许重复的列表
    
        r.sadd(name,value)
            name对应的集合中添加元素value
        r.sscard(name)
            获取name对应的集合中元素个数
        r.sscan(name)
            获取name对应的集合元素
        r.sdiff(name1,name2)
            集合对比两个存在的列表,返回两个列表中都存在的元素
        r.sdiffstore(dest,keys,*args)
            获取第一个name对应的集合中且不再其他name对应的集合中,再将其新加入到dest对应的列表中
                r.sdiffstore('s3','s1','s2')
                把s1和s2的差集存入到s3
        r.sismember(name,value)
            value是否存在name集合中
        r.smembers('s1')
            获取s1中所有的元素
        
        r.move(src,dse,value) 返回True, 
            将value从src移动到dse集合中,插入到开头
        r.pop(name)
            从集合的右侧(尾部)移除一个成员,并将其返回
        r.srandmember(name,numbers)
            从name中随机获取numbers个元素
        r.srem(name,values)
            在name对应的集合中删除某些值
            
        r.sunion(keys,*args)
            获取一个或多个name的合集
        r.sunionstore(dest,keys,*arhs)
            获取一个或多个name对应的集合的并集,并将结果保存到dest对应的集合中
          
    有序集合:
        r.zadd(name,*args)
            例:
                r.zadd('name','hd',4,'age',7) 4和7是 对元素进行排序
                或
                r.zadd('name',"hd"=4,"age"=7)
        r.zcard(name)
            获取name对应的有序集合元素的个数
        r.zcount(name,min,max)
            获取name对应的有序集合众分数在[min~max]之间的元素
        r.zincrby(name,value,amount)
            自增name对应的有序集合的value对应的分数
        
            
            
'''

