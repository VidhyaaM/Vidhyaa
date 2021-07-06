from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from selenium.webdriver.common.keys import Keys
class GoogleSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\vithu\eclipse-workspace\chromedriver_win32\chromedriver.exe")
        cls.driver.set_page_load_timeout(10)
        cls.driver.maximize_window()
    def test_srearch_python(self):
        self.driver.get(r"https://google.com")
        self.driver.find_element_by_name("q").send_keys("python.org")
        self.driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
    def test_srearch_name(self):
        self.driver.get(r"https://google.com")
        self.driver.find_element_by_name("q").send_keys(" vidhyaa ")
        self.driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
if __name__ =='__main__':
    unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output='C:/Users/vithu/eclipse-workspace/PythonPractice2/SelProj1/reports'))
