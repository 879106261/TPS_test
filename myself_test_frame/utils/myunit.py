from .driver import openbrower
import unittest
from selenium import webdriver


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = openbrower()
        #self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    #
    # def test(self):
    #     self.driver.get('https://www.baidu.com')

    def tearDown(self):
        self.driver.quit()

class MyTestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = openbrower()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()



