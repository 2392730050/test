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
#         print("���н���")
#     def test_Three(self):
#         x3="admin"
#         assert x3=="adin"
#     def test_four(self):
#         assert 3 == 3

import pytest

# class Testclass:
#     def setup_module(self):
#         print("setup_module:��������ֻ����һ��")
#     def teardown_module(self):
#         print("setup_module:��������ֻ����һ��")
#     def setup_function(self):
#         print("��ͷ")    
#     def teardown_function(self):
#         print("���н���")
#     def setup_class(self):
#         print("������ʼ")
#     def test_one(self):
#         print("������")
#         assert 3==3
#     def test_two(self):
#         try:
#             print("����2")
#             assert 3 != 3
#         except BaseException as f:
#             print (f)
#     def teardown_class(self):
#         print("��������") 
# if __name__=="__main__":
#     pytest.main(["-s","test_one.py"])   


# @pytest.fixture(scope="class") 
# def login():
#     print("�����˺��ȵ�¼")
# def test_s1(login):
#     print("��¼�������������")
# @pytest.mark.usefixtures("login")
# def test_s2():
#     print("����Ҫ��¼")
# def test_a2():
#     print("����Ҫ��¼")
# def test_s3(login):
#     print("��¼�������2")  
# if __name__=="__main__":
#     pytest.main(["-s","test_one.py"])   
# @pytest.fixture(scope="function")
# def admin():
#     print("�������")
# def test_s2():
#     print("�������1")
# def test_s3():
#     print("�������2")
# def test_s4():
#     print("�������4")
# if __name__=="__main__":
#     pytest.main(["-s","test_one.py"])   

