#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD

'''

r'''
    Python threading 模块：
        Python 线程有2种调用方式:
            1.
                直接调用:
                    首先要import threading
                    然后定义一个线程要运行的函数：
                        def sayhi(num):
                            print("running on number:%s" %(num))
                            time.sleep(3) #停止3秒 这个需要引入time模块
                        if __name__ == '__main__'
                            t1 = threading.Thread(target=sayhi,agrs=(1,))  #生成一个线程的实例
                            t2 = threading.Thread(target=sayhi,agrs=(2,))
                            t1.start()#启动线程
                            t2.start()#启动线程


            2.
                继承式调用:
                    import threading
                    import time

                    class MyThread(threading.Thread):
                        def __init__(self,num):
                            threading.Thread.__init__()
                            #也可以按下面的新方法来继承父类的初始化方法
                            #super(MyThread,self).__init__(self)
                            self.num = num

                        def run(self):#每个线程都要运行这个函数
                            print("running on number:%s"%(num))
                            time.sleep(3)

                    if __name__ == "__main__":
                        t1 = MyThread(1)
                        t2 = MyThread(2)
                        t1.start()
                        t2.start()
                在执行多线程的时候可以设置t1.join() 来阻塞线程等待线程结束之后再向下走

'''

#例:

#直接调用
import threading
import time
'''
def SayHi(num):
    print("running Hi %s"%(num))
    time.sleep(3)

if __name__ == '__main__':
    t1 = threading.Thread(target=SayHi,args=(1,))
    t2 = threading.Thread(target=SayHi, args=(1,))
    t1.start()
    t2.start()
    t1.join() #阻塞线程
    t2.join()#阻塞线程

#继承式
lock = threading.Lock() #定义一个锁
class MyThread(threading.Thread):
    def __init__(self,num):
        super(MyThread,self).__init__()
        lock.acquire() #获取一把锁
        self.num = num
        lock.release() #释放锁
    def run(self):
        print('running Thread ..%s'%(self.num))
        time.sleep(3)

if __name__ == '__main__':
'''
'''
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    t_list=[]
    for i in range(10):
        t = MyThread(i) #创建实例对象
        t.start() #启用线程
        #把线程加入列表进行设置线程阻塞
        t_list.append(t)

    #设置所有的线程阻塞
    for i in t_list:
        i.join()
   '''

r'''
    start 启动线程
    join 等待线程结束,这个是阻塞线程
    setDaemon(True Or False)  守护线程,当守护线程退出的时候,其它线程也会结束运行
'''

'''
GIL和多线程锁:
    一个进程下可以启动多个线程,多个线程共享父进程的内存空间,也就是意味着每个线程都可以同时访问一份数据
    GIL:
        GIL就是一个互斥锁,在线程中一次只允许一个线程对变量进行修改。
            GIL并不是Python的特性,而是实现Python解析器是所引入的一个语法标准。
        例:
        lock = threading.Lock() #进行设置一个锁
        class MyThread(threading.Thread):
            def Run():
                lock.acquire()　＃加锁
                    num+=1
                lock.release() # 解锁

'''

r'''
    递归锁和信号量：
        递归锁就是在一把大锁中还包含子锁
    递归锁：
        lock = threading.RLock() #进行设置一个锁
            class MyThread(threading.Thread):
                def Run():
                    lock.acquire()　＃加锁
                        num+=1
                    lock.release() # 解锁
    信号量(Semaphore):
        互斥锁同时允许一个人线程进行更改数据,而Semaphore同时允许一定数量的线程更改数据

    #例:
import threading,time
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("Run the threadL%s\n"%(n))
    semaphore.release()

if __name__ == '__main__':
    num =0
    semaphore = threading.BoundedSemaphore(3) #最多允许3个线程同时运行
    for i  in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()

'''

r'''
线程间同步和交互
     Events是一个线程之间进行数据交换的对象,一般是一个线程判断另外一个线程是否执行完毕
    event  = threading.Event()
    event.wait() #标签如果没设置就一直等待
    event.set()  设置标签
    event.isSet()  判断是否设置标签,如果设置了返回true
    event.clear() 清空设置标签



import threading,time
import random

def light():
    if not event.isSet():
        event.set() #设置标签
    count = 0
    while True:
        if count <10:
            print("绿灯....")
        elif count < 13:
            print("黄灯....")
        elif count < 20:
                if event.isSet():
                    event.clear()
                print("红灯....")

        else:
            count = 0
            event.set()#打开绿灯
        time.sleep(1)
        count+=1

def car(n):
    while True:
        if event.isSet():
            time.sleep(2)
            print("【%s】号车开始同行..."%(n))
        else:
            print("【%s】号车等待红灯...."%(n))
            event.wait()


if __name__ == '__main__':
    event = threading.Event()
    Light = threading.Thread(target=light)
    Light.start()
    for i in range(3):
        t = threading.Thread(target=car,args=(i,))
        t.start()
'''
r'''
    队列(queu):
        在多个线程之间进行数据交换的时候使用队列
        queue.Queue(naxsuze=0) 先进先出
        queue.LifoQueue(maxsize=0) 先进后出
        queue.PriorityQueue(maxsize=0)#存储数据时可设置优先级的队列
    queue方法:
        queue.get()  阻塞的方法
        queue.get_nowait() #非阻塞，如果为空则报 queue.Empty 异常

        queue.put()  阻塞的方法
        queuq.put_nowait() #非阻塞,如果满的话就报queue.Full 异常

        queue.qsize()  拿到queue的长度
        queue.empty()  队列是否为空
        queue.full()  队列是否满了
        queue.put(item.block=True,timeout=None) #放入数据,默认是block的，当queue满的时候put就会进行阻塞,Timeout是阻塞情况下多长时间后就进行报异常
        queue.put_nowait(item)  非阻塞,满了就抛异常

        queue.get(block=True,timeout=None) #取出数据,默认是block的,当queue满的时候get会进行阻塞等待,如果超出timeout时间则报错,默认是一直阻塞中
        queue.get_nowait() #拿出数据
        queue.task_done() # 一个queue通知另外一个queue某个任务已完成。

'''
#例
import queue

#q = queue.Queue(maxsize=3)#定义一个queue,队列的大小是3,先入先出,下面取出的是[1,2,3]
q = queue.LifoQueue(maxsize=3) #先入后出  下面取出的是123
q1 = queue.PriorityQueue(maxsize=3) #自定义队列,数字越小出的越靠前出来
#q.get(timeout=3) #如果不存在抛出 queue Empty 异常
q.put([1,2,3]) #向队列中添加一个数据

q.put(('A','B','C')) #向队列中添加一个数据
data = q.get_nowait()#取出数据
print("先入后出：",data)
q.put('123') #向队列中添加一个数据
q1.put((6,[1,2,3])) #向自定义队列添加数据
q1.put((5,('A','B','C')))
q1.put((3,'123'))
data = q1.get()#取出数据
print("自定义队列：",data)

b = q.full()
print("Full",b) #判断队列是否已满

coun = q.qsize() #拿到队列的长度
print("Count:",coun)