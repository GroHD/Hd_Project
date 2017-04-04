#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
r'''
    RabbitMQ 是一个在AMQP基础上完整的，可复用的企业消息系统。
    MQ全程为Message Queue消息队列,是一种应用程序对应程序的通信方法。应用程序通过读写出入队列的消息来通信，而无须专用连接来裂解他们。消息传递指的是程序之间通过在消息中发送数据进行通信，而不是通过直接调用彼此来通信,直接调用通常是用于诸如远程过程调用的技术。
    
    RabibitMQ安装:
        安装配置epel源:
             wget http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
        安装erlang:
            wget http://erlang.org/download/otp_src_19.3.tar.gz 
        安装RebibitMQ
            yum -y install rabbitmq-server
            
        安装API:
            pip install pika #官方的
            
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
                        body='Hello Word!')
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

channel.basic_publish(callback,queue='hello',no_ack=True)
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






