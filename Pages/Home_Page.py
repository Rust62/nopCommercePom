from selenium.webdriver.common.by import By
from Pages.Base_Page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    Dashboard = (By.XPATH, "//h1[normalize-space()='Dashboard']")


