# coding=gbk
import pytest
# @pytest.fixture(scope="module")
# def admin():
#     print("打开浏览器")
# def setup_class():
#     print("开始运行")
def test_one(login):
    print("打开浏览器3")
    #raise NameError    
def test_two():
    print("打开浏览器4")
def test_two1():
    print("打开浏览器5")
# def teardown_class():
#     print("运行结束")
if __name__=="__main__":
    pytest.main(["-s","test_two.py"])   