from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\Users\vithu\eclipse-workspace\chromedriver_win32\chromedriver.exe")
#driver = webdriver.Firefox()
#driver = webdriver.Ie()
driver.set_page_load_timeout(10)
driver.get(r"https://google.com")
driver.find_element_by_name("q").send_keys("python.org ")
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(4)
driver.quit()