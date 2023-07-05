import pytest

from generic.base_test import BaseTest
from pages.LoginPage import LoginPage
from generic.utility import Excel


class TestInValidLogin(BaseTest):

    @pytest.mark.regression
    def test_invalid(self):
        for r in range(2,6):
            try:
                email = Excel.get_cellvalue("../data/input.xlsx","Invalidlogin",r, 1)
                password = Excel.get_cellvalue("../data/input.xlsx","Invalidlogin",r, 2)
            except:
                email = Excel.get_cellvalue("data/input.xlsx", "Invalidlogin", r, 1)
                password = Excel.get_cellvalue("data/input.xlsx", "Invalidlogin", r, 2)
            loginpage=LoginPage(self.driver)
            loginpage.set_email("admin@yourstore.com1")
            loginpage.set_password("admin")
            loginpage.click_on_loginbtn()
            result=loginpage.verify_errormsg_is_displayed(self.wait)
            assert result
        print(self.driver.title)