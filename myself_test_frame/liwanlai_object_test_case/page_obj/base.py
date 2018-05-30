#页面基础类，用于所有页面的继承
class Page(object):
    liwanlei_url = 'http://47.104.199.225'

    def __init__(self,selenium_driver,base_url=liwanlei_url,parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self,url):
        url = self.base_url+url
        self.driver.get(url)
        #assert self.on_page(),'地址:%s 没有打开'%url

    def find_element(self,*doc):
        return self.driver.find_element(*doc)

    def find_elements(self,*doc):
        return self.driver.find_element(*doc)

    def open(self):
        self._open(self.url)

    # def on_page(self):
    #     return self.driver.current_url == (self.base_url+self.url)

    def script(self,src):
        return self.driver.execute_script(src)
