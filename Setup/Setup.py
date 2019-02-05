'''
Created on Aug 30, 2018

@author: devalbr
'''
from selenium import webdriver


class Setup(object):
    '''
    classdocs
    '''

    def setup(self):
        self.driver = webdriver.Chrome("\\\\USHOUHOME01\\devalbr\\Desktop\\Chrome_driver\\chromedriver.exe")

    def tearDown(self):
        self.driver.close()

