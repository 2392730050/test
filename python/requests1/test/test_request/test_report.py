# coding=gbk
import time
import unittest
from BeautifulReport import BeautifulReport 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

test_dir='./'
discover=unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py' )

if __name__ == "__main__":
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    filename1=now +'接口测试报告.html'
    BeautifulReport(discover).report(description="接口注册测试", filename=filename1, log_path="./")


    username='2392730050@qq.com'
    password="hzxjmsddwooqeafi"
    sender=username
    receivers = ','.join(['488851885@qq.com'])

    #设置请求头信息
    msg = MIMEMultipart()
    msg['Subject'] = '接口测试报告' #邮件名
    msg['From'] = sender
    msg['To'] = receivers

    #html格式
    jpgpart = MIMEApplication(open(filename1, 'rb').read())
    jpgpart.add_header('Content-Disposition', 'attachment', filename='接口测试报告.html')
    msg.attach(jpgpart)
    
    #发送邮件
    client = smtplib.SMTP()
    client.connect('smtp.qq.com')
    client.login(username, password)
    client.sendmail(sender, receivers, msg.as_string())
    client.quit()
    print("测试报告以成功发送到邮箱")
