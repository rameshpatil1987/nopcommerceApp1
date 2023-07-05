import random
import string
import time

import pytest
from selenium.webdriver.common.by import By

from generic.base_test import BaseTest
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.Addcustomer import AddCustomer


class TestAddCustomer(BaseTest):
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addcustomer(self):
        loginpage = LoginPage(self.driver)
        loginpage.set_email("admin@yourstore.com")
        loginpage.set_password("admin")
        loginpage.click_on_loginbtn()
        time.sleep(10)
        addcustomer = AddCustomer(self.driver)
        addcustomer.click_on_customer_menu()
        addcustomer.click_on_customer_menuitem()
        addcustomer.click_on_addnew()

        self.email = random_generator() + "@gmail.com"
        addcustomer.set_email(self.email)
        addcustomer.set_password("test123")
        addcustomer.set_firstname("ramesh")
        addcustomer.set_lastname("patil")
        addcustomer.set_gender("Male")
        addcustomer.set_dob("10/01/1987")
        addcustomer.set_companyname("telusko")
        addcustomer.set_customerroles("Guests")
        addcustomer.set_managerofvendor("Vendor 2")
        addcustomer.set_admincomment("this is testing")
        addcustomer.clickonsavebtn()

        msg=self.driver.find_element(By.TAG_NAME,"body").text

        if "The new customer has been added successfully." in msg:
            print('new customer is added')
            assert True
        else:
            print('new customer is not added')
            assert False
        time.sleep(7)




def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))
