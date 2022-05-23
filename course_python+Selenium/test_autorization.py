from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

link='https://icl-dev.sblogistica.ru/login'
browser=webdriver.Chrome()
browser.get(link)


# browser.switch_to.window(browser.window_handles[1])
# browser.get(link)
# browser.close()
# browser.switch_to.window(browser.window_handles[0])

login=browser.find_element_by_xpath("//input[@name='username']")

login.send_keys("Client1")
password=browser.find_element_by_xpath("//input[@name='password']")
password.send_keys("test1")
button=browser.find_element_by_xpath("//button[text()='Войти']")
button.click()
