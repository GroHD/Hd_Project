#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
r'''
    Python 的语句:

        语句          角色                  例子

        赋值          创建引用值            a,b,c = 'good','bad','ugly'

        调用          执行函数              log.write('spam,ham')

        打印调用       打印对象              print('这是打印数据','hd')

        if/elif/else  选择动作            if 'spam' in text:
                                            print(text)

        for/else      序列迭代            for x in mylist:
                                            print(x)

        while/else    一般循环            while x > y:
                                            print("Hello")

        pass           空占位符           while True:
                                            pass

        break          循环退出           while True:
                                            if exittest():break

        continue       循环继续           while True
                                            if skiptest(): continue
        def            函数和方法         def  f(a,b,c=1,*d)
                                            print(a+b+c+d[0])
        return         函数结果           def  f(a,b,c=1,*d):
                                            return a+b+c+d[0]
        yield          生成器函数         def gen(n):
                                            for i in n:yield i*2

        global         命名空间           x = 'old'
                                        def function():
                                            global x,y; x = 'new'
        nonlocal       Namespaces(3.0+) def outer():
                        命名空间(Py3.0以上)   x = 'old'
                                            def function:
                                                    nonlocal x;x = 'new'

        import        模块访问             import  sys

        from          属性访问             from sys import stdin

        class         创建对象             class Subclass(Superclass):
                                                staticData=[]
                                                def method(self):pass

        try/except/finally   捕获异常       try:
                                                cation()
                                           except:
                                                print('action error')

        raise        触发异常               raise EndSearch(location)

        assert       调试检查               assert x>y,"X too small"

        with/as      环境管理器              with open('data') as myfile:
                                                print(myfile)

        del          删除引用                del data[k]
                                            del data[i:j]
                                            del obj.attr
                                            del variable


    在检查一个内容是否是int类型时，可以使用isdigit方法检查字符的内容
    s ='123'
    X = 'XXX'
    s.isdigit()
    X.isdigit()
    (True,False)

Try 语句处理错误:
    在Python中,处理错误最通用的方式就是使用try语句，用它来补货并完全复原错误信息。
    try:
        XXXXX
    except:
        XXXX
    else:
        xxxx

    这个try 语句的组成是：try 关键字后面跟代码主要代码块（XXXXX），在跟except 部分，给异常处理代码（XXXX），再接else 部分，如果try部分没有引发异常
    就执行这一部分代码,ptyhon 会先执行tyr 部分, 如果有异常就运行except部分或没有异常执行else部分
'''

r'''
赋值语句形式：
    spam = 'Spam' 基本形式
    spam,ham = 'yum','YUM'  元祖赋值运算(位置性)
    [spam,ham] = ['yum','YUM'] 列表赋值运算(位置性)
    a,b,c,d = 'spam'  序列赋值运算,通用性
    a,*b = 'spam' 扩展的序列解包   一种新的序列赋值允许我们更灵活地选择要赋值的一个序列部分, 等号右边的s赋值给等号左边的a，b赋值给pam 这为手动分辨操作的结果的赋值提供了一种简单的替代方法
    spam = ham = 'lunvh' 多重目标赋值运算   变量名spam和ham两者都赋值成相同的字符串对象'lunch'的引用，效果和写成ham ='lunch' 然后在写spam =ham。
    spams += 42  增强赋值运算(相当于spams = spams+42)

    注意虽然可以在等号两侧混合相匹配的序列类型，右边元素的数目还是要跟左变变量的数目相同，不然会产生错误。
    a,b,c,d = 'abcd'#正确
    a,b,c,f = 'abc' #错误,等号两遍就的数量不同

    要是想通用的话，就需要使用分片了，这里有几种方式使用分片运算，可以使最后的情况正常工作。

    a,b,c = sting[0],sting[1],sting{2:]

'''

r'''
    通常一个函数的返回值是None,在函数不返回人何有意义内容的函数默认返回的就是None
'''
r'''
    调用格式：
        从语法上讲,调用3.0的print函数有如下的形式
        print([object,.....][,sep=' '][,end='\n'][file=sys.stdout])
        在上面的函数中,方括号中的选项是可选的,并且可能会在一个给定的调用中省略，并且=后面的值都给出了参数的默认值。这个内置的函数把字符串sep所分开的一个或多个对象的文本表示，后面跟着的字符串end,都打印到流file中
        sep,end 和file 部分如果给出的话，必须作为参数的关键字参数给定，也就是说必须使用一种特殊的"name=value"的语法来传递参数。

        sep:
            是在每一个对象的文本之间插入的一个字符串，如果没有传递的话,他默认地市一个单个的空格，传递一个空格它会抑制分隔符
            print(a,b,c,d,sep='end') #打印a,b,c,d 的时候每个输出的变量之间都用end 进行分割

        end:
            是添加在打印文本末尾的一个字符串,如果没有传递它默认是一个\n换行符。
        file:
            file指定了文本将要发送到的文件,标准流或者其它类似文件的地方，如果没有传递它默认的是sys.stdout，带有类似文件的write(string)方法的任何对象都可以进行传递，但真正的文件应该为了输出而打开
            print(x,y,z,sep='...',file==open('data.text','w')) #把打印输出到文本
'''

#打印 99 乘法表
def main():
    for  i in range(1,10):
        for j in range(1,(i+1)):
            print("%d * %d = %d\t"%(j,i,(i*j)),end='') # end  默认的是换行，现在设置成'' 不进行换行
        print('')

    return None

if __name__ == '__main__':
    main()

r'''
    python2.6和python 3.0 print语句的区别：
        python2.6           python3.0           说明

        print x,y           print(x,y)          默认

        print x,y,          print(x,y,end='')   不在文本末尾添加'\n'

        print >> afile,x,y  print(x,y,file=afile)   把文本发送搭配myfile.write 而不是sys.stdout.write
'''


r'''
    其实print 语句只是python 的人性化的特性，提供sys.stdout 对象简单的接口，在加上默认的格式设置，实际上，如果想写的复杂一些，也可以直接使用sys模块输出
    import sys

    sys.stdout.write('Hello Word!\n')
'''
r'''
if/else 三元表达式
  if x:
    a = y
  else:
    a = z

可以携程
a = y if x else z
这个表达式和上面四行if语句的结果相同,但是更容易编写代码。当x为真的时候python会执行 表达式y，而当x为假的时候才会执行表达式z


'''

r'''
 while和for 语句：
    while是一个通用循环的一种方法，而for是用它来遍历序列对象内的元素，并对每个元素运行一个代码块
    while语句最完整的书写格式是：
                首行以及测试表达式，有一列或多列缩进语句的主题以及一个可选的else部分(控制权里快循环而又没碰到break语句时会执行)，python会一直计算winle开头的测试，然后执行循环主题内的语句，知道测试返回假为止

        while <test>: 表达式
            <statements1> 循环体语句
        else: 可选else 语句，如果在循环体语句里没有碰到break 语句则执行这个语句
            <<statements2> 执行代码语句

    break,coninue pass 和循环else

        break:
            跳出最近所在的循环(跳过整个循环语句)
        continue:
            跳到最近所在循环的开头(到循环的表达式行)
        pass:
            什么事也不做，只是空占位符
        循环else块：
            只有当循环正常离开的时候才会执行（也就是说没有碰到break语句）

    一般循环格式：
        加入break和continue语句后，while 循环的一般格式如下：
            while<test1>:
                <statements1>
                if <test2>:break
                if <test3>:continue
            else:
                <statementd2>
        break和continue 可以出现在while（或for）循环主体的任何地方，但通常会进一步嵌套在if语句中，根据某些条件来采取对应的操作

    pass语句是无运算的占位语句，当语法需要语句并且还没有任何实用的语句可写时，就可以使用它。它通常用于为复合语句编写一个空的主体，例如想写个无限循环，每次迭代的时候什么也不做， 就写个pass
        while True:pass

        python3.0中可以使用...（三个连续的点号）来省略代码。由于省略号自身什么也不做，这可以当作pass 语句的一种替代方案
    continue 语句会立刻跳到循环的顶端。

    循环else:
        和循环else子语句结合时，只有使用break语句跳出当前循环的时候才会执行循环else语句
'''