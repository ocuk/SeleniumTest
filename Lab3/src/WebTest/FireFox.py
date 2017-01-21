#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
binary = FirefoxBinary('C:\Program Files (x86)\Mozilla Firefox\Firefox.exe')
 
class FireFoxTests(unittest.TestCase):
     
    def setUp(self):
        self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver.get('https://www.facebook.com')
        sleep(1)
 
    def tearDown(self):
        # end the session
        self.driver.quit()
     
    def test_check_terms(self):
             
        # click the terms of service link
        terms = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'terms-link')))
        self.assertIsNotNone(terms, 'no terms')
        terms.click()
        sleep(2)
     
        # focus on the new tab 
        tabs = self.driver.window_handles
        self.driver.switch_to_window(tabs[1])
        sleep(2)
        assert "Пользовательское соглашение".decode('utf8') in self.driver.title
         
             
        # scroll down the page
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2)      
             
        # return to the main tab   
        body = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        self.assertIsNotNone(body, 'no body') 
        body.send_keys(Keys.CONTROL + Keys.TAB)
        self.driver.switch_to_window(tabs[0])
        sleep(3)
        assert "Добро пожаловать на Фейсбук".decode("utf8") in self.driver.title
            
    def test_log_in(self):
            
        # set up
        driver = self.driver
        my_email = 'overkholyak@gmail.com'
        my_password = '9fyn1iPF'
    
        # log in
        email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
        email.send_keys(my_email)
        passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
        passw.send_keys(my_password)
        passw.submit()
                
        profile = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='_2s25']")))
        profile.click()
        sleep(5)
        assert 'Oxana Verkholyak' in driver.title 
                
        # scrool down
        for i in range(200): 
            e = 2*i + 1
            b = 2*i - 1
             
            script = 'window.scrollTo(' + str(b) + ', ' + str(e) + ');'
            driver.execute_script(script)            
        sleep(2)   
            
        # open dropout menu
        nav = driver.find_element_by_id('userNavigationLabel')
        nav.click()
        sleep(5)
         
        #log out
        logout = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, 'show_me_how_logout_1')))
        driver.execute_script("$(arguments[0]).click();", logout)
        sleep(3)
        assert 'Facebook' in driver.title 
           
             
    def test_sign_up(self):
             
        driver = self.driver
        name = 'Yakity'
        surname = 'Yak'
        mail = 'ryku@gmail.ru'
        password = 'sdfhs3534q'
       
        fname = driver.find_element_by_name("firstname")
        fname.send_keys(name)
        lname = driver.find_element_by_name("lastname")
        lname.send_keys(surname)
       
        email = driver.find_element_by_name("reg_email__")
        email.send_keys(mail)
        emconf = driver.find_element_by_name("reg_email_confirmation__")
        emconf.send_keys(mail)
        passw = driver.find_element_by_name("reg_passwd__")
        passw.send_keys(password)
       
        select = Select(driver.find_element_by_id('day'))
        select.select_by_visible_text('29')
        select = Select(driver.find_element_by_id('month'))
        select.select_by_visible_text('Май')
        select = Select(driver.find_element_by_id('year'))
        select.select_by_visible_text('1991')
       
        gender = driver.find_element_by_id('u_0_i')
        gender.click()
       
        submit =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'u_0_e')))
        driver.execute_script("$(arguments[0]).click();", submit)
        sleep(5)
        element =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'u_6_4')) or EC.presence_of_element_located((By.ID, 'u_0_5')))
        assert element.text == 'Проверка безопасности'.decode('utf8')
        sleep(5)
        
        driver.back()
        sleep(3)
            
    def test_post(self):
            
        #set up
        driver = self.driver
        my_email = 'overkholyak@gmail.com'
        my_password = '9fyn1iPF'
     
        # log in
        email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
        email.send_keys(my_email)
        passw = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
        passw.send_keys(my_password)
        passw.submit()
        sleep(5)
    
        box = driver.find_element_by_xpath("//div[@class='_2aha' and text()='Feeling/Activity']")
        self.assertIsNotNone(box, 'no box')
        box.click()
        sleep(2)
          
        body = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        self.assertIsNotNone(body, 'no body') 
        body.send_keys('Automatic post')  
            
        privacy = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'u_0_1b')))
        privacy.click()
        sleep(5)
            
        onlyme = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_48u1' and text()='Only Me']")))
        onlyme.click()
        sleep(5) 
            
        post = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='_1mf7 _4jy0 _4jy3 _4jy1 _51sy selected _42ft']")))
        post.click()
        sleep(3) 
            
        txt = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[text()='Automatic post]")))
        self.assertIsNotNone(txt, 'not posted')
  
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FireFoxTests)
unittest.TextTestRunner(verbosity=2).run(suite)