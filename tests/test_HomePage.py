import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.Homepage import Homepage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):
    def test_formSubmission(self, getData):
        log = self.getlogger()
        homePage = Homepage(self.driver)
        homePage.getName().send_keys(getData["fname"])
        homePage.getEmail().send_keys(getData["email"])
        log.info("the passwords is "+getData["pword"])
        homePage.getPassword().send_keys(getData["pword"])
        homePage.clickCheckbox().click()
        homePage.clickRadiobutton().click()
        self.selectOptionByText(homePage.selectGender(), getData["Gender"])
        # sel = Select(homePage.selectGender())
        # sel.select_by_index(0)
        # sel.select_by_visible_text("Female")
        homePage.clickSubmit().click()
        alertText = homePage.getSuccessMessage().text
        print(alertText)
        assert "Success" in alertText
        self.driver.refresh()

    # @pytest.fixture(params=[("Akchhay", "Khanha", "123456", "Male"), ("Twinkle", "Khanna", "654321", "Female")])
    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param

        # driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Rahul")
        # driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        # driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
        # self.driver.find_element(By.ID, "exampleCheck1").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
        # for the static dropdown menu, there shoul be a Select class
        # dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        # 3 various ways to select static drop down menu.
        # dropdown.select_by_value()
        # dropdown.select_by_index(0)
        # dropdown.select_by_visible_text("Female")

        # locators -> id, name, classname, xpath, cssselector, linkname
        # for xpath -> //tagname[@attribute = 'value']
        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        #message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        # print(message)
        # assert "Success" in message