import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    __lnkcustomer_menu = (By.XPATH, "(//ul[@role='menu'])[2]/li[4]")
    __lnkcustomer_menuitem = (By.XPATH, "(//ul[@class='nav nav-treeview'])[4]/li[1]")
    __btnadd_new = (By.XPATH, "//a[@class='btn btn-primary']")
    __txtemail = (By.ID, "Email")
    __txtpwd = (By.ID, "Password")
    __txtfirstname = (By.ID, "FirstName")
    __txtlastname = (By.ID, "LastName")
    __rdgendermale = (By.ID, "Gender_Male")
    __rdgenderfemale = (By.ID, "Gender_Female")
    __txtdob = (By.ID, "DateOfBirth")
    __companyname = (By.ID, "Company")
    __customerroles = (By.XPATH, "(//div[@class='k-multiselect-wrap k-floatwrap'])[2]")
    __customerrole_registered = (By.XPATH, "//span[text()='Registered']")
    __customerrole_administrators = (By.XPATH, "//span[text()='Administrators']")
    __customerrole_forummoderators = (By.XPATH, "//span[text()='Forum Moderators']")
    __customerrole_vendors = (By.XPATH, "//span[text()='Vendors']")
    __customerrole_guests = (By.XPATH, "//li[.='Guests']")
    __drpmanagerofvendors = (By.XPATH, "//select[@id='VendorId']")
    __txtadmincomment = (By.XPATH, "//textarea[@id='AdminComment']")
    __savebtn = (By.NAME, "save")

    def __init__(self, driver):
        self.__driver = driver

    def click_on_customer_menu(self):
        self.__driver.find_element(*self.__lnkcustomer_menu).click()

    def click_on_customer_menuitem(self):
        self.__driver.find_element(*self.__lnkcustomer_menuitem).click()

    def click_on_addnew(self):
        self.__driver.find_element(*self.__btnadd_new).click()

    def set_email(self, email):
        self.__driver.find_element(*self.__txtemail).send_keys(email)

    def set_password(self, pw):
        self.__driver.find_element(*self.__txtpwd).send_keys(pw)

    def set_firstname(self, fname):
        self.__driver.find_element(*self.__txtfirstname).send_keys(fname)

    def set_lastname(self, lname):
        self.__driver.find_element(*self.__txtlastname).send_keys(lname)

    def set_gender(self, gender):
        if gender == 'Male':
            self.__driver.find_element(*self.__rdgendermale).click()
        elif gender == 'Female':
            self.__driver.find_element(*self.__rdgenderfemale).click()
        else:
            self.__driver.find_element(*self.__rdgendermale).click()

    def set_dob(self, dob):
        self.__driver.find_element(*self.__txtdob).send_keys(dob)

    def set_companyname(self, cname):
        self.__driver.find_element(*self.__companyname).send_keys(cname)

    def set_customerroles(self, role):
        self.__driver.find_element(*self.__customerroles).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.__driver.find_element(*self.__customerrole_registered)
        elif role == 'Administrators':
            self.listitem = self.__driver.find_element(*self.__customerrole_administrators)
        elif role == 'Forum Moderators':
            self.listitem = self.__driver.find_element(*self.__customerrole_forummoderators)
        elif role == 'Vendors':
            self.listitem = self.__driver.find_element(*self.__customerrole_vendors)
        elif role == 'Guests':
            self.__driver.find_element(By.XPATH, "//span[@title='delete']").click()
            time.sleep(3)
            self.listitem = self.__driver.find_element(*self.__customerrole_guests)
        else:
            self.listitem = self.__driver.find_element(*self.__customerrole_guests)
        self.__driver.execute_script("arguments[0].click()", self.listitem)

    def set_managerofvendor(self, value):
        drp = Select(self.__driver.find_element(*self.__drpmanagerofvendors))
        drp.select_by_visible_text(value)

    def set_admincomment(self, comment):
        self.__driver.find_element(*self.__txtadmincomment).send_keys(comment)

    def clickonsavebtn(self):
        self.__driver.find_element(*self.__savebtn).click()


