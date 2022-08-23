from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    # self.driver.find_element(By.ID, "country").send_keys("ind")
    location = (By.ID, "country")

    def deliveryLocation(self):
        return self.driver.find_element(*ConfirmPage.location)

