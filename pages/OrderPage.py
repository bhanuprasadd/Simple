from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class OrderPage(object):

    def __init__(self, driver):
        self.driver = driver

    def click_on_orders(self):
        menuItem = self.driver.find_element_by_xpath("// *[@id = 'nav-link-yourAccount'] / span[2]")
        subMenuItem = self.driver.find_element_by_xpath("//*[@id='nav_prefetch_yourorders']/span")

        ActionChains(self.driver).move_to_element(menuItem).click(subMenuItem).perform()
        order_summary = self.driver.find_element_by_xpath("//*[@id='ordersContainer']/div[1]/label/span").text
        return order_summary
