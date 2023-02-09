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
birthday = "3/24/1990"
gender = "Male"
company_name = "Azal"
tax_exempt = "no"
role = "Registered"

class TestNewCustomer ( BaseTest ):

    def test_add_new_customer(self):
        self.loginPage = LoginPage ( self.driver )
        self.loginPage.do_login ( TestData.Admin_email , TestData.Password )
        self.loginPage.do_click(AddCustomer.Customers_menu)
        self.loginPage.do_click(AddCustomer.Customers_menu_item)
        self.loginPage.do_click(AddCustomer.Add_new)
        self.loginPage.do_send_keys(AddCustomer.Email, email)
        self.loginPage.do_send_keys(AddCustomer.First_name, first_name)
        self.loginPage.do_send_keys(AddCustomer.First_name, last_name)
        self.loginPage.do_send_keys(AddCustomer.Date_of_birth, birthday)
        self.loginPage.set_gender(gender, AddCustomer.Male_gender, AddCustomer.Female_gender)
        self.loginPage.take_screenshot(TestData.Scr_Sh1)
        self.loginPage.do_send_keys(AddCustomer.Company_name, company_name)
        if tax_exempt == "yes":
            self.loginPage.do_click(AddCustomer.Tax_exempt)

        # def setCustomerRoles(self , role):
            self.loginPage.do_click(AddCustomer.Customer_roles)

            if role == 'Registered':
                self.list_item = self.loginPage.get_element_text(AddCustomer.Customer_roles_registered)
            elif role == 'Administrators':
                self.list_item = self.loginPage.get_element_text(AddCustomer.Customer_roles_administrators)
            elif role == 'Guests':
            # Here user can be Registered( or) Guest, only one

                self.driver.find_element_by_xpath ( "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]" ).click ()
                self.listitem = self.driver.find_element_by_xpath ( self.lstitemGuests_xpath )
        #     elif role == 'Registered':
        #         self.listitem = self.driver.find_element_by_xpath ( self.lstitemRegistered_xpath )
        #     elif role == 'Vendors':
        #         self.listitem = self.driver.find_element_by_xpath ( self.lstitemVendors_xpath )
        #     else:
        #         self.listitem = self.driver.find_element_by_xpath ( self.lstitemGuests_xpath )
        #     time.sleep ( 3 )
        #     # self.listitem.click()
        #     self.driver.execute_script ( "arguments[0].click();" , self.listitem )





        time.sleep(3)

        # logger.info ( "**********Verify that logged in and button 'logout' is visible*************" )
        # flag = self.loginPage.is_visible ( LoginPage.logout_button )
        # assert flag


