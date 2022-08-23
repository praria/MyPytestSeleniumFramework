import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.Homepage import Homepage
from utilities.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup") it is connection between setup fixture and test_ file
# Base class is inherited because it had a knowledge of fixtures


class TestOne(BaseClass):
    def test_end2end(self):
        # service_obj = Service("C:/Users/prari/Documents/Applications/chromedriver.exe")
        # driver = webdriver.Chrome(service=service_obj)
        # driver.implicitly_wait(4)
        # driver.get("https://www.rahulshettyacademy.com/angularpractice/")

        # regular expression in css selector-> a[href*='shop']  or xpath -> //a[contains(@href, 'shop')]
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

        log = self.getlogger()

        homepage = Homepage(self.driver)

        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        # checkoutPage = CheckoutPage(self.driver)

        checkoutPage = homepage.shop_items()
        productLists = checkoutPage.getProducts()

        log.info("getting the product lists")

        for product in productLists:
            productName = product.find_element(By.XPATH, 'div/h4/a').text
            log.info(productName)
            if productName == "Blackberry":
                product.find_element(By.XPATH, "//button[@class='btn btn-info']").click()

        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        # checkoutPage = CheckoutPage(self.driver)

        checkoutPage.clickCheckoutButton().click()

        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        # confirmPage = checkoutPage.clickNextCheckoutButton()

        # self.driver.find_element(By.ID, "country").send_keys("ind")
        # confirmPage = ConfirmPage(self.driver)

        log.info("entering the country name as ind")

        confirmPage = checkoutPage.clickNextCheckoutButton()
        confirmPage.deliveryLocation().send_keys("ind")

        # wait = WebDriverWait(self.driver, 20)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        log.info("success text message received ad "+successText)
        print(successText)
        assert "Success! Thank you!" in successText
