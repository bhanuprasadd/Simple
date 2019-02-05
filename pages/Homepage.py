from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class HomePage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_on_Login(self):
        element1 = self.driver.find_element_by_xpath("//span[text()='Hello, Sign in']")
        element2 = self.driver.find_element_by_xpath("//*[@id='nav-flyout-ya-signin']/a/span")
        ActionChains(self.driver).move_to_element(element1).click(element2).perform()

    def get_page_title(self):
        return self.driver.title

    def login(self):
        self.click_on_Login()
        self.driver.implicitly_wait(300)
        self.driver.find_element_by_id("ap_email").send_keys("bhanu.d.prasad@gmail.com")
        self.driver.find_element_by_xpath("//*[@id='continue']").click()
        self.driver.find_element_by_id("ap_password").send_keys("Indrani@143")
        self.driver.find_element_by_id("signInSubmit").click()


'''


    def click_on_depart_city(self):
        self.driver.find_element_by_id("ctl00_mainContent_ddl_originStation1_CTXT").click()
        self.driver.find_element_by_xpath("//a[@value ='HYD']").click()

    def click_on_arrival_city(self):
        self.driver.find_element_by_xpath("(//a[@value ='BLR'])[2]").click()

    def get_text_from_drop_down(self):
        element = self.driver.find_element_by_id("ctl00_mainContent_ddl_originStation1_CTXT")
        return element.text
'''




