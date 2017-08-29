#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
'''

import smtplib
from email.mime.text import MIMEText  #需要安装email  包
From = 'laoshou125hd@163.com'
To = '137590629@qq.com'
subject='This Is First Email...'
userName = 'laoshou125hd@163.com'
userpassword='woaiwode1314.'
#msg=MIMEText('''           你好,这是一封自动发送邮件''') #发送普通文件
msg = MIMEText('''<h1>这个是HTML 页面</h1>''','html','utf-8') #发送html
msg['Subject'] = subject
msg['From'] = From
msg['To'] = To
def SendEmail():
   try:
       smtp = smtplib.SMTP()
       smtp.connect('smtp.163.com')
       smtp.login(userName,userpassword)
       smtp.sendmail(From,To,msg.as_string())
       smtp.quit()
       print('Email Send Success....')
   except Exception as e:
       print('发送失败!失败信息:%s'%(str(e)))

if __name__ == '__main__':
    SendEmail()

