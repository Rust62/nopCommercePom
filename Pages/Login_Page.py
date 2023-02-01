from selenium import webdriver
from selenium.webdriver.common.by import By
from Config import Test_Data
from Pages.Base_Page import BasePage


class LoginPage(BasePage):
    admin_email = (By.ID, "Email")
    admin_password = (By.XPATH, "Password")
    login_button = (By.XPATH, "//button[@type='submit']")
    logout_button = (By.XPATH, "//a[normalize-space()='Logout']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = webdriver.Chrome()
        self.driver.get(Test_Data.Base_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self):
        self.do_clear(self.admin_email)
        self.do_send_keys(self.admin_email, Test_Data.Admin_email)
        self.do_clear(self.admin_password)
        self.do_send_keys(self.admin_password, Test_Data.Password)
        # self.do_click(self.login_button)







