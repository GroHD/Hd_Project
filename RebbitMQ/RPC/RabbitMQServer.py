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
        credentials = pika.PlainCredentials(userName,userPassword)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
        return connection
    def SendMess(self):
        connection = self.GetConnection(self.userName,self.userPassword,self.host)
        channel = connection.channel()
        self.uid = uuid.uuid4()
        result = channel.queue_declare(exclusive=True)
        self.queueName = result.method.queue
        channel.basic_consume(self.CallBack, queue=self.queueName)
        channel.queue_declare(queue='Message')
        channel.basic_publish(
                            exchange='',
                            routing_key='Message',
                            properties=pika.BasicProperties(
                                reply_to=self.queueName,
                                correlation_id = str(self.uid)
                            ),
                            body=self.mess
                            )
        print("Send OK!!!")
        channel.start_consuming()
    def CallBack(self,ch,method,properties,body):
        if str(self.uid) == properties.correlation_id:
            print("Server Data Is %s"%(body))


if __name__ == '__main__':
    con = GetConnBase('Hello Word','web_admin','123456','192.168.0.9')
    con.SendMess()