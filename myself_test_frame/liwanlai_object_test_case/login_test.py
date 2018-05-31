from time import  sleep
import unittest
import sys
import logging

sys.path.append('../utils')
from utils import myunit
from utils.insert_img import insert_img
from utils.exe_deco import exe_deco
from utils.write_log import write_log
from utils.log_info  import Logger

from liwanlai_object_test_case.page_obj.loginPage import login
from liwanlai_object_test_case.page_obj.creatProjectPage import creatProject

log = Logger()

class loginTest(myunit.MyTest):
    '''liwanlei 登录测试'''
    def user_login_verify(self,username='',password=''):
        login(self.driver).user_login(username,password)

    @exe_deco
    def test_login1(self):
        '''用户名密码错误'''
        self.user_login_verify(username='bbt',password='123456')
        po = login(self.driver)
        self.assertEqual(po.user_login_error(),'用户不存在')
        log.output('用户不存在验证成功',level=logging.INFO)
        insert_img(self.driver, 'user_login_error.png')
        #write_log('user_login_error.png 图片插入成功')
        log.output('user_login_error.png 图片插入成功', level=logging.INFO)

    # @exe_deco
    # def test_login2(self):
    #     '''用户名密码正确'''
    #     self.user_login_verify(username='liwanlei',password='liwanlei')
    #     sleep(3)
    #     po = login(self.driver)
    #     self.assertEqual(po.user_login_success(), '首页')
    #     #write_log('用户登录在验证成功')
    #     log.output('用户登录在验证成功', level=logging.INFO)
    #     insert_img(self.driver, 'user_login_success.png')
    #     #write_log('user_login_success.png 图片插入成功')
    #     log.output('user_login_success.png 图片插入成功', level=logging.INFO)

if __name__ == '__main__':
    unittest.main()

