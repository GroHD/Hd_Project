#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''
Name:HD
七牛文件上传
'''
from qiniu import Auth,put_file,etag
import time
#设置AcKey和SeKey
AccessKey = '6nHz6YBV6yhtIgHMO5zkZY6eSMUliagNbmAcYz5A'
SecretKey = 'q_B-04JYgEHt98pJtxBC3kcPLMy1THRC2H7rlwF7'
#设置上传文件
class UpLoad(object):
    def __init__(self):
        #构建对象
        self.q = Auth(access_key=AccessKey,secret_key=SecretKey)
        #设置服务器要上传的目录
        self.bucket_name='project'

    def uploadFile(self,fileName,filePath):
        #生成上传token ,并且制定过期时间
        token = self.q.upload_token(self.bucket_name,fileName,3600)
        #上传文件
        ret,info = put_file(token,fileName,filePath)
        #如果上传失败ret 是none  ret 返回的是key 和hash  key 是返回的服务器保存的文件名,hash是使用 etag(filePath)  判断本地文件的数据
        if None is ret:
            print(info)

def main():
    i = 0
    while True:
        upfile = UpLoad()
        #上传文件,第一个参数是服务器文件名字,第二个参数是要上传那个文件
        upfile.uploadFile(str(i)+'_.jpg','http://p1.so.qhimgs1.com//t01f9f817ede1c02aa1.jpg')
        time.sleep(5)
        print('upload Success......')
        i = i+1
if __name__ == '__main__':
    main()