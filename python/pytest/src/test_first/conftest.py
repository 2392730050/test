# coding=gbk
import pytest
from selenium import webdriver
@pytest.fixture()
def login():
    driver=webdriver.Firefox()
    driver.get("https://www.baidu.com/")
    print("��¼")
    driver.quit()