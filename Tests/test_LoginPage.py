import logging
from Config.Test_Data import TestData
from Pages.Login_Page import LoginPage
from Tests.test_base import BaseTest

logger = logging.getLogger ( __name__ )
logger.setLevel ( logging.INFO )
logging.basicConfig ( filename="login_page.log",
                      format='%(asctime)s: %(levelname)s: %(message)s' ,
                      datefmt='%m/%d/%y %I:%M:%S %p'
                      )


# formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
# file_handler = logging.FileHandler("login_page.log")
# # file_handler.setLevel(logging.INFO)
# file_handler.setFormatter(formatter)
# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)


class TestLogin ( BaseTest ):

    def test_login_page_title(self):
        self.loginPage = LoginPage ( self.driver )
        title = self.loginPage.get_login_page_title ()
        logger.info ( "********************Login page logs ********************* " )
        assert title == "Your store. Login" , self.loginPage.take_screenshot ( TestData.Scr_Sh )

    def test_login_panel_is_visible(self):
        self.loginPage = LoginPage ( self.driver )
        logger.info("**********Verify that Admin area demo is visible**************")
        flag = self.loginPage.is_visible ( LoginPage.Admin_area_demo )
        assert flag

    def test_login(self):
        self.loginPage = LoginPage ( self.driver )
        self.loginPage.do_login ( TestData.Admin_email , TestData.Password )
        logger.info("**********Verify that logged in and button 'logout' is visible*************")
        flag = self.loginPage.is_visible(LoginPage.logout_button)
        assert flag
