import unittest
from selenium import webdriver
from tasks.login_page import LoginPage
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service


class Test_Login(unittest.TestCase):

    #driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    driver = webdriver.Chrome(executable_path="chromedriver.exe")

    __user = 'standard_user'
    __password = 'secret_sauce'

    __usuario ='a'
    __contraseña = 'b'
    #__button = '//*[@id="login-button"]'

    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.maximize_window()
        driver.implicitly_wait(10)

    def test1_login(self):
        page_login = LoginPage().init_page(self.driver)
        self.assertTrue(page_login)

    def test2_insert_credential(self):
        driver = self.driver
        LoginPage().enter_credential(driver, self.__user, self.__password)

    def test3_login(self):
        driver = self.driver
        page_pantalla = LoginPage().enter_login(driver, self.__usuario, self.__contraseña)
        self.assertTrue(page_pantalla)

    def test4_imagen(self):
        driver = self.driver
        page_saucelabs = LoginPage().enter_saucelabs(driver, self.__user, self.__password)
        self.assertTrue(page_saucelabs)

        #driver = self.driver
        #LoginPage().enter_login(driver, self.__user, self.__password)
        #self.assertTrue()


    #@classmethod
    #def tearDownClass(cls):
     #   cls.driver.quit()
