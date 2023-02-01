from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self, title):
        WebDriverWait(self.driver, 2).until(ec.title_is(title))
        return self.driver.title

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 2).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def do_clear(self, by_locator):
        WebDriverWait(self, 2).until(ec.visibility_of_element_located(by_locator)).clear()
