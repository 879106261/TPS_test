from selenium import webdriver
import time
import os,sys
sys.path.append('../lib')
#截图函数
def insert_img(driver,file_name):
    #获取父 父l路径名
    base_dir = os.path.dirname(os.path.dirname(__file__))
    #定义图片路径
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    #base = base_dir.split('/TPS_test')[0]
    execTime = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
    filr_name = execTime +'-'+ file_name
    file_path = base_dir +  '/report/image/'+ filr_name
    #截图
    driver.get_screenshot_as_file(file_path)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get('https://www.baidu.com')
    insert_img(driver,'baidu.png')
    print('ok')
    driver.quit()

