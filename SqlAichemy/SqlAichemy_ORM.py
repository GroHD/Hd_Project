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
from sqlalchemy import create_engine,Table,Column,Integer,String,MetaData,ForeignKey,select,and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship,session
#mysql+mysqldb”指定了使用 MySQL-Python 来连接，“root”和“123”分别是用户名和密码，“localhost”是数据库的域名，“test”是使用的数据库名（可省略），“charset”指定了连接时使用的字符集（可省略）
#create_engine() 会返回一个数据库引擎，echo 参数为 True 时，会显示每条执行的 SQL 语句，生产环境下可关闭
engine = create_engine("mysql+mysqldb://root:123456//localhost:3306/test?charset=utf8",max_overflow=5,echo=True)
#执行MetaData 后返回一个实力
metadata = MetaData(bind=engine,reflect=True)

user = Table('TableName',metadata,
            Column('ID',Integer,primary_key=True), #主键  z自增id
            Column('Name',String(20)) #姓名

            )


metadata.create_all() #创建表


r'''
#插入数据
'''
conn = engine.connect() #拿到游标
sql = user.insert().values(name='hd') #插入数据
conn.execute(sql)#执行sql
conn.close()

r'''
#删除数据
'''
sql = user.delete().where(user.c.ID >1) #删除ID大于1的数据
conn.execute(sql)#执行sql
conn.close()

r'''
#修改数据
'''
sql = user.update().where(user.c.ID=='1').values(name='nn')
conn.execute(sql)#执行sql语句
conn.close()

r'''
#查找数据
'''
sql =select([user.c.ID]) #查询出列表中的ID
res = conn.execute(sql)
print(res.fetchall()) #去除结果

#根据条件查询结果
sql = select([user,]).where(user.c.ID == 1)
res = conn.execute(sql)
print(res.fetchall())


r'''
   不用写sql语句的orm
'''
Base = declarative_base() #生成一个SQLORM基类，所有的子类都需要继承该类
#映射表
class Host(Base):
        __tablename__='hosts'
        id = Column(Integer,primary_key=True,autoincrement=True)
        hostname = Column(String(64),unique=True,unllable=False)
        ip_addr = Column(String(48),unique=True,nullable=False)
        port = Column(Integer,default=22)

Base.metadata.create_all(engine)#创建表

def main():
    SessionCls = sessionmaker(bind=engine)#创建于数据库的会话sess class ，注意这里返回给session的是一个类不是实例
    session = SessionCls() #创建连接实例
    #添加数据
    h1 = Host(hostname='localhost',ip_addr='127.0.0.1')
    h2 = Host(hostname='ubuntu',ip_addr='192.168.1.55',port=8822)
    #session.add(h1)
    #session.add(h2)
    session.add_all([h1,h2]) #批量执行
    session.commit()#执行方法

    #查询数据  会返回查询到的数据
    obj = session.query(Host).filter(Host.hostname=='localhost').first() #拿到第一条数据, all() 拿到所有的数据
    #like查询
    obj = session.query(Host).filter(Host.hostname.like('%ed%')) #like查询
    #in 查询
    obj = session.query(Host).filter(Host.hostname.in_(['ed','he','hh']))#in 查询
    # and和or 查询   需要sqlaichemy 导入and__ 和or_
    from sqlalchemy import add_,or_
    obj = session.query(Host).filter(and_(Host.hostname.like('ubuntu%'),Host.port >20)).all() # 查询host表hostname等于ubuntu 并且port 大于20
    print(obj.id)
    #修改数据
    obj.hostname ='test server'
    #删除数据
    session.delete(obj)
    session.commit()#执行方法

    #可以使用order_by(Host.port) 来排序

r'''
    多对多关联:

'''
class Parent(Base):
    __tablename__ ="parent"
    id = Column(Integer,primary_key=True)
    name = Column(String(20),unique=True,unllable=False)
class Child(Base):
        __tablename__ ='child'
        id = Column(Integer,primary_key=True)
        parent_id = Column(Integer,ForeignKey('parent.id'))  #这是父外键
        parent = relationship('Parent',backref='host_list') #关联外键,需要从sqlalichemy.ORM 里导入relationship,写完这句话就可以在外键关联中的表查询中使用children字段来拿到对应数据,括号里的参数是类名,第二个参数就是反向关联,
        
obj = Child().query(Child.parent_id == 1).all(); # 拿到child 节点力的所有数据
print(obj.parent.name)#拿到外键关联的id

r'''
 join 查询
  在sqlalchemy 里导入func模块就可以使用count   sum 这些函数
'''
from sqlalchemy import func

objes = session.query(Child,func.count(Child.parent.name),Child.Parent.name).group_by(Child.Parent.name).all()  #查询出当前Parent表中按name字段进行分组计算 
objs = session.query(Parent,func.count(Parent.name)).join(Child.parent).filter(Child.parent == 1).group_by(Parent.name).all() #进行join查询然后进行分组统计
objs = session.query(Child).join(Parent).filter(Parent == 1).all() #join查询出 Child表中引用的Parent的主键有哪些，filter是where条件
objs = session.query(Child,func.count(Child.parent_id),Child.id,Parent.name).join(Parent).group_by().all() #分组查询,然后列出对应的数据 类似于下面的sql语句
'''
select count(*),th.teachName,cla.claName from Child  th
left join Parent cla on cla.ID = th.parent_id
GROUP BY th.parent_id
'''
objs = session.query(Parent).join(Child.parent).filter(Child.parent == 1).group_by(Child.name).all()  
r'''
 关联查询
    关联查询需要建立一张中间表,然后再relationship 的时候使用secondary 进行设置中间表
    backref 在关系的另一个模型中添加反向引用
    primaryjoin 明确指定两个模型之间使用的联结条件，只在模棱两可的关系中需要指定
    lazy    指定如何加载相关记录。有可选值有select(首次访问按需要加载),immediate(源对象加载后就加载)，joined(加载记录,但使用联结)，subquery(立即加载,但使用子查询),noload(永不加载)和dynamic(不加载记录,但提供加载记录的查询)
    uselist     如果设为false,不使用列表,而使用标量值
    order_by    指定关系中记录的排序方式
    secondary   指定多对多关系中关系表的名字
    
'''

Parent = relationship('Parent',secondary='ParentToChild',backref='Child') #设置中间表和双向关联
if __name__ == '__main__':
    main()

r'''
    多表查询
'''

