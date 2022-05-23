from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//body/div/div/div/div/h5[@id]"),"$100")
    )
button=browser.find_element(By.XPATH,"//*[@id='book']")
button.click()
browser.execute_script("window.scrollBy(0, 300);")
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()

