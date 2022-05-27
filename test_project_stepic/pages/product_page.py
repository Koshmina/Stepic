from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException
import math


class ProductPage(BasePage):
    def bascet_add(self):
        self.should_be_button()
        self.click_button()
        self.solve_quiz_and_get_code()
        self.product_name()
        self.product_price()

    # self.should_be_add_good()

    def should_be_button(self):
        assert self.is_element_present(*ProductPageLocators.button_add_product), "No button"

    def click_button(self):
        button = self.browser.find_element(*ProductPageLocators.button_add_product)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def product_name(self):
        name_product = self.browser.find_element(*ProductPageLocators.name_product)
        allert_text = self.browser.find_elements(*ProductPageLocators.allert_text)
        allert_text[0].text
        assert name_product.text == allert_text[0].text, "Item does not match in bascet"

    def product_price(self):
        price = self.browser.find_element(*ProductPageLocators.price)
        allert_price = self.browser.find_element(*ProductPageLocators.allert_price)
        print(price.text)
        print(allert_price.text)
        assert price.text == allert_price.text, "price does not match"
