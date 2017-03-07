#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
'''
hashlib模块用于加密相关的操作,3.X里代替了md5模块和sha模块,主要提供SHA1,SHA224,SHA256,SHA384,SHA512,MD5算法

MD5 和SHA1 是基于相同原理加密的,但是SHA1比MD5的算法更高级,破解难度更难

import hashlib
m = hashlib.md5()
m.update(b'woaiwode1314')#加密的字符串
bMid = m.digest() #2进制格式
m.hexdigest() #十六进制加密
#这里需要注意的是

如果在加密的时候出现这个错误:
Unicode-objects must be encoded before hashing
则表示需要把字符串转换为byte

import hashlib
hash = hashlib.sha256()
hash.update(b"admin")#转换为byte
print(hash.hexdigest())


hmac模块:
它内部对我们创建key和内容再进行处理然后再加密
import hmac
m = hmac.new('houdong')
m.update(b'admin')
print(m.hexdigest())

import hmac

m = hmac.new(b'key',b'mes')
m.update(b'admin')
print(m.hexdigest())
'''