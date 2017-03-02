#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD

'''
a = 'a'
#print(isinstance(a,str)) #判断a 是否是某str类的实例
#print(issubclass(a,str)) #判断a 是不是str的派生类类,  但是a必须是类才可以

r'''
在编程的过程中,为了增加友好性,在程序出现bug时一般不会将错误信息显示给用户,而是实现一个提示的页面,通俗来说就是不让用户看见大黄页
    语法：
        try:
            正常代码
        except Exception:
            出错页面
        finally:
            运行完上面的代码之后运行这个代码

    语法错误是无法被被错误获取到的,因为语法错误是在程序运行之前就出错了！
'''

try:
    a = 1+2
except ValueError as ne:
    print('数字错误！')
except IndexError as ine:
    print('索引错误！')
except Exception as e :
    print(e)
finally:
    print('最后运行')


'''
    自定义异常:
        自定义一个类,然后继承Exception
            需要初始化传入错误消息
            出异常的时候需要通过__str__把消息返回

'''

#例:
class MyException(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message


try:
    raise  MyException('This Is Error.....')
except MyException as e:
    print("Project Error,Error Message:",e)
