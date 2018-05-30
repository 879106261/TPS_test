from time import  sleep
import unittest
import sys

sys.path.append('../utils')
sys.path.append('../utils')
from utils import myunit
from utils.insert_img import insert_img
from utils.exe_deco import exe_deco
from utils.write_log import write_log


from liwanlai_object_test_case.page_obj.loginPage import login
from liwanlai_object_test_case.page_obj.creatProjectPage import creatProject

class creatProjectTest(myunit.MyTestClass):
    @exe_deco
    def user_login(self,username='liwanlei',password='liwanlei'):
        '''登录'''
        login(self.driver).user_login(username, password)
        write_log('登录成功')
    @exe_deco
    def test_creatProject(self):
        '''创建项目'''
        self.user_login()
        creatProject(self.driver).creatProject(name='爱德华3')
        write_log('项目创建成功')
        insert_img(self.driver, 'creat_project_success.png')
        write_log('creat_project_success.png 图片插入成功')


if __name__ == '__main__':
    unittest.main()
