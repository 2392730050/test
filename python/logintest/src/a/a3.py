#coding=utf-8
# def a(func):
#     print("a")
#     def inner():
#         print("111")
#         func()
#     return inner
# def b(func):
#     print("b")
#     def i():
#         print("222222")
#         func()
#     return i
# 
# def c(func):
#     def c1(*a,**b):
#         func(*a,**b)
#     return c1
# @a
# @b
# def f1():
#     print("2")
# @a
# @b
# def f2():
#     print(3)
# 
# @c
# def f3(a,b):
#     
#     print(a+b)
#     
# @c
# def f4(a,b,c):
#     print(a+b-c)
#     
# f3(4,2)
# f4(4,2,3)


# import requests
# a = requests.get("http://ws.webxml.com.cn/WebServices/WeatherWS.asmx").text
# print(a)


# import requests
# url = 'https://www.lagou.com/jobs/companyAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false'
# form_data = {'first': 'true',
#              'pn': '1',
#              'kd': 'python'}
# HEADERS = {
#     # User-Agent(UA) 服务器能够识别客户使用的操作系统及版本、CPU 类型、浏览器及版本、浏览器渲染引擎、浏览器语言、浏览器插件等。也就是说伪装成浏览器进行访问
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
#     # 用于告诉服务器我是从哪个页面链接过来的，服务器基此可以获得一些信息用于处理。如果不加入，服务器可能依旧会判断为非法请求
#     'Referer': 'https://www.lagou.com/zhaopin/Python/?labelWords=label'}
# 
# def getJobs():
#     res = requests.post(url=url, headers=HEADERS, data=form_data)
#     result = res.json()
#     print(result)
# 
# getJobs()


# 
# url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E6%B7%B1%E5%9C%B3&district=%E5%8D%97%E5%B1%B1%E5%8C%BA&needAddtionalResult=false&isSchoolJob=1'
# 
# HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
#     'Referer': 'https://www.lagou.com/jobs/list_Python?px=default&gx=&isSchoolJob=1&city=%E6%B7%B1%E5%9C%B3&district=%E5%8D%97%E5%B1%B1%E5%8C%BA'
# }
# 
# form_data = {'first': 'true',
#              'pn': '1',
#              'kd': 'python'}
# 
# def getJobs():
#     res = requests.post(url=url, headers=HEADERS, data=form_data)
#     result = res.json()
#     jobs = result['content']['positionResult']['result']
#     return jobs
# 
# for job in getJobs():
#     # 这里演示，提取出公司地址+名称+公司优势+工资待遇
#     print(job['district'] + ':' + job['companyFullName'] + ':' + job['positionAdvantage'] + ':' + job['salary'])

                                              

import requests
# url="http://qjwmall.ngrok.pisen.com.cn/"
# payload = {'key1': 'value1', 'key2': 'value2'}
# a=requests.get(url=url,params=payload)
# print(a.url)

#用户注册接口
# url="https://www.apiopen.top/login"
# payload={'key':'00d91e8e0cca2b76f515926a36db68f5',"phone":"13594347817","passwd":"123456","name":"叫爸爸"}
#headers = {'user-agent': 'my-app/0.0.1'}
# a = requests.get(url=url,params=payload)
# b = a.text
# print(a.url)
# print(b)
# filename="D:/Users/a2.txt"
# with open(filename,'a')as f:
#     f.write(b)
#     f.write("\n")
#assert b in "用户已注册！"

# payload = (('key1', 'value1'), ('key1', 'value2'))
# r = requests.post('http://httpbin.org/post', data=payload)
# print(r.text)


