#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
r'''

    RabbitMQ 是一个在AMQP基础上完整的，可复用的企业消息系统。
    MQ全程为Message Queue消息队列,是一种应用程序对应程序的通信方法。应用程序通过读写出入队列的消息来通信，而无须专用连接来裂解他们。消息传递指的是程序之间通过在消息中发送数据进行通信，而不是通过直接调用彼此来通信,直接调用通常是用于诸如远程过程调用的技术。
    
    RabibitMQ安装:
        主要的页面:
            http://www.cnblogs.com/astroboyx/archive/2012/04/09/2739902.html
        安装配置epel源:
             wget http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
        安装erlang:
            wget http://erlang.org/download/otp_src_R16B03.tar.gz
                1.然后解压下载的gz包 tar  -zxvf  *.tar.gz
                2.cd 进入解压出来的文件夹
                3.执行./configure --prefix=/usr/local/erlang  就会开始编译安装  会编译到 /usr/local/erlang 下 如果不报错就执行make 和 make install
                   报错：
                        configure: error: No curses library functions found
                        configure: error: /bin/sh '/root/otp/erts/configure' failed for erts
                    执行:
                        sudo apt-get install libncurses5-dev 
                    然后再执行./configure

                    编译完成以后，进入/opt/erlang，输入erl测试erlang是否安装成功。

                4.
        安装RebibitMQ
           wget http://www.rabbitmq.com/releases/rabbitmq-server/
            解压:
                tar zxvf rabbitmq-server-generic-unix-2.7.1.tar.gz -C /opt
            cd rabbitmq/sbin 
                        ./rabbitmq-server -detached可以实现后台启动
                            
            修改/etc/profile，添加环境变量
            #set rabbitmq environment
            export PATH=$PATH:/opt/rabbitmq/sbi
            source profile使得文件生效
            cd /opt/rabbitmq/sbin  ./rabbitmqctl stop/start关闭/启动rabbitmq

            添加用户:
                sudo rabbitmqctl add_user web_admin  123456
            删除用户:
                sudo rabbitmqctl delete_user web_admin
            查看用户:
                sudo rabbitmqctl list_users
            添加vhost:
                sudo rabbitmqctl add_vhost vhost1
            查看vhost:
                sudo rabbitmqctl list_permissions -p /vhost1
            给用户添加权限:
                sudo rabbitmqctl set_permissions -p / web_admin '.*''.*''.*'
        安装API:
            pip install pika #官方的

            水水水水水水水水水水水水水水水水水水水
            
'''
 #发送数据端
import pika
#阻塞的连接,链接localhost 服务器
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#生成一个管道
channel = connection.channel()
#在管道里申明一个queue,队列的名字是hello
channel.queue_declare(queue='hello')

channel.basic_publish(
                        exchange='',
                        routing_key='hello',
                        body='Hello Word!'
                        )
#参数:
'''
    exchange:
        消息控制器,用来区分消息使用那个消息队列来处理的,默认是空
    routing_key
         是消息队列名称
    body:
        发送消息内容
'''
print("[x] Sent'Hello World!'!")

connection.close() #关闭


#接受数据段端(client)
#阻塞的链接,
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#生成一个管道
channel = connection.channel()
#在管道里声明一个queue队列,名字是hello,当有hello这个队列的话,则忽略该方法,否则就生成队列
channel.queue_declare('hello')
#回掉函数
def callback(ch,method,propertis,body):
    print("[x] Received%r"%body)
channel.basic_consume(callback,queue='hello',no_ack=True)
'''
    参数：
        callback  回掉函数,收到小心后就调用这个函数
        queue  从那个队列里收取信息
        no_ack  是否需要确认,True 是不需要确认,False的时候当消息处理完毕,会给服务器发送一个确认消息
'''

channel.start_consuming()#开始接受数据阻塞

r'''
    如果有两个消费者(client) 一个生产者(client),消息会轮询的向每个消费者发送,第一条消息会发送到A客户端,第二个会发到B客户端,然后以此发送数据。。。。
'''
r'''

消息持久化:
    #队列持久化
    在管道里声明queue队列名字的时候,如果个加一durable=True就是消息持久化,这个queue在定义的是定义为不是持久化或是持久化，那么是无法修改的，要不删掉,要么定义别的。
    在写消息持久化的时候必须接收端和发送端是一致的,需要消息持久化的话需要在客户端和服务端分别增加一些消息持久化代码
  #消息持久化
    服务器写把下面的代码写到basic_publish里:
         properties=pika.BasicProperties(
                            delivery_mode=2
                        )
    把下面的代码写到客户端的回掉函数里:
        ch.basic_ack(delivery_tag= method.delivery_tag)
'''

r'''
channel_le.basic_qos(prefetch_count=1) #定义同时只取一个任务,那么久不会进来多个数据  这个就是防止在不同配置服务器上出现处理消息不一致的情况。

'''
r'''
消息发布和订阅:
'''
r'''
消息发布:
'''
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel= connection.channel()
# 因为是广播所以不需要定义queue的名字
channel.exchange_declare(exchange='logs',
                         type='faout'
                         )

message = 'Hello!Word'
r'''
    Type参数:
    fanout
    所有bind到此exchange的queue都可以接收消息  
    direct
    通过routingKey和exchange决定的那个唯一的queue可以接收消息
    
    topic
    所有符合routingKey(此时可以是一个表达式)的routingKey所bind的queue可以接收消息
    表达式符号说明：#代表一个或多个字符，*代表任何字符
    例：#.a会匹配a.a，aa.a，aaa.a等
    *.a会匹配a.a，b.a，c.a等
    注：使用RoutingKey为#，Exchange Type为topic的时候相当于使用fanout
'''

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message
                     )
print("[x] Send %r"%message)
connection.close() #关闭发送消息


r'''消息接受端'''
connection  = pika.BlockingConnection(pika.ConnectionParameters('localhos'))
channel = connection.channel()
channel.exchange_declare(exchange='logs',type='faout')
result = channel.queue_declare(exclusive=True) #不指定queue名字,reabbit会随机分配名字,当接收完消息之后就删除该名字
queue_name = result.method.queue
channel.queue_bind(exchange='logs',routing_key='',queue=queue_name) #queue绑定到exchange上开始接受消息,如果type是direct,那么可以循环绑定 routing_key


print("等待接受数据....")

def callbackMess(ch,method,perperties,body):
    print("接受到的消息是:%s"%body)
    return

channel.basic_consume(callbackMess,queue=queue_name,no_ack=True)



channel.start_consuming()

r'''
    type类型:
        faout  任何消息
        direct：
                根据routing_key 来分发队列,然后再接收端可以根据routing_key 进行取出对应的数据，比如在服务端放入routing_key 里方法Info里,那么在消息接收端里可以从routing_key里的info里 取出数据

'''





r'''链接远程失败:
      添加一个用户
      rabbitmqctl add_user rollen root
      设置权限
      rabbitmqctl set_user_tags rollen administrator
      //开启可以远程连接
      rabbitmqctl set_permissions -p / rollen ".*" ".*" ".*"
'''


