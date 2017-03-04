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
'''
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
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    '''
    t_list=[]
    for i in range(10):
        t = MyThread(i) #创建实例对象
        t.start() #启用线程
        #把线程加入列表进行设置线程阻塞
        t_list.append(t)

    #设置所有的线程阻塞
    for i in t_list:
        i.join()


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
        递归锁就是在一把大锁中海包含子锁

'''