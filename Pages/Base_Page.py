from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self , driver):
        self.driver = driver

    def do_click(self , by_locator):
        WebDriverWait ( self.driver , 5 ).until ( ec.presence_of_element_located ( by_locator ) ).click ()

    def do_send_keys(self , by_locator , text):
        WebDriverWait ( self.driver , 5 ).until ( ec.visibility_of_element_located ( by_locator ) ).send_keys ( text )

    def get_element_text(self , by_locator):
        element = WebDriverWait ( self.driver , 5 ).until ( ec.visibility_of_element_located ( by_locator ) )
        return element.text

    def is_visible(self , by_locator):
        element = WebDriverWait ( self.driver , 5 ).until ( ec.visibility_of_element_located ( by_locator ) )
        return bool ( element )

    def get_element(self , by_locator):
        element = WebDriverWait ( self.driver , 5 ).until ( ec.presence_of_element_located( by_locator ) )
        return element

    def get_title(self , title):
        WebDriverWait ( self.driver , 5 ).until ( ec.title_is ( title ) )
        return self.driver.title

    def do_clear(self , by_locator):
        WebDriverWait ( self.driver , 5 ).until ( ec.visibility_of_element_located ( by_locator ) ).clear ()

    def take_screenshot(self , file):
        return self.driver.save_screenshot ( file )

    def set_gender(self, gender, by_locator1, by_locator2):
        if gender == 'Male':
            self.do_click (by_locator1)
        elif gender == "Female":
            self.do_click (by_locator2)


    # # def setCustomerRoles(self , role):
    #     self.driver.find_element_by_xpath ( self.txtcustomerRoles_xpath ).click ()
    #     time.sleep ( 3 )
    #     if role == 'Registered':
    #         self.listitem = self.driver.find_element_by_xpath ( self.lstitemRegistered_xpath )
    #     elif role == 'Administrators':
    #         self.listitem = self.driver.find_element_by_xpath ( self.lstitemAdministrators_xpath )
    #     elif role == 'Guests':
    #         # Here user can be Registered( or) Guest, only one
    #         time.sleep ( 3 )
    #         self.driver.find_element_by_xpath ( "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]" ).click ()
    #         self.listitem = self.driver.find_element_by_xpath ( self.lstitemGuests_xpath )
    #     elif role == 'Registered':
    #         self.listitem = self.driver.find_element_by_xpath ( self.lstitemRegistered_xpath )
    #     elif role == 'Vendors':
    #         self.listitem = self.driver.find_element_by_xpath ( self.lstitemVendors_xpath )
    #     else:
    #         self.listitem = self.driver.find_element_by_xpath ( self.lstitemGuests_xpath )
    #     time.sleep ( 3 )
    #     # self.listitem.click()
    #     self.driver.execute_script ( "arguments[0].click();" , self.listitem )