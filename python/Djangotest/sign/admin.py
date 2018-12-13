#coding=utf-8
from django.contrib import admin
from sign.models import Event,Guest
# Register your models here.
class eventadmin(admin.ModelAdmin):
    list_display=["id",'name','limit','address',"status",'create_tme']#输入要展示的内容
    search_fields=['name','address']#创建搜索栏
    list_filter=['status']#过滤器
class Gusetadmin(admin.ModelAdmin):
    list_display=['realname','phone','email',"sign",'call_now',"event"]
    search_fields=["realname",'phone']#搜索栏
    list_filter=['sign']#过滤器
admin.site.register(Event,eventadmin)
admin.site.register(Guest,Gusetadmin)