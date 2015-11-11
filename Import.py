# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, re, random, csv

class iZettle():

    def setUp(self):
        #Configure these
        self.username = "email@domain.com"          #Your iZettle Admin Email Address (Admin require to add products)
        self.password = "Password123"               #Your iZettle Password
        self.csvfilename = "dummy.csv"              #Your csv file containing products
        
        #self.driver = webdriver.Firefox()              #Use for debugging
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(30)
        self.base_url = "https://my.izettle.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def __init__(self):
            print('Script Starting...')
            self.setUp()
            self.login()
            self.loadProducts()
            self.loopProducts()
            self.logout()
            print('Script Complete.')        

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


    def login(self):
        print('Logging In')
        driver = self.driver
        driver.get(self.base_url + "login")
        driver.find_element_by_xpath("//*[@id='user_email_address']").send_keys(self.username)
        driver.find_element_by_xpath("//*[@id='user_password']").send_keys(self.password)
        driver.find_element_by_xpath("//*[@id='new_user']/button").click()

    def logout(self):
        print('Logging Out')
        driver = self.driver
        driver.get(self.base_url + "logout")
        
    def addProduct(self, product):
        #Assign Values
        name    = product[0]
        variant = product[1]
        barcode = product[2]
        price   = product[3]
        tax     = product[4]

        print('Adding Product ' +variant)
        driver = self.driver
        #Add New Product
        driver.get(self.base_url + "products/new")

        #Configure
        driver.find_element_by_xpath("//*[@id='product_name']").send_keys(name)
        driver.find_element_by_xpath("//*[@id='new_product']/div[2]/div[1]/div/div[2]/fieldset[1]/input").send_keys(variant)
        driver.find_element_by_xpath("//*[@id='product_variants_attributes_0_barcode']").send_keys(barcode)
        driver.find_element_by_xpath("//*[@id='product_variants_attributes_0_price']").send_keys(price)
        Select(driver.find_element_by_xpath("//*[@id='product_vat_percentage']")).select_by_value(tax)
        
        #Submit
        driver.find_element_by_xpath("//*[@id='new_product']/div[2]/div[4]/button").click()

    def loadProducts(self):
        print('Loading products from CSV')
        import csv
        with open(self.csvfilename, 'rt') as f:
            reader = csv.reader(f)
            self.products = list(reader)
        return

    def loopProducts(self):
        print('Looping through products')
        for product in self.products:
            self.addProduct(product)
                         
iZettle()
