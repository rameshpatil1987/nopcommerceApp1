from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    __email=(By.ID,"Email")
    __password=(By.ID,"Password")
    __loginbtn=(By.XPATH,"//button[@type='submit']")
    __errormsg=(By.XPATH,"//div[contains(text(),'unsuccessful')]")

    def __init__(self,driver):
        self.__driver=driver

    def set_email(self,email):
        self.__driver.find_element(*self.__email).clear()
        self.__driver.find_element(*self.__email).send_keys(email)

    def set_password(self,password):
        self.__driver.find_element(*self.__password).clear()
        self.__driver.find_element(*self.__password).send_keys(password)

    def click_on_loginbtn(self):
        self.__driver.find_element(*self.__loginbtn).click()

    def verify_errormsg_is_displayed(self,wait):
        try:
            wait.until(EC.visibility_of_element_located(self.__errormsg))
            print('error msg is displayed')
            return True
        except:
            print('error msg is displayed')
            return False

