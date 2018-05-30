from selenium.webdriver.common.by import By
from .base import Page
from time import sleep

class creatProject(Page):
    Project_loc = (By.XPATH,"//span[text()='项目']")
    creatProject_loc = (By.TAG_NAME,"input")
    projectName_loc = (By.ID,'project')
    create_loc = (By.TAG_NAME,"button")
    #点击项目
    def project(self):
        self.find_element(*self.Project_loc).click()

    #新增项目
    def projectcreat(self):
        self.find_element(*self.creatProject_loc).click()

    #填写项目名
    def projectName(self,name):
        self.find_element(*self.projectName_loc).send_keys(name)

    #点击添加
    def create(self):
        self.find_element(*self.create_loc).click()

    #创建项目主流程
    def creatProject(self,name=''):
        self.project()
        self.projectcreat()
        self.projectName(name)
        self.create()