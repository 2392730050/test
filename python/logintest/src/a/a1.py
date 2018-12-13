# coding=gbk
from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
class login_page():
    #用户名输入框
    login_name=(By.ID,"UserName")
    #密码输入框
    login_pwd=(By.ID,"Password")
    #点击登录
    login_click=(By.ID,"Login")
    login_url="http://user.passport.pisendev.com/OAuth/SignOn?appkey=11092718&display=PC&expires=1544860054404&redirect=http%3a%2f%2fqjwmall.ngrok.pisen.com.cn%2fAccount%2fLoginCallBack&state=http%3a%2f%2fqjwmall.ngrok.pisen.com.cn&which=Account&sign=090129cf60e9f34765dea753e986d57f252823e8b16595a16f9b9dcb0757ae20"
    #登录验证
    login_Verification1=(By.CLASS_NAME,"userName")
    #登录失败
    login_fail=(By.ID,"submitPrompt")
    #用户名为空
    login_numbernull=(By.CLASS_NAME,"errorPrompt")
    #验证码
    login_VerificationCode=(By.ID,"passwordPrompt")
    
    def url(self):
        self.driver=webdriver.Firefox()
        self.driver.get(self.login_url)
    #登陆用户名
    def login_admin(self,value):
        self.driver.find_element(*self.login_name).send_keys(value)
    #登陆密码
    def login_powd(self,value):
        self.driver.find_element(*self.login_pwd).send_keys(value)
    #登陆点击按钮
    def logig_clic(self):
        self.driver.find_element(*self.login_click).click()
    #运行完毕关闭浏览器    
    def quit(self):
        self.driver.quit()
    #验证码 
    def logig_clic1(self):
        self.driver.find_element(*self.login_VerificationCode).click()    
    #验证是否登陆成功
    def __call__(self,value):
        a = self.driver.find_element(*self.login_Verification1).text
        print(a)
        assert a == value
    #登陆失败
    def Login_failure(self,value):
        a = self.driver.find_element(*self.login_fail).text
        print(a)
        assert a == value
    #用户名为空
    def  loginname_null(self,value):
        a = self.driver.find_element(*self.login_numbernull).text
        print(a)
        assert a == value
    #密码为空
    def loginpwd_null(self,value):
        a = self.driver.find_element(*self.login_VerificationCode).text
        print(a)
        assert a == value