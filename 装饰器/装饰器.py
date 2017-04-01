#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
r'''
装饰器:
    装饰器就是不修改原来方法的情况下给方法增加功能
    
    可以通过 高阶函数来增加

'''
#例:


def new_Function(fun):
    def Change(x):
        print("call",fun.__name__,"()")
        return fun(x)
    return Change

def sum(x):
    return x*x



fun = new_Function(sum)
print(fun(2))
r'''
    上面就是使用高阶函数来完成的,
    new_Function 函数是装饰器函数
'''

r'''
装饰器:
    Python内置的@语法就是为了简化装饰器调用,装饰器必须有一个函数,这个函数就是用来让方法回掉并且传入自己的
'''

#例
def new_fun(fun,*args,**kwargs):
    print("call",fun.__name__,"()")

@new_fun
def f1(x):
    return x*2
r'''
为了使装饰器的参数可变,在写装饰器的时候参数可以写成动态类型的,这样就可以传入不定量的参数了
'''
r'''
带参数的装饰器:
    有的装饰希望打印日志的时候可以根据参数来打印出不同的级别日志,那么就需要log日本本身传入对应的参数
    类似于:
        @log('DEBUG')
        def my_func():
            pass
    把上面的定义范承毅高阶函数的调用就是
    
    log_decorator = log('DEBUG')
    my_func = log_decorator(my_func)
    
    上面的语句又相当于:
        log_decorator = log('DEBUG')
        @log_decorator
        def my_func():
            pass
    
    所以,带参数的log函数首先返回一个decorator函数,再让这个装饰器函数接收my_func并返回新函数
    
    def log(prefix):
        def log_decorator(func):
            def warpper(*args,**kwargs):
                print("[%s]%s...."%(prefix,func.__name__))
                return func(*args,**kwargs)
            return warpper
        return log_decorator
        
    @log('DEBUG')
    def test():
        pass
        
    print(test())
    
    #执行结果
        [DEBUG] test()...
        None   
             
    可对于三层嵌套的decorator定义,可以先把它拆分开
    
    #标准decorator
    def log_decorator(func):
        def warpper(*args,**kwargs):
             print("[%s]%s...."%(prefix,func.__name__))
            return func(*args,**kwargs)
        return warpper
        
    #返回decorator:
        def log(prefix):
            return log_decorator(f)
    
    拆开以后会发现调用失败,因为日,在三层嵌套的decorator定义中,最内层的warpper引用了最外层的参数prefix,所以把一个闭包拆成普通的函数调用会比较困难。
    
    
'''


def  log(txt):
    def log_decorator(func):
        def warpper(*args,**kwargs):
            print("[%s]%s..."%(txt,func.__name__))
            return func(*args,**kwargs)
        return warpper
    return log_decorator
@log("DEBUG")
def Login(n):
    print(n)
    return

if __name__ == '__main__':
   print(Login(1))
r'''
 @decorator 可以动态实现函数功能的增加,但是经过@decorator 改造过后的函数和原函数相比,除了功能多一点意外,还有一个不一样的地方就是打印函数名的时候会发现函数名已不是函数自己的名字,而是@decorator 内部定义的wrapper
 例:
'''
def  log(txt):
    def log_decorator(func):
        def warpper(*args,**kwargs):
            print("[%s]%s..."%(txt,func.__name__))
            return func(*args,**kwargs)
        return warpper
    return log_decorator
@log("DEBUG")
def Login(n):
    print(n)
    return

#if __name__ == '__main__':
#    print("Login Function Name Is :",Login.__name__)
    #打印的是warpper
r'''
可见,由decorator返回的新函数函数名已经不是Login,而是由@log内部定义的wrapper。这对于那些依赖函数名的代码就会消失效。
decorator 还会改变函数的__doc)__等其他属性。
如果要让调用者看不出一个函数经过了@decorator的"改造"，就需要把原函数的一些属性赋值到新函数中:

'''
#例:
def Writer(txt):
    def war_decorator(func):

        def warpper(*agrs,**kwargs):
            print(txt)
            return func(*agrs,**kwargs)

        warpper.__name__ = func.__name__
        warpper.__doc__ = func.__doc__
        return warpper
    return war_decorator
@Writer('Hell')
def Hello(n):
    print(n)
print("hello Name Is :",Hello.__name__)

