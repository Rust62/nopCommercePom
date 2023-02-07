from selenium.webdriver.common.by import By

from Config.Test_Data import TestData
from Pages.Base_Page import BasePage
from Pages.Home_Page import HomePage


class LoginPage ( BasePage ):

    def __init__(self , driver):
        super ().__init__ ( driver)
        self.driver.get ( TestData.Base_URL)

    admin_email = (By.ID , "Email")
    admin_password = (By.ID , "Password")
    login_button = (By.XPATH , "//button[@type='submit']")
    logout_button = (By.XPATH , "//a[normalize-space()='Logout']")
    Title = (By.XPATH, "//title")
    Admin_area_demo = (By.XPATH, "//h1[normalize-space()='Admin area demo']")

    def get_login_page_title(self):
        return self.driver.title

    def do_login(self, username, password):
        self.do_clear ( self.admin_email )
        self.do_clear ( self.admin_password )
        self.do_send_keys ( self.admin_email , username )
        self.do_send_keys ( self.admin_password , password)
        self.do_click ( self.login_button )
        return HomePage(self.driver)

    def loggen(self):
        pass

