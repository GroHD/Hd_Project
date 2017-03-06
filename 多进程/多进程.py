#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
r'''
    多进程multiprocessing
    #例:

from multiprocessing import Process
import time,os

def f(name):
    time.sleep(2)
    print("hello",name)
    print("module Name:",__name__) #拿到程序名称
    print("parent Process:",os.getppid())#拿到父id
    print("parent Id:", os.getpid())#拿到当前进程的id

if __name__ == '__main__':
    p1 = Process(target=f,args=('bob',))
    p2 = Process(target=f, args=('bob',))
    p1.start()
    p2.start()
'''
'''
    进程间通讯
        不同进程间内存是不共享的,要想实现两个进程间的数据交换,可以使用下面的方法:
    Queues
        使用方法和threding里的queue差不多
        引入queue
        from multiprocessing import Process,Queue

#队列例子
from multiprocessing import Process,Queue

def f(q,name):
   q.put([42,None,name]) #把子进程数据存入q

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=f,args=(q,'hd'))

    p2 = Process(target=f, args=(q,'nana')) #向子进程中放入nana  数组
    p1.start()
    p2.start()
    print(q.get()) #父进程中取出q中的数据
    print(q.get())  #拿出队列中的数
    p1.join()
    p2.join()

'''
r'''
    管道(Pipe())：
        它会返回一对对象,是双向取值


from multiprocessing import  Process,Pipe

def f(conn,name):
    conn.send([42,None,name])
    conn.close()

if __name__ == '__main__':
    parent_conn,child_conn = Pipe() #定义管道
    p = Process(target=f,args=(child_conn,'hd')) #把管道传入子进程
    p.start()
    print(parent_conn.recv())#从父进程中取出管道
    p.join()

'''

'''
    进程间的数据传递:
        进程间的数据可以同时被多个人修改,修改的时候可以使用Manager 进行修改，
        Manage支持List dict,Namespace,Lock,RLoce,Semaphore,BoundedSeamaphore,Condition,Event等等
        平时最长用的就是List和dict 这两个
    from multiprocess.ing import Process,Manage


#例:
from multiprocessing import  Process,Manager

def f(d,l):
    d[1] ='1'
    d[2] = 2
    d[0.25] = None;
    l.append(1)
    print(l)

if __name__ == '__main__':
    with Manager() as manage: #自动关闭数据共享
        d = manage.dict() #创建字典
        l = manage.list(range(5))#创建列表
        p_list=[]
        for i  in range(10):#循环创建10个进程
            p = Process(target=f,args=(d,l))
            p.start()
            p_list.append(p)
        for i in p_list:
            i.join()

        print(d)
'''
'''
进程同步:
    因为每个进程都不是同步的,所以需要同步每个进程,可以使用Lock进行同步


#例:
from multiprocessing import Process,Lock
import time


def f(i,l):
    l.acquire() #枷锁
    time.sleep(1)
    print("I===",i)
    l.release() #解锁
if __name__ == '__main__':
    l = Lock()
    p_list=[]
    for i in range(100):
        p = Process(target=f,args=(i,l,))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()
'''
'''
    进程池:
        进程池内部维护一个进程序列,当使用时,则去进池中获取一个进程,如果进程池中没有可用的进程,那么进程就会等待,直到进程池中有可用进程为止

    进程池中有两个方法:
        1.apply
        2.apply_async
'''
#例:
from multiprocessing import Process,Pool
import time

def Foo(i):
    time.sleep(2)
    return i+100 #把执行结果返回

def Bar(arg):
    print('---->exec done:',arg)#回调方法,执行调用的方法返回的参数

if __name__ == '__main__':
    pool = Pool(5)#线程池中最多有5个线程
    for i in range(10):
        pool.apply_async(func=Foo,args=(i,),callback=Bar)#第一个参数是执行那个方法,第二个是执行方法里的参数,第三个是回调方法
        #pool.apply(func=Foo,args=(i,)) 同步的时候无法使用回调参数
    print('end')
    pool.close()
    pool.join()#进程池中进程执行完毕后再关闭,如果不写该函数,那么程序就直接关闭
