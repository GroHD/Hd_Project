#!/usr/bin/env python
#-*- coding:utf-8 -*-

#定义一个类,继承object
class Person(object):
    #类变量
    num_count =0
    #初始化方法
    def __init__(self,name,age,gender):
        self.name =name
        self.age = age
        self.gender = gender
    #普通方法
    def SayHello(self):
        print("Name Is %s Age Is %d Gender Is %s"%(self.name,self.age,self.gender))
#一个学生类继承Person
class Student(Person):
    def __init__(self,name,age,gender,fenshu):
        #实现父类的初始化方法
        super(Student,self).__init__(name,age,gender)
        self.fenshu = fenshu
    def Print(self):
        print("SayHell %s"%(self.name))

def main():

    p1 = Student('HD',29,'man',22)
    p1.Print()


if __name__ == '__main__':
    main()
    
    
   r''' 
    动态添加字段和方法:
        1.动态添加字段
        例:
            class demo(object):
                def __init__(self):
                    self.name='hd'
                 def func(self):
                    print('func')
                 @staticmetod
                 def funct1(self):
                    print('funct1')
            def test(arg):
                print('test:',arg)
            def test1(arg):
                print('----test-1:',arg)
             
            demo.func2 = test #添加的是动态方法,只有对象才可以调用
            
            a = demo()
            a.func2()
            a.func3 = test1('aassddsas')
            demo.age = 18
            print('demo.age',demo.age)
            a.gender = 'male'
            print('demo.gender',a.gender)
            #当给类添加方法时,添加的是动态方法,只有实例化后才能调用,给对象添加的字段是动态字段,对类添加的字段是静态字段
            
            #slots__的使用
                在新式类中可以使用slots对类添加动态字段做一定的控制
                class demo(object):
                    __slots__ = ('name','age')
                    def __init__(self):
                        self.name = 'hd'
                        
                a = demo()
                a.name = 'hd'
                a.age = 20
                a.gender = 'male' #因为__slots__中没有此方法,所以运行的时候会报错说没有gender该方法
                #但是对类添加静态字段没有限制
                demo.name='hd'
                demo.age=28
                demo.gender ='male'  #对类添加静态字段可以使用
                    
            #父类的初始化
                python实例化子类时,只执行自己的构造函数,其他语言像java,会先执行父类的构造函数,然后执行子类的构造函数,python中需要手动执行父类的构造函数
                class Fa:
                    def __init__(self):
                        print('This Is Fa.__init__')
                class So(Fa):
                    def __ init__(self):
                        Fa.__init__(slef):
                        print(so.__init__)
                  s = So()
                  #也可以使用super执行父类的构造函数,但super是新式类引进的,要使用Super则需要继承object
                  class Fa(object):
                    def __init__(self):
                        print('This Is Fa.__init__')
                  class So(Fa):
                    def __init__(self):
                        super(So,self).__init__()
                        print('So.__init__')
                        
                  s =So()
                  
                  #执行结果
                  This Is Fa.__init__
                  So.__init__
                  
                  #结果：
                        要主动执行父类的构造函数时,对于经典类：
                            使用Fa.__init__(self)执行父类的构造函数
                         对于新式类:
                            使用super(So,self).__init__() 执行父类的构造函数
                    
                    查看父类:__bases__只显示一层继承的所有父类
                    class A:
                        pass
                    class B:
                        pass
                    class CA,B):
                        pass
                    print(C.__bases__)
                    #执行结果:
                        (<class__main__.A as 0x7145c478c125s>,<class __main__.B at 0x71458115a>)
                    #修改代码改为多级继承：
                        class A:
                            pass
                        class B(A)
                            pass
                        class C(B):
                            pass
                        print(c.__bases__)
                     #执行结果:
                        (<class __main__.B at 0x71715c17x0>,)
                        
                  使用__call__方法,对象实例化
                    call是python 中一个有趣的语法,只要定义类型的时候,实现call函数,这个类型就成为可调用的。既我们就可以把这个类的对象当作函数来使用,相当于重载了括号运算符
                    class demo(object):
                        def __init__(self):
                            self.name='hd'
                         def func(self):
                            print('func')
                         def __call__(self):
                            print('This Is Call')
                    a = demo()
                    a()
                    #执行结果
                        This Is Call
                        
                    
