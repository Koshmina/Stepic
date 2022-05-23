from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test():
    try:
        link='http://suninjuly.github.io/wait1.html'
        browser=webdriver.Chrome()
        browser.get(link)
        button=WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Verify']")))

        button.click()
        message=browser.find_element_by_xpath("//div[@id='verify_message']")
        assert "Verification was sccessful!" in message.text
    except AssertionError :
        raise Exception("Текст")
    except ZeroDivisionError :
        raise Exception("Текст2")


    finally:
        time.sleep(6)
        browser.close()