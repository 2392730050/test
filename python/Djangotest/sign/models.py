# coding=utf-8
from django.db import models

# Create your models here.
#发布会
#常用类型： 
    #AutoFiled:一个存放intgerField(整数字段)类型的自动增量
    #Booleanfiled:用于存放一个布尔值的数据
    #charfiled: 用于存放字符型数据需要使用max_length指定长度
    #DecimalFiled：小数类型
    #floatfiled:用户存放浮点型
    #intgerField:整数类型
    #DateTimeField:用于存放时间
    #Textfiled:用户存放文本数据类型
    #TimeField：时间类型
    #URLField：用于存放URL地址
    #BinaryField: 存储原始二进制数据的字段
    #ForeignKey：关联
class Event(models.Model):
    name = models.CharField(max_length=100) #发布会标题
    limit = models.IntegerField()#参加人数
    status = models.BooleanField()#状态״̬
    address = models.CharField(max_length = 200)#地址
    start_time= models.DateTimeField("发布会时间")#发布会时间
    create_tme = models.DateTimeField(auto_now=True)#当前时间
    #str方法告诉DJango以str方式显示
    def __str__(self):
        return self.name    
class Guest(models.Model):
    event = models.ForeignKey(Event,on_delete=models.DO_NOTHING)#关联发布会ID
    realname= models.CharField(max_length=200)#姓名
    phone = models.CharField(max_length=11)#手机号
    email= models.EmailField()#邮箱地址
    sign = models.BooleanField()#签到状态״̬
    call_now=models.DateTimeField(auto_now=True)#创建时间（自动获取当前时间）
class Meta:
    unique_together=("event","phone")#关联两个主键验证唯一性
def __str__(self):
    return self.realname