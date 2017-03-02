#!/usr/bin/env python
#-*-coding:utf-8 -*-
'''
   Name:HD
'''
'''
    断言就是判断某个条件是否正确,如果正确就继续向下走,不正确就抛出AssertError 并且包含错误信息
    书写方法:
        assert 表达式,表达式不满足之后要提示的字符串
'''
a = 1
try:
    assert  a == 2,'这里出错了,有什么问题找我'
    print("断言正确");
except Exception as e:
    print(e)
finally:
    pass