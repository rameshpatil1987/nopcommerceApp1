from selenium.webdriver.common.by import By



class SearchCustomer:
    __email = (By.XPATH, "//input[@type='email']")
    __fname = (By.XPATH, "//input[@id='SearchFirstName']")
    __lname = (By.XPATH, "//input[@id='SearchLastName']")
    __searchbtn = (By.XPATH, "//button[@id='search-customers']")
    __table = (By.XPATH, "//table[@id='customers-grid']")
    __tablerows = (By.XPATH, "//table[@id='customers-grid']//tbody/tr")
    __tablecolumns = (By.XPATH, "//table[@id='customers-grid']//tbody/tr/td")

    def __init__(self, driver):
        self.__driver = driver

    def set_email(self,email):
        self.__driver.find_element(*self.__email).send_keys(email)

    def set_fname(self,fname):
        self.__driver.find_element(*self.__fname).send_keys(fname)

    def set_lname(self, lname):
        self.__driver.find_element(*self.__lname).send_keys(lname)

    def click_on_searchbtn(self):
        self.__driver.find_element(*self.__searchbtn).click()


    def get_rows(self):
        return len(self.__driver.find_elements(*self.__tablerows))

    def get_columns(self):
        return len(self.__driver.find_elements(*self.__tablecolumns))

    def search_customer_by_email(self, email):
        flag = False
        for r in range(1, self.get_rows() + 1):
            table = self.__driver.find_element(*self.__table)
            email_id = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, Name):
        flag = False
        for r in range(1, self.get_rows() + 1):
            table = self.__driver.find_element(*self.__table)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']//tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag


