from Config.Test_Data import TestData
from Pages.Home_Page import HomePage
from Pages.Login_Page import LoginPage
from Tests.test_base import BaseTest


class TestHome (BaseTest):

    def test_dashboard_is_visible(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = self.loginPage.do_login(TestData.Admin_email, TestData.Password)
        dashboard = self.homePage.is_visible(HomePage.Dashboard)
        assert dashboard

