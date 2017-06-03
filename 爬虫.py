#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
import urllib2,urllib.request,urllib.cooklielib
import cookielib  #Cookie使用
def LoadUrl():
    #urlopen 接受三个参数 urlopen(url,data,timeout)
    r'''
            第一个参数:
                url既为URL
            第二个参数:
                data是访问URL时要传送的数据
            第三个参数:
                timeout 是设置超时时间
            第二三个参数可以不写的,第一个参数是必须写的
            在这个例子中写了www.so.com URL,执行urlopen方法之后,返回一个response对象,返回信息便保存在这里面
            response 对象有一个read方法,可以返回获取到的页面内容
            
        构造Request
            request = urllib2.Request('http://www.so.com')
            response = urllib2.urlopen(request)
            print(response.read())
        #POST和GET传送数据:
            POST:
                values = {'userName':'1105061266@qq.com','password':'xxxxxxxx'}
                data = urllib.urlencode((values)
                url ='http://www.so.com'
                request = urllib2.Request(url,data)
                response = urllib2.urlopen(request)
                print(response.read())
            GET:
                values ={}
                values['userName'] = '1105061266@qq.com'
                values['password'] = 'xxxxxxxxxx'
                data = urllib.urlencode(values)
                geturl = url+'?'+data
                request = urllib2.Request(geturl)
                response = urllib2.urlopen(request)
                print(response.read())
        设置Headers
            url='http://www.so.com/login'
            user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
            values = {'username':'cqc','password':'xxxxxxxx'}
            headers = {'User-Agent':user_agent} #这里可以加入其它请求头信息
            data = urllib.urlencode(values)
            request = urllib2.Request(url,data,headers)
            response = urllib2.urlopen(request)
            page = response.read()
    
        Proxy(代理)的设置
            urllib2默认会使用环境变量http_proxy来设置HTTP Proxy。某些可以设置一些代理服务器来帮助你完成工作,每隔一段时间换一个代理。
            下面一段代码说明了代理的设置用法:
                enable_proxy = True
                proxy_handler = urllib2.ProxyHandler({'http':'http://some-proxy.com:8080'})
                null_proxy_handler = urllib2.ProxyHandler({})
                if enable_proxy:
                    opener = urllib2.build_opener(proxy_handler)
                else:
                    opener = urllib2.build_opener(null_proxy_hander)
                urllib2.install_opener(opener)
                
    URLError异常处理:
        try:
        except urllib2.URLError as e:
            print(e.code) #打印状态码
            print(e.reason)
            
    Cookie的使用:
        
        获取Cookie保存到变量里:
            首先,利用CookieJar对象实现获取cookie的功能,存储到变量中
            #声明一个CookieJar对象实例来保存cookie
            cookie = cookielib.CookieJar()
            #利用urllib2库的HTTPCookierocessor对象来创建cookie处理器
            hander = urllib.HTTPCookieProcessor(cookie)
            #通过hander来构建opener
            opener = urllib2.build_opener(handler)
            #此处的open方法同urllib2的urlopen方法,也可以传入request
            response = opener.open('http://www.so.com')
            for item in cookie:
                print('%s=%s'%(item.name,item.value))
        #保存cookie到文件
            在上面的方法中,我们将cookie保存到了cookie这个变量中,如果将cookie保存到文件中我们要用到FileCookieJar这个对象
            #设置保存cookie的文件,同级目录下的cookie.txt
            filename='cookie.txt'
            #声明一个MozillaCookieJar对象实例来保存cookie 之后写文件
            cookie = cookielib.MozillaCookueJar(filename)
            #利用urllib2库的HTTPCookieProeccsion对象来创建cookie处理器
            handler = urllib2.HTTPCookieProcessor(cookie)
            #通过handler来构建opener
            opener = urllib2.build_opener(handler)
            #创建一个请求,原理同urllib2的urlopen
            response = opener.open('http://www.so.com')
            cookie.save(ignore_discard=True,ignore_expires=True)
        #从文件中获取Cookie并访问
            把文件保存到Cookie中,可以使用下面的方法来读取cookie并访问网站
                #创建实例
                cookie = cookielib.MozillaCookieJar()
                #从文件中读取cookie的内容到变量
                cookie.load('cookie.txt',ignore_discard=True,ignore_expires=True)
                #创建请求的request
                request = urllib2.Request('http://www.so.com')
                #利用urllib2的buld_opener方法创建一个opener
                opener = urllib2.build_opener(urllib2.HttpCookieProcessor(cookie))
                response = opener.open(req)
                print(response.read())
        例子利用cookie模拟登陆网站:
            import urllib
            import urllib2
            import cooklielib
            
            filename='cookie.txt'
            cookie = cookielib.MozillaCookieJar(filename)
            opener =urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
            postdata = urllib.urlencode({'username':'1105061266@qq.com','password':'1234567'})
            #登陆教务系统url
            logurl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bks_login2.login'
            #模拟登陆,并把cookie保存到变量
            response = opener.open(loginUrl,postdata)
            #保存cookie到cookie.txt文件中
            cookie.save(ignore_discard=True,ignore_expires=True)
            #利用cookie请求另外一个网址,并携带该cookie
            gradeUrl=''http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
            #请求访问成绩查询网址
            result = opener.open(gradeUrl)
            print(result.read())
    正则表达式：
        
            
            
    '''
    response = urllib2.urlopen('http://www.so.com')
    print(response.read())



if __name__ == '__main__':
    LoadUrl()

