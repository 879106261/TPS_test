from selenium.webdriver import Remote
from selenium import webdriver

#使用Remote执行分布式测试，启动浏览器
def browser():
    host = '127.0.0.1:8080'
    dc = {'browserName':'firefox'}
    driver = Remote(command_executor='http://'+host+'/wd/hub',desired_capabilities=dc)
    return driver

def openbrower():
    driver = webdriver.Firefox()
    return driver


if __name__ =='__main__':
    dr = openbrower()
    dr.get('https://www.jd.com')
    #dr.quit