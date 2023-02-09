from Config.Test_Data import TestData
from Pages.Login_Page import LoginPage
from Tests.test_base import BaseTest
from Utilities.base_Log import LogGen
from Utilities.random_Generator import RandGen

logger = LogGen.loggen()  # Logger
rand_set = RandGen.random_generator()

class TestLogin ( BaseTest ):
    def test_login_page_title(self):
        self.loginPage = LoginPage ( self.driver )
        title = self.loginPage.get_login_page_title ()
        logger.info( "********************Login page logs   ********************* " )
        assert title == "Your store. Login" , self.loginPage.take_screenshot (TestData.Scr_Sh)

    def test_login_panel_is_visible(self):
        self.loginPage = LoginPage ( self.driver )
        logger.info ( "**********Verify that Admin area demo is visible**************" )
        flag = self.loginPage.is_visible ( LoginPage.Admin_area_demo )
        assert flag

    def test_login(self):
        self.loginPage = LoginPage ( self.driver )
        self.loginPage.do_login ( TestData.Admin_email , TestData.Password )
        logger.info ( "**********Verify that logged in and button 'logout' is visible*************" )
        flag = self.loginPage.is_visible ( LoginPage.logout_button )
        assert flag


