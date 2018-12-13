# coding=gbk
import pytest 
import smtplib
import time
from selenium import webdriver

#     
# @pytest.fixture()
# def login():
#     driver=webdriver.Firefox()
#     driver.get("https://www.baidu.com/")
#     print("登录")
#     yield 
#     print("执行完毕")
#     driver.quit()
# class Test_Three():   
#     def setup_class(self):
#         print("打开浏览器")
#     def test_one(self,login):
#         print(1)
#     def test_three(self):
#         assert 3==3
#     def test_two(self,login):
#         print(2)
#     def teardown_class(self):
#         print("关闭浏览器")
# if __name__=="__main__":
#     pytest.main(["-x","-s","Test_Three.py"])  

# @pytest.fixture(scope="function",autouse=True)
# def start():
#     print("开始执行function")
#     print("xxxxx")
#     yield
#     print("结束测试")
# 
# class Test_a():
#     @pytest.mark.usefixures("start")
#     def test_01(self):
#         print("用例1")
#     def test_02(self):
#         print("用例2")
# if __name__=="__main__":
#     pytest.main(["-x","-s","Test_Three.py"]) 

#参数化parametrize
# @pytest.mark.parametrize("test_input,expected",
#                          [("3+5",8),
#                           ("2+4",6),
#                           ("6*0",0),
#                           #标记为失败的用例就不运行了，直接跳过显示xfaild 内置函数mark.xfail
#                           pytest.param('6*0',1,marks=pytest.mark.xfail)
#                           ])
# 
# def test_eval(test_input,expected):
#     assert eval(test_input)==expected
# if __name__=="__main__":
#     pytest.main(["-x","-s","Test_Three.py"])  

# @pytest.mark.parametrize("x",[0,1]) 
# @pytest.mark.parametrize("y",[0,1])
# 
# def test_01(x,y):
#     print(x,y)
#     print(x==y)
# if __name__=="__main__":
#     pytest.main(["-x","-s","Test_Three.py"])   

# 
# def f():
#     return 3
# def test_one():
#     a = f()
#     print(a)
#     assert a%3==0 ,"判断a是否是偶数当前a的值是：%s"%a#错误是弹出提示
# if __name__=="__main__":
#     pytest.main(["-x","-s","Test_Three.py"])   

# def test_zero_division():
#     with pytest.raises(ZeroDivisionError) as f :
#         1/1
#     assert f.Type==ZeroDivisionError
#     assert "division by zero" in str(f.Value)
# a = [1,2,3,4] 
# b = 1
# def test_a():
#         assert 1 in a 
# def test_b():        
#         assert 2 in a
# # @pytest.mark.skipif( b == 1)  
# # def test_c():
# #         assert 3 in a   
# @pytest.mark.webtest          
# def test_c():
#     assert 3 in a   
# if __name__=="__main__":
#     pytest.main(["-x","-s","Test_Three.py","-m=webtest"])         
         
# 
# class Test_calss():
#     def test_1(self):
#         assert 1==1
#     @pytest.mark.skip()
#     def test_2(self):
#         assert 2==3
#     def test_3(self):
#         assert 3==3
# if __name__=="__main__":
#     pytest.main(["-v","-k","not test_1 or test_2"])           
        
# canshu=[{"user":"admin","psw":"111111"}] 
# @pytest.fixture(scope="moudle")
# def login(request):
#     user=request.param["user"]
#     pwd=request.param['psw']
#     print("正在操作登录：账号:%s,，密码:%s"%(user,pwd))
#     if pwd:
#         return True
#     else:
#         return False
# @pytest.mark.parmetrize("login",canshu,indirect=True) 
# class Test_xx():
#     def test_01(self,login):
#         '''用例1登录'''
#         result = login
#         print("用例1：%s"%result)
#         assert result ==True
#     def test_02(self,login):
#         result=login 
#         print("用例3，登录结果：%" % result)
#         if not result:
#             pytest.xfail("登录不成功")
#         assert 1==1
#     def test_03(self,login):
#         result = login
#         print("用例3 登录结果：%" %result)
#         if not result:
#             pytest.xfail("登录不成功 标记为xfail")
# if __name__=="__main__":
#     pytest.main(["-s","Test_Three.py"])           
#         

# test_login_data=[("admin","11111"),("admin","")]
# def login(user,psw):
#     '''普通登录函数'''
#     print("登录账户：%s"%user) 
#     print("登录密码:%s"%psw)
#     if psw:
#         return True
#     else:
#         return False   
# @pytest.mark.parametrize("user","psw",test_login_data)
# def test_login(user,psw):
#     '''登录用例'''
#     result=login(user, psw)
#     assert result==True,'失败原因密码为空'    
# if __name__=="__main__":
#     pytest.main(["-s","Test_Three.py"])  