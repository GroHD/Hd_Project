#!/usr/bin/env python

import pika
class GetClient(object):
    def __init__(self,userName,userPassword,host):
        self.userName = userName
        self.userPassword = userPassword
        self.host = host
    def GetConnection(self,userName,userPassword,host):
        credentials = pika.PlainCredentials(userName,userPassword)
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=host,credentials=credentials))
        return connection
    def RecveMess(self):
        connection = self.GetConnection(self.userName,self.userPassword,self.host)
        channel = connection.channel()
        channel.queue_declare(queue='Message')
        channel.basic_consume(CallBack,queue='Message')
        channel.start_consuming()

def CallBack(ch,method,properties,body):
    print("[x] Revce %s"%(body))
    print(properties.reply_to)
    ch.basic_publish(
                        exchange='',
                        routing_key=properties.reply_to,
                        properties=pika.BasicProperties(
                            correlation_id=properties.correlation_id
                        ),
                        body='OK'
                    )
    print("回复OK")
if __name__ == '__main__':
      con = GetClient('web_admin','123456','192.168.0.9')
      con.RecveMess()