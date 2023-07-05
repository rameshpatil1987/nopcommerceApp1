import time

import pytest

from generic.base_test import BaseTest
from pages.Addcustomer import AddCustomer
from pages.LoginPage import LoginPage
from pages.Searchcustomer import SearchCustomer


class TestSearchCustomer(BaseTest):
    @pytest.mark.run(order=1)
    @pytest.mark.regression
    def test_search_customer_by_email(self):
        loginpage = LoginPage(self.driver)
        addcust = AddCustomer(self.driver)
        searchcust = SearchCustomer(self.driver)
        loginpage.set_email("admin@yourstore.com")
        loginpage.set_password("admin")
        loginpage.click_on_loginbtn()
        addcust.click_on_customer_menu()
        addcust.click_on_customer_menuitem()
        searchcust.set_email("victoria_victoria@nopCommerce.com")
        searchcust.click_on_searchbtn()
        time.sleep(5)
        status = searchcust.search_customer_by_email("victoria_victoria@nopCommerce.com")
        print('cust name is found by email')
        assert status

    @pytest.mark.run(order=2)
    @pytest.mark.regression
    def test_search_customer_by_name(self):
        loginpage = LoginPage(self.driver)
        addcust = AddCustomer(self.driver)
        searchcust = SearchCustomer(self.driver)
        loginpage.set_email("admin@yourstore.com")
        loginpage.set_password("admin")
        loginpage.click_on_loginbtn()
        addcust.click_on_customer_menu()
        addcust.click_on_customer_menuitem()
        searchcust.set_fname("Brenda")
        searchcust.set_lname(" Lindgren")
        searchcust.click_on_searchbtn()
        status = searchcust.search_customer_by_name("Brenda Lindgren")
        print('cust name is found by full name')
        assert status


