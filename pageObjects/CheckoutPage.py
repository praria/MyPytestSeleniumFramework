from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    products = (By.XPATH, "//div[@class='card h-100']")

    # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    nextCheckoutButton = (By.XPATH, "//button[@class='btn btn-success']" )

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def clickCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkoutButton)

    def clickNextCheckoutButton(self):
        self.driver.find_element(*CheckoutPage.nextCheckoutButton).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage




