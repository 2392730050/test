# coding=gbk
import unittest
from BeautifulReport import BeautifulReport 
import requests
import time
class request_case(unittest.TestCase):
    def setUp(self):
        self.url="https://www.apiopen.top/createUser?key=00d91e8e0cca2b76f515926a36db68f5&"
        '''�û���ע��'''
        self.admin={'phone':"1778158785","passwd":"123456"}
        '''�û�ע��ɹ�'''
        self.admin1={"phone":"1875587815","passwd":"123654"}
        '''�û��������ֻ�����'''
        self.admin2={'phone':"","passwd":'123456'}
        '''�û�����������'''
        self.admin3={'phone':"18349225555","passwd":''}
    def test_1(self):
        '''�û���ע��'''
        self.r=requests.get(url=self.url,params=self.admin)
        self.request=self.r.json()
        print(self.r.url)
        print(self.r.text)
        if self.r.status_code == 200:
            print("���ӳɹ�")
        else:
            print("����ʧ��")
        try:
            self.assertEqual(self.request['msg'], '�û���ע�ᣡ', 'ʧ��')
        except BaseException as f:
            print(f)
    
    def test_2(self):
        '''�û�ע��ɹ�'''
        self.r1=requests.get(url=self.url, params=self.admin1)
        self.request1=self.r1.json()
        print(self.r1.text)
        print(self.r1.url)
        try:    
            self.assertEqual(self.request1['msg'],'�ɹ�!')
        except BaseException as f:
            print(f)
    
    def test_3(self):
        '''�û��������ֻ�����ע��'''
        self.r2=requests.get(url=self.url, params=self.admin2)
        self.request2=self.r2.json()
        print(self.r2.text)
        print(self.r2.url)
        try:
            self.assertCountEqual(self.request2['msg'],'�����쳣��key,phone,passwd �����Ǳ����')
        except BaseException as f:
            print(f)
    
    def test_4(self):
        '''�û�����������ע��'''
        self.r3=requests.get(url=self.url, params=self.admin3)
        self.request3=self.r3.json()
        print(self.r3.text)
        print(self.r3.url)
        try:
            self.assertEqual(self.request3['msg'],'�����쳣��key,phone,passwd �����Ǳ����')
        except BaseException as f:
            print(f)
    
    def tearDown(self):
        print("close")

if __name__ == "__main__":
    suite = unittest.TestSuite()     
    suite.addTest(request_case('test_1'))
    suite.addTest(request_case('test_2'))
    suite.addTest(request_case('test_3'))
    suite.addTest(request_case('test_4'))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename=now +'ע��ӿڲ��Ա���.html'
    BeautifulReport(suite).report(description="�ӿ�ע�����", filename=filename, log_path="D:\BeautifulReport")
