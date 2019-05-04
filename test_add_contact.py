# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        # open homepage
        wd.get("http://localhost/addressbook/")
        # login
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        # open add new contact page
        wd.find_element_by_link_text("add new").click()
        # fill form name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Misha")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("MIO")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Ivanov")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("MIOBN")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("MR")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Comp")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Moscow")
        # fill form telephone
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("8495")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("8911")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("8812")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("84951")
        # fill form e-mail
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("er")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("qw")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("yu")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("rewti")
        # fill form bday
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("14")
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[16]").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("November")
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Birthday:'])[1]/following::option[45]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1986")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("18")
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[20]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("November")
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Anniversary:'])[1]/following::option[45]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1996")
        # fill form secondary
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("SPb")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("Nevskiy")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("none")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True


    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
