from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())
link='http://suninjuly.github.io/cats.html#'
browser.get(link)
c=browser.find_element_by_xpath('//div')
browser.switch_to.window(browser.window_handles[1])
browser.close()
browser.switch_to.window(browser.window_handles[0])




time.sleep(12)