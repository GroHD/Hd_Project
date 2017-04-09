#!/usr/bin/env python

import pika
class GetClient(object):
    def __init__(self,userName,userPassword,host):
        self.userName = userName
        self.userPassword = userPassword
        self.host = host
    def GetConnection(self,userName,userPassword,host):
        credentials = pika.PlainCredentials(userName,userPassword) #要登陆的用户名和密码
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))#使用用户名和密码登陆那个服务器
        return connection
    def RecveMess(self):
        connection = self.GetConnection(self.userName,self.userPassword,self.host) #打开链接
        channel = connection.channel()#创建管道
        channel.queue_declare(queue='Message')#给队列命名,用来存取消息
        channel.basic_consume(CallBack,queue='Message')#从队列里拿到数据
        channel.start_consuming()
#回掉函数那数据
def CallBack(ch,method,properties,body):
    print("[x] Revce %s"%(body))
    print(properties.reply_to)
    #向客户端回数据
    ch.basic_publish(
                        exchange='',
                        routing_key=properties.reply_to,#回到那个随机队列里
                        properties=pika.BasicProperties(
                            #delivery_mode=2,#消息持久化
                            correlation_id=properties.correlation_id #随函数返回的uuid,用来确认当条消息
                        ),
                        body='OK' #回复的消息
                    )
   # ch.basic_ack(delivery_tag=method.delivery_tag)#消息持久化
    print("回复OK")
if __name__ == '__main__':
      con = GetClient('web_admin','123456','192.168.0.9')
      con.RecveMess()