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
    filename1=now +'�ӿڲ��Ա���.html'
    BeautifulReport(discover).report(description="�ӿ�ע�����", filename=filename1, log_path="./")


    username='2392730050@qq.com'
    password="hzxjmsddwooqeafi"
    sender=username
    receivers = ','.join(['488851885@qq.com'])

    #��������ͷ��Ϣ
    msg = MIMEMultipart()
    msg['Subject'] = '�ӿڲ��Ա���' #�ʼ���
    msg['From'] = sender
    msg['To'] = receivers

    #html��ʽ
    jpgpart = MIMEApplication(open(filename1, 'rb').read())
    jpgpart.add_header('Content-Disposition', 'attachment', filename='�ӿڲ��Ա���.html')
    msg.attach(jpgpart)
    
    #�����ʼ�
    client = smtplib.SMTP()
    client.connect('smtp.qq.com')
    client.login(username, password)
    client.sendmail(sender, receivers, msg.as_string())
    client.quit()
    print("���Ա����Գɹ����͵�����")