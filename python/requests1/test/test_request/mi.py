# -*- coding: utf-8 -*- 
# import requests
# url="https://www.apiopen.top/login?key=00d91e8e0cca2b76f515926a36db68f5&"
# admin={'phone':"","passwd":"12344456"}
# r = requests.get(url=url,params=admin)
# r1=r.json()
# print(r.url)
# print(r.text)
# print (r1['data']["phone"])
# print (r1['data']["passwd"])
 
# import smtplib
# from email.mime.text import MIMEText
# from email.utils import formataddr
#     
# my_sender='2392730050@qq.com'    # 发件人邮箱账号
# my_pass = 'hzxjmsddwooqeafi'              # 发件人邮箱密码(当时申请smtp给的口令)
# my_user='488851885@qq.com'      # 收件人邮箱账号，我这边发送给自己
# def mail():
#     ret=True
#     try:
#         msg=MIMEText('测试发送邮件','plain','utf-8')
#         msg['From']=formataddr(["大号",my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
#         msg['To']=formataddr(["小号",my_user])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
#         msg['Subject']="邮件主题-测试"                # 邮件的主题，也可以说是标题
#         
#         server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
#         server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
#         server.sendmail(my_sender,[my_user,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
#         server.quit()# 关闭连接
#     except Exception:# 如果 try 中的语句没有执行，则会执行下面的 ret=False
#         ret=False
#     return ret
#     
# ret=mail()
# if ret:
#     print("邮件发送成功")
# else:
#     print("发送邮件失败")
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# 
# username='2392730050@qq.com'
# password="hzxjmsddwooqeafi"
# sender=username
# receivers = ','.join(['@qq.com'])
# 
# msg = MIMEMultipart()
# msg['Subject'] = 'Python mail Test'
# msg['From'] = sender
# msg['To'] = receivers
# 
# #html格式
# jpgpart = MIMEApplication(open('D:\\BeautifulReport\\2018-12-05 09_25_33接口测试报告.html', 'rb').read())
# jpgpart.add_header('Content-Disposition', 'attachment', filename='接口测试报告.html')
# msg.attach(jpgpart)
# 
# client = smtplib.SMTP()
# client.connect('smtp.qq.com')
# client.login(username, password)
# client.sendmail(sender, receivers, msg.as_string())
# client.quit()
# print("发送成功")

# dict = {1:1}
# print (dict)
# dict.clear()
# del dict
# print(dict)    
# import yaml
# f=open('yam1.yaml',encoding='utf-8')
# res=yaml.load(f)
# print(res)


import requests
url='https://transfer.swft.pro'
data={
    'username':'12121212',
    'password':'123456789'
}
def send_post(url,data):
    res=requests.post(url=url,data=data)
    res1=res.json()
    print(res)
    return res1

