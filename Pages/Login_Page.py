from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from Config.Test_Data import TestData
from Pages.Base_Page import BasePage
from Pages.Customers_Page import AddCustomer
from Pages.Home_Page import HomePage


class LoginPage ( BasePage ):
    def __init__(self , driver):
        super ().__init__ ( driver )
        self.list_item = None
        self.driver.get ( TestData.Base_URL )

    admin_email = (By.ID , "Email")
    admin_password = (By.ID , "Password")
    login_button = (By.XPATH , "//button[@type='submit']")
    logout_button = (By.XPATH , "//a[normalize-space()='Logout']")
    Title = (By.XPATH , "//title")
    Admin_area_demo = (By.XPATH , "//h1[normalize-space()='Admin area demo']")

    def get_login_page_title(self):
        return self.driver.title

    def do_login(self , username , password):
        self.do_clear ( self.admin_email )
        self.do_clear ( self.admin_password )
        self.do_send_keys ( self.admin_email , username )
        self.do_send_keys ( self.admin_password , password )
        self.do_click ( self.login_button )
        return HomePage ( self.driver )

    def set_customer_role(self, role):
        self.do_click ( AddCustomer.Customer_roles )
        if role == 'Registered':
            self.list_item = self.get_element ( AddCustomer.Customer_roles_registered )
        elif role == 'Administrators':
            self.list_item = self.get_element ( AddCustomer.Customer_roles_administrators )
        elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one
            self.do_click ( AddCustomer.btn_delete_registered )
            self.list_item = self.get_element ( AddCustomer.Customer_roles_guests )
        elif role == 'Forum Moderators':
            self.list_item = self.get_element ( AddCustomer.Customer_roles_forum_moderators )
        elif role == 'Vendors':
            self.list_item = self.get_element ( AddCustomer.Customer_roles_vendors )
        else:
            self.list_item = self.get_element ( AddCustomer.Customer_roles_guests )
        self.list_item.click()
        # self.driver.execute_script ( "arguments[0].click();" , self.list_item )

    def set_manager_of_vendor(self , value):
        drp = Select ( self.get_element(AddCustomer.Manager_of_vendor))
        drp.select_by_visible_text ( value )
