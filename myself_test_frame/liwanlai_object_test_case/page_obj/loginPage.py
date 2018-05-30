from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

# 用户登录liwanlei
class login(Page):
    url = '/login'
    login_username_loc = (By.ID,'username')
    login_password_loc = (By.ID,'password')
    login_button_loc = (By.CLASS_NAME,'btn')

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码名
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #定义统一登录入口
    def user_login(self,username='',password=''):
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(3)

    user_login_error_loc =(By.ID,'duanyan')
    user_login_success_loc =(By.XPATH,"//span[text()='首页']")
    #用户名密码错误
    def user_login_error(self):
        return self.find_element(*self.user_login_error_loc).text

    #登录成功
    def user_login_success(self):
        return self.find_element(*self.user_login_success_loc).text

