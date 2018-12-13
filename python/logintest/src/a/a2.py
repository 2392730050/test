#coding=utf-8
import unittest
import a1
from time import sleep
import time
from BeautifulReport import BeautifulReport
class test_login(unittest.TestCase):
    def setUp(self):
        self.p1=a1.login_page()
        self.p1.url()
        #登陆成功的参数
        self.login_name="18349225505"
        self.login_pwd="cyf123456."
        self.isval="测试test"
        #登陆失败的参数
        self.login_name1="18349225501"
        self.login_pwd1="cyf123456."
        #用户名为空
        self.login_name2=""
        self.login_pwd2="cyf123456."
        #密码为空
        self.login_name3="18349225505"
        self.login_pwd3=""
    #@unittest.skip('跳过此用例')
    
    def test_1(self):
        '''登陆成功'''
        print(1)
        self.p1.login_admin(self.login_name)
        self.p1.login_powd(self.login_pwd)
        sleep(10)
        self.p1.logig_clic()
        sleep(10)
        self.p1.__call__(self.isval)    
    
    def test_2(self):
        '''登陆失败'''
        print(2)
        self.p1.login_admin(self.login_name1)
        self.p1.login_powd(self.login_pwd1)
        sleep(10)
        self.p1.logig_clic()
        sleep(2)
        self.p1.Login_failure("登录失败,账号或密码错误!")
    
    def test_3(self):
        '''用户名为空'''
        print(3)
        self.p1.login_admin(self.login_name2)
        sleep(2)
        self.p1.login_powd(self.login_pwd2)
        self.p1.loginname_null("请输入正确的手机号码!")
    def test_4(self):
        '''密码为空'''
        print(3)
        self.p1.login_admin(self.login_name3)
        sleep(2)
        self.p1.logig_clic()
        sleep(3)
        self.p1.loginpwd_null("请输入密码")
    def tearDown(self):
        self.p1.quit()
        print("运行结束")
if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(test_login("test_1"))
    suite.addTest(test_login("test_2"))
    suite.addTest(test_login("test_3"))
    suite.addTest(test_login("test_4"))
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename=now +'测试报告.html'
    BeautifulReport(suite).report(description="登陆成功测试", filename=filename, log_path="D:\BeautifulReport")
