#!/usr/bin/env python

import pika
import uuid

class GetConnBase(object):
    def __init__(self,mess,userName,userPassword,host):
        self.mess = mess
        self.userName = userName
        self.userPassword = userPassword
        self.host = host
    def GetConnection(self,userName,userPassword,host):
        credentials = pika.PlainCredentials(userName,userPassword) #要登陆的用户名和密码
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials)) #打开连接
        return connection
    def SendMess(self):
        connection = self.GetConnection(self.userName,self.userPassword,self.host) #连接服务器
        channel = connection.channel() #申请管道
        self.uid = uuid.uuid4() #创建随机的uuid
        result = channel.queue_declare(exclusive=True) #生成随机的队列名称,使用完成后删除
        self.queueName = result.method.queue #拿到队列名字
        channel.basic_consume(self.CallBack, queue=self.queueName) #从随机队列里拿出数据
        channel.queue_declare(queue='Message')#定义向服务器发送数据
        channel.basic_publish(
                            exchange='',
                            routing_key='Message',
                            properties=pika.BasicProperties(
                                reply_to=self.queueName,#告诉服务器客户端接受的队列名称是什么
                               # delivery_mode=2,#消息持久化
                                correlation_id = str(self.uid) #确认消息的uuid,因为一个客户端可以有多条消息,这个是要确认使用那条消息
                            ),
                            body=self.mess#发送消息
                            )
        print("Send OK!!!")#发送完成
        channel.start_consuming()#等待接收
    def CallBack(self,ch,method,properties,body):
        if str(self.uid) == properties.correlation_id: #判断是否是本条回复的消息
            print("Server Data Is %s"%(body))
            # ch.basic_ack(delivery_tag=method.delivery_tag)#消息持久化


if __name__ == '__main__':
    con = GetConnBase('Hello Word','web_admin','123456','192.168.0.9')
    con.SendMess()