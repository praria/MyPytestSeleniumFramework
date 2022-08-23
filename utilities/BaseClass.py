import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # specifying the file where the test msg to be printed. filehandler and logger are linked in this step
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filehandler.setFormatter(formatter)  # filehandler and Formatter are linked
        logger.addHandler(filehandler)  # this method takes in the filehandler object
        # test msg to be printed
        logger.setLevel(logging.DEBUG)  # we may set the hierrachial level where we want the report from. eg: warning
        return logger

    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 20)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectOptionByText(self, locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)