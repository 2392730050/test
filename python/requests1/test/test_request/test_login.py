# -*- coding: utf-8 -*- 
import unittest
from BeautifulReport import BeautifulReport 
import requests
import time

class test_login(unittest.TestCase):
    def setUp(self):
        self.url='https://www.apiopen.top/login?key=00d91e8e0cca2b76f515926a36db68f5&'
        '''用户登录成功'''
        self.login1={'phone':13594347817,'passwd':123456}
        ''' 用户密码错误 '''
        self.login2={'phone':13594347817,'passwd':1253456}       
        '''用户名不存在'''
        self.login3={'phone':1357817,'passwd':1253456}
        '''用户名为空'''
        self.login4={'phone':"","passwd":"12344456"}
    def test_login1(self):
        '''用户登录成功 '''
        self.r=requests.get(url=self.url,params=self.login1)
        self.request=self.r.json()
        print(self.r.url)
        print(self.r.text)
        try:    
            if self.request['data']['phone'] == 13594347817 and self.request['data']['passwd'] == 123456:
                print("登录成功")
            else:
                print('登录失败')
            self.assertEqual(self.request['msg'],'成功!','登录失败')
        except BaseException as f:
            print (f)
        
    def test_login2(self):
        '''用户输入错误的用户名或密码'''
        self.r1=requests.get(url=self.url,params=self.login2) 
        self.request1=self.r1.json()
        print(self.r1.url)
        print(self.r1.text)
        try:
            self.assertEqual(self.request1['msg'],'用户名或者密码错误！')
        except BaseException as f:
            print(f)
    
    def test_login3(self):
        '''用户输入不存在的用户名'''
        self.r2=requests.get(url=self.url,params=self.login3) 
        self.request2=self.r2.json()
        print(self.r2.url)
        print(self.r2.text)
        try:    
            self.assertEqual(self.request2['msg'],'用户不存在！')
        except BaseException as f:
            print(f)
    def test_login4(self):
        '''用户输入不存在的用户名'''
        self.r3=requests.get(url=self.url,params=self.login4) 
        self.request3=self.r3.json()
        print(self.r3.url)
        print(self.r3.text)
        try:    
            self.assertEqual(self.request3['msg'],'参数异常：key,phone,passwd 参数是必须项！')
        except BaseException as f:
            print(f)
    def tearDown(self):
        print("运行结束关闭用例")
if __name__ == "__main__":
    unittest.main()