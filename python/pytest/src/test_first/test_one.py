# coding=gbk
#content of test_class.py
# def funx(x):
#     return x+1
# def test_answer():
#     assert funx(4)==5
# class Testclass:
#     def test_one(self):
#         x="this"
#         assert "h" in x
#     def test_two(self):
#         x1="admin"
#         x2="ju"
#         assert x1 in x2 
#         print("运行结束")
#     def test_Three(self):
#         x3="admin"
#         assert x3=="adin"
#     def test_four(self):
#         assert 3 == 3

import pytest

# class Testclass:
#     def setup_module(self):
#         print("setup_module:整个用例只运行一次")
#     def teardown_module(self):
#         print("setup_module:整个用例只运行一次")
#     def setup_function(self):
#         print("开头")    
#     def teardown_function(self):
#         print("运行结束")
#     def setup_class(self):
#         print("用例开始")
#     def test_one(self):
#         print("运行中")
#         assert 3==3
#     def test_two(self):
#         try:
#             print("运行2")
#             assert 3 != 3
#         except BaseException as f:
#             print (f)
#     def teardown_class(self):
#         print("用例结束") 
# if __name__=="__main__":
#     pytest.main(["-s","test_one.py"])   


# @pytest.fixture(scope="class") 
# def login():
#     print("输入账号先登录")
# def test_s1(login):
#     print("登录过后的其他操作")
# @pytest.mark.usefixtures("login")
# def test_s2():
#     print("不需要登录")
# def test_a2():
#     print("不需要登录")
# def test_s3(login):
#     print("登录过后操作2")  
# if __name__=="__main__":
#     pytest.main(["-s","test_one.py"])   
# @pytest.fixture(scope="function")
# def admin():
#     print("打开浏览器")
# def test_s2():
#     print("打开浏览器1")
# def test_s3():
#     print("打开浏览器2")
# def test_s4():
#     print("打开浏览器4")
# if __name__=="__main__":
#     pytest.main(["-s","test_one.py"])   


