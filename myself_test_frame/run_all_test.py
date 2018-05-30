from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time


def send_mail():
    pass

#执行测试用例
now = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
filename = './report/'+ now + '-result.html'
fp = open(filename,'wb')
runner = HTMLTestRunner(stream=fp,title ='liwanlei平台ui测试',description='环境：win10 浏览器：火狐')
discover = unittest.defaultTestLoader.discover('liwanlai_object_test_case',pattern='*_test.py')
runner.run(discover)
fp.close()
