import unittest
from selenium import webdriver
import pages
from pages import Homepage
from pages import OrderPage


class MyTestCase(unittest.TestCase):
    global home
    global login
    def setUp(self):
        self.driver = webdriver.Chrome('\\\\USHOUHOME01\\devalbr\\Desktop\\Chrome_driver\\chromedriver.exe')
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.in/")
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()

    def testcase1(self):
        self.home = pages.Homepage.HomePage(self.driver)
        page_title = self.home.get_page_title()
        print(page_title)
        self.assertEqual(self.home.get_page_title(),"Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in")
    def testcase2(self):
        self.home = pages.Homepage.HomePage(self.driver)
        self.home.login()
        self.login = pages.OrderPage.OrderPage(self.driver)
        self.assertEquals(self.login.click_on_orders(),"0 orders")

if __name__ == '__main__':
    unittest.main()
