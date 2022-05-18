from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element(By.XPATH, "//body/div/form/h2/span[2]")
    num2 = browser.find_element(By.XPATH, "//body/div/form/h2/span[4]")
    c = int(num1.text) + int(num2.text)
    print(c)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(c))
    button1 = browser.find_element(By.XPATH, "//*[local-name()='button']")
    button1.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
