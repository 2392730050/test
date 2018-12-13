#coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from sign.models import Event,Guest
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import logging

# Create your views here.
def index(request):
    return HttpResponse("Django")
    
def index1(request):
    return render(request,"Djangopage.html")

def login_action(request):
    if request.method == "psot":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
    if username == "admin" and password == "admin123":
        return HttpResponseRedirect("/event_mange/")
    else:
        return render(request,"Djangopage.html","用户名或密码错误")

    return render(request,"Djangopage.html")
#导入Model中的Guest类 通过Guest.Objects.all()查询所有嘉宾对象(数据)
#并通过render()方法附加在guest_manage.html页面并返回客服端
@login_required
def guest_manage(request):
    guest_list = Guest.objects.all()
    username = request.session.get('username', '')
    #页面显示的个数
    paginator = Paginator(guest_list,5)
    #通过get请求显示到第几个界面
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    #如果没有page页 抛出PageNotAnInteger返回第一页数据
    except PageNotAnInteger:
        # 如果页数不是整型, 取第一页.
        contacts = paginator.page(1)
    #如果超出页数就抛出Emptypage异常，取最后一页
    except EmptyPage:
        # 如果页数超出查询范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})
   
    

@login_required
def event_manage(request):
    username=request.session.get('user','')
    event_list=Event.objects.all()
    return render(request,'guest_manage.html',{'user':username,'guests':event_list})


    
    
