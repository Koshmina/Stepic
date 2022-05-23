import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('sites', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                   "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                   "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                   "https://stepik.org/lesson/236904/step/1",
                                   "https://stepik.org/lesson/236905/step/1"])


def test_lesson(browser, sites):
    c = '1'
    browser.get(sites)
    browser.implicitly_wait(10)
    inp = browser.find_element(By.XPATH, '//textarea')
    answer = math.log(int(time.time()))
    inp.send_keys(answer)
    button = browser.find_element(By.XPATH, '//button[text()="Отправить"]')
    # button= WebDriverWait(browser,5).until(EC.element_to_be_clickable(By.XPATH,'//button[text()="Отправить"]'))
    button.click()
    ass = browser.find_element(By.XPATH, '// pre[text() = "Correct!"]')
    if ass == 'False':
        c = c +


    print(c)
