from Pages.Base_Page import BasePage
from Pages.Login_Page import LoginPage
from Tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(LoginPage)
        assert title == "Your store. Login"





