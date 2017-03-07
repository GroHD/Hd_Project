#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
r'''
    生产消费者可以使用多线程下的queue 队列进行加载
'''
from multiprocessing import Process,Queue
import time

def ShengChan(que,name):
    while True:
        time.sleep(1)
        if que.qsize()==0:
            que.put(name)
            print("%s生产了..."%(name))

def XiaoFeiZhe(que,gk):
    while True:
        if que.qsize()>0:
            print("%s我消费了：%s"%(gk,que.get()))
            time.sleep(5)

if __name__ == '__main__':
    que = Queue()
    p1 = Process(target=ShengChan,args=(que,'ha',))
    p2 = Process(target=ShengChan, args=(que, 'hd',))
    p3 = Process(target=ShengChan, args=(que, 'nana',))
    p1.start()
    p2.start()
    p3.start()
    g1 = Process(target=XiaoFeiZhe,args=(que,'xf1'))
    g1.start()
    g1.join()
    p1.join()

