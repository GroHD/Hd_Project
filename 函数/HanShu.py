#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
函数:
HD:2017年3月28日15:57:19
'''
r'''
    函数就是将一些语句集合在一起的部件,它们能够不止一次地在程序中运行,函数还能够计算出一个返回值,并能够改变作为函数输入的参数，而这些参数在代码运行时也许每次都不同。
    函数就是在编程过程中复制粘贴的代替，

'''

r'''
    编写内置函数:
        def  语句:
            def 语句将创建一个函数对象并将其赋值给一个变量名。
            def 语句格式如下:
                def <funcationName>(arg1,arg2,...argN):
                    <代码块>
                
                就像所有的多行python语句一样,def包含了首行并有一个代码块跟随在后边,这个代码块通常都会缩进或者冒号后边简单的一句。而这个代码块就成为了函数的主体，也就是每当调用函数时python所执行的语句。
                
                def 首行定义了函数名,赋值给了函数对象，并在括号中包含了0个或以上的参数(也有时候称为形参)。在函数调用的时候，在首行的参数名赋值给了括号中传递来的对象。
                
                函数主体往往包含了一条return 语句：
                    def <functionName>(arg1,agr2,...argN):
                        ......
                        return <value>
                        
                    Python 的return 语句可以在函数主体中的任何地方出现。它表示函数调用的结束，并将结果返回至函数调用处。return 语句是可选的，如果没有return 语句,那么函数将会在控制流程执行完函数主体时结束。一个没有返回值的函数自动返回了none对象
                    
                
                def 语句是实时执行的：
                    python的def语句实际上是一个可执行的语句:
                        当它运行的时候,它创建一个新的函数对象并将其赋值给一个变量名。
                        其次因为它是一个语句,一个def可以出现在任一句可以出现的地方，甚至嵌套在其他的语句中。
                        函数还可以通过嵌套在if语句中去实现不同的函数定义,这样也是合法的：
                            if test:
                                def func():
                                    ....
                            else:
                                def func():
                                    ...
                            func() #调用方法
                            
                      在程序运行时简单地给一个变量进行复制。python函数在程序运行之前并不需要全部定义。def 在运行时在进行评估，而在def之中的代码在函数调用之后才会评估。
                      因为函数定义是实时发生的,所以对于函数名来说并没什么特别之处，关键之处在于函数名所引用的那个对象:
                      例:
                        othername = func
                        othername()
                        
                        在这里函数赋值给一个不同的变量名,并通过新的变量名进行了调用。在python中函数仅仅是对象，在程序执行时他清楚的记录在内内存之中。
                    
        
            
    
'''
r'''
函数返回多个参数:
    def Return():
    return 1,2,3


a1,a2,a3 = Return()

print(a1,a2,a3)

如果返回多个参数的话,计算结果都不一样,那么就需要放入一个集合中,然后返回这个集合
def count():
    fs = []
    for i in range(1, 4):
        tem = i*i
        fs.append(tem)
    return fs

f1, f2, f3 = count()
print f1(), f2(), f3()

'''

r'''
    函数式:
        Python支持的函数式编程：
            1.不是纯函数式编程:允许有变量
            2.支持高阶函数:函数也可以作为变量传入
            3.支持闭包:有了闭包就能返回函数
            4.有限度的支持匿名函数
            
    变量可以只想函数
        >>f = abs
        >>f(-20)
        >>20 
        
    函数名其实就是指向函数的变量
    
    高阶函数:
            能接受函数做参数的函数
            
            变量可以指向函数
            函数的参数可以接受变量
            一个函数可以接收另一个函数作为参数
            能接受函数作参数的函数就是高阶函数
            
        例:
            接受abs函数
                定义一个函数，接收x,y,f三个参数
                其中x,y是数值,f是函数
                def  fun(x,y,f):
                    return f(x)+f(y)
            调用:
                fun(-5,9,abs) #abs是一个函数
                
    python中闭包:
        在函数内部定义的函数和外部定义的函数是一样的,只是它们无法被外部访问:
            def g(lst):
                print("g()....")
                def f():
                    print("f()..")
                    return sum(lst)
                    
                return f
                
        上面将f函数定义到g函数内部,可以放弃其它代码调用f函数,上面f函数内部应用来外层函数的变量，然后返回内层函数的情况较闭包,
        闭包的特点就是返回的函数还引用了外层函数的局部变量,所以,要正确使用闭包，就要确保应用的局部变量在函数返回后不能变
        
'''

r'''
匿名函数:
    高阶函数可以接受函数做参数,有些时候,我们不需要显示地滴定函数,直接传入匿名函数更方便,
    关键字 lambda表示匿名函数:
        书写格式:
            fu = lambda x:x*x
            
            冒号前边的x表示函数参数,冒号后边的x表示执行的过程
            
    匿名函数有个限制,就是只能有一个表达式,不能写return 返回这就是表达式的结果。
    使用匿名函数，可以不必定义函数名,直接创建一个函数对象,很多时候可以简化代码
    例:
        li = [x  for x in range(1,11)]
        fn = map(lambda x :x * x,li)
        for ite in fn:
            print(ite)
    在返回函数的时候,也可以返回匿名函数:
        myabs = lambda x : -x if x < 0 else x
        
item = filter(lambda x : True if x and len(x.strip())>0 else False, ['test', None, '', 'str', '  ', 'END'])

for ite in item:
    print(ite)
'''

