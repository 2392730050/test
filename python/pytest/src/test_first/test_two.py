# coding=gbk
import pytest
# @pytest.fixture(scope="module")
# def admin():
#     print("�������")
# def setup_class():
#     print("��ʼ����")
def test_one(login):
    print("�������3")
    #raise NameError    
def test_two():
    print("�������4")
def test_two1():
    print("�������5")
# def teardown_class():
#     print("���н���")
if __name__=="__main__":
    pytest.main(["-s","test_two.py"])   