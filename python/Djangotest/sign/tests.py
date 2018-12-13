#coding=utf-8
from django.test import TestCase
from models import Event,Guest
# Create your tests here.
class ModelTest(TestCase):
    def setUp(self):
        Event.object.create(id=1,name="12",limit=10,address='cd',status=True,create_tme='2018-11-29')
        Guest.object.create(id=1,Event_id=1,realname='张三',phone='1834922505',email='23927@qq.com',sign=True)
        
    def test_Event(self):
        result = Event.object.get(name="12")
        self.assertEqual(result.name, "12", "断言失败1")
        self.assertTrue(result.status)
    def test_Guest(self):    
        result = Event.object.get(phone="1834922505")
        self.assertEqual(result.realname, "张三", "断言失败1")
        self.assertTrue(result.sign)