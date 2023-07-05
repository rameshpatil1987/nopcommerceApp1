import pytest

from generic.base_test import BaseTest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from generic.utility import Excel
from generic.customLogger import Loggen


class TestValidLogin(BaseTest):
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_validlogin(self):
        try:
            email = Excel.get_cellvalue("../data/input.xlsx", "Validlogin", 2, 1)
            password = Excel.get_cellvalue("../data/input.xlsx", "Validlogin", 2, 2)
        except:
            email = Excel.get_cellvalue("data/input.xlsx", "Validlogin", 2, 1)
            password = Excel.get_cellvalue("data/input.xlsx", "Validlogin", 2, 2)


        loginpage = LoginPage(self.driver)
        loginpage.set_email(email)
        loginpage.set_password(password)
        loginpage.click_on_loginbtn()
        homepage = HomePage(self.driver)
        result = homepage.verify_homepage_is_displayed(self.wait)
        assert result
        print(self.driver.title)
