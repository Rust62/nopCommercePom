import time

from Config.Test_Data import TestData
from Pages.Customers_Page import AddCustomer
from Pages.Login_Page import LoginPage
from Tests.test_base import BaseTest
from Utilities.base_Log import LogGen
from Utilities.random_Generator import RandGen

logger = LogGen.loggen ()  # Logger
rand_set = RandGen.random_generator ()

email = rand_set + "@gmail.com"
first_name = "John"
last_name = "Smith"
password = "12345"
birthday = "3/24/1990"
gender = "Male"
company_name = "Azal"
tax_exempt = "no"
role = "Registered"
manager_of_vendor = "Vendor 2"
admin_comment = "****This is for testing add new customer****** "


class TestNewCustomer ( BaseTest ):

    def test_add_new_customer(self):
        self.loginPage = LoginPage ( self.driver)
        self.loginPage.do_login ( TestData.Admin_email , TestData.Password )
        self.loginPage.do_click ( AddCustomer.Customers_menu )
        self.loginPage.do_click ( AddCustomer.Customers_menu_item )
        self.loginPage.do_click ( AddCustomer.Add_new )
        self.loginPage.do_send_keys ( AddCustomer.Email , email )
        self.loginPage.do_send_keys ( AddCustomer.Password , password )
        self.loginPage.do_send_keys ( AddCustomer.First_name , first_name )
        self.loginPage.do_send_keys ( AddCustomer.Last_name, last_name )
        self.loginPage.do_send_keys ( AddCustomer.Date_of_birth , birthday )
        self.loginPage.set_gender ( gender , AddCustomer.Male_gender , AddCustomer.Female_gender )
        self.loginPage.take_screenshot ( TestData.Scr_Sh1 )
        self.loginPage.do_send_keys ( AddCustomer.Company_name , company_name )
        if tax_exempt == "yes":
            self.loginPage.do_click ( AddCustomer.Tax_exempt )

        # self.loginPage.set_customer_role(role)
        self.loginPage.set_manager_of_vendor(manager_of_vendor)
        self.loginPage.do_send_keys(AddCustomer.Admin_comment, admin_comment)
        self.loginPage.do_click(AddCustomer.Save_btn)

        text = self.loginPage.get_element_text(AddCustomer.Add_success_alert)
        assert text == "×\nThe new customer has been added successfully."






