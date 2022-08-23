from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")

    # tuples or objects  for test_HomePage
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    radiobutton = (By.CSS_SELECTOR, "#inlineRadio1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successMessage = (By.CLASS_NAME, "alert-success")

    def shop_items(self):
        self.driver.find_element(*Homepage.shop).click()
        checkoutPage = CheckoutPage(self.driver)
        return checkoutPage

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getPassword(self):
        return self.driver.find_element(*Homepage.password)

    def clickCheckbox(self):
        return self.driver.find_element(*Homepage.checkbox)

    def clickRadiobutton(self):
        return self.driver.find_element(*Homepage.radiobutton)

    def selectGender(self):
        return self.driver.find_element(*Homepage.gender)

    def clickSubmit(self):
        return self.driver.find_element(*Homepage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*Homepage.successMessage)




        # asterisk * is used in order to read tuple
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
