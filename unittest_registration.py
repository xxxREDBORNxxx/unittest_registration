import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistration(unittest.TestCase):
    links: list = ["http://suninjuly.github.io/registration1.html",
                   "http://suninjuly.github.io/registration2.html"]
    check_selectors: dict = {"first_block .form-control.first": "Ivan",
                             "first_block .form-control.second": "Petrov",
                             "first_block .form-control.third": "Ivan.Petrov@mail.ru"}
    button_selector = "button.btn"
    registration_selector = "Welcome!"
    response_selector = "h1"
    wait_time: int = 3

    @staticmethod
    def check_element(browser, selector_element):
        return browser.find_element(By.CLASS_NAME, selector_element)

    @staticmethod
    def input_element(browser_element, value):
        return browser_element.send_keys(value)

    def activate_button(self, browser, selector_element):
        WebDriverWait(browser, self.wait_time).until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, selector_element))).click()
        # browser.find_element(By.CSS_SELECTOR, selector_element).click()

    # def wait_registration(self, browser):
    #     return WebDriverWait(browser, self.wait_time).until(EC.presence_of_element_located((
    #         By.LINK_TEXT, self.registration_selector)))

    @staticmethod
    def check_response(browser, selector_element):
        # устанавливаем ожидание перед поиском ответа регистрации для новой страницы
        browser.implicitly_wait(5)
        return browser.find_element(By.TAG_NAME, selector_element).text
        # return WebDriverWait(browser, 3).until(EC.presence_of_element_located((
        #     By.CSS_SELECTOR, selector_element))).text

    def test_registration_1(self):

        with webdriver.Chrome() as driver:
            driver.get(self.links[0])
            # заполняем обязательные поля формы регистрации
            for selectors_value, value in self.check_selectors.items():
                self.input_element(self.check_element(driver, selectors_value), value)

            self.activate_button(driver, self.button_selector)
            # self.wait_registration(driver)
            # time.sleep(1)
            self.assertEqual("Congratulations! You have successfully registered!",
                             self.check_response(driver, self.response_selector),
                             "Your last name is a Fly, you're out of luck!")

    def test_registration_2(self):

        with webdriver.Chrome() as driver:
            driver.get(self.links[1])

            for selectors_value, value in self.check_selectors.items():
                self.input_element(self.check_element(driver, selectors_value), value)

            self.activate_button(driver, self.button_selector)
            # self.wait_registration(driver)
            self.assertEqual("Congratulations! You have successfully registered!",
                             self.check_response(driver, self.response_selector),
                             "Your last name is a Fly, you're out of luck!")


if __name__ == "__main__":
    unittest.main()
