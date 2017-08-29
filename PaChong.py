#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''
import urllib2,urllib
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
            hander = urllib2.HTTPCookieProcessor(cookie)
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
  #agent 池
agents = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:17.0; Baiduspider-ads) Gecko/17.0 Firefox/17.0",
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Avant Browser/1.2.789rel1 (http://www.avantbrowser.com)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9b4) Gecko/2008030317 Firefox/3.0b4",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; BIDUBrowser 7.6)",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; Touch; LCJB; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 )",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows 98; Win 9x 4.90)",
    "Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a",
    "Mozilla/2.02E (Win95; U)",
    "Mozilla/3.01Gold (Win95; I)",
    "Mozilla/4.8 [en] (Windows NT 5.1; U)",
    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
    "HTC_Dream Mozilla/5.0 (Linux; U; Android 1.5; en-ca; Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.2; U; de-DE) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/234.40.1 Safari/534.6 TouchPad/1.0",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; htc_bahamas Build/CRB17) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.1-update1; de-de; HTC Desire 1.19.161.5 Build/ERE27) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; de-ch; HTC Hero Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; HTC Legend Build/cupcake) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 1.5; de-de; HTC Magic Build/PLAT-RC33) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1 FirePHP/0.3",
    "Mozilla/5.0 (Linux; U; Android 1.6; en-us; HTC_TATTOO_A3288 Build/DRC79) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.0; en-us; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-us; T-Mobile G1 Build/CRB43) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari 525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.5; en-gb; T-Mobile_G2_Touch Build/CUPCAKE) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Droid Build/FRG22D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Milestone Build/ SHOLS_U2_01.03.1) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.0.1; de-de; Milestone Build/SHOLS_U2_01.14.0) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 0.5; en-us) AppleWebKit/522  (KHTML, like Gecko) Safari/419.3",
    "Mozilla/5.0 (Linux; U; Android 1.1; en-gb; dream) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 2.0; en-us; Droid Build/ESD20) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; Sprint APA9292KT Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-us; ADR6300 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 2.2; en-ca; GT-P1000M Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (Linux; U; Android 3.0.1; fr-fr; A500 Build/HRI66) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
    "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/525.10  (KHTML, like Gecko) Version/3.0.4 Mobile Safari/523.12.2",
    "Mozilla/5.0 (Linux; U; Android 1.6; es-es; SonyEricssonX10i Build/R1FA016) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
    "Mozilla/5.0 (Linux; U; Android 1.6; en-us; SonyEricssonX10i Build/R1AA056) AppleWebKit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
]
        
            
            
    '''
    response = urllib2.urlopen('http://www.so.com')
    print(response.read())



if __name__ == '__main__':
    LoadUrl()




























