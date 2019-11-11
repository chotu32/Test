import time

import pyautogui as pyautogui

import unittest

from logger import logger

from pageclasses.Selenium4TestingPage import Selenium4TestingPage
from utilities.BaseClass import BaseClass
from utilities.ConfigUtility import ConfigUtility


class Registrationtest(unittest.TestCase):
    global config
    config = ConfigUtility()

    def test_registration(self):
        objSeleniumPage = Selenium4TestingPage()
        base = BaseClass()
        webdriver = base.setUp()
        objSeleniumPage.enterUserName(webdriver, config.test_config("Username"))
        objSeleniumPage.enterPassword(webdriver, config.test_config("Password"))
        objSeleniumPage.clickOnLoginBtn(webdriver)
        objSeleniumPage.clickOnRegistrationLink(webdriver)
        objSeleniumPage.selectPatientCategory(webdriver, config.test_config("patientCategory"))
        objSeleniumPage.selectTitle(webdriver, config.test_config("title"))
        objSeleniumPage.enterFirstName(webdriver, config.test_config("firstName"))
        objSeleniumPage.enterLastName(webdriver, config.test_config("lastName"))
        objSeleniumPage.enterDateOfBirth(webdriver, config.test_config("dateOfBirth"))
        objSeleniumPage.enterAge(webdriver, config.test_config("age"))
        objSeleniumPage.selectGender(webdriver)
        objSeleniumPage.selectMaritalStatus(webdriver)
        objSeleniumPage.selectReligion(webdriver, config.test_config("religion"))
        objSeleniumPage.selectPrimaryLanguage(webdriver)
        objSeleniumPage.selectRelation(webdriver)
        objSeleniumPage.selectPatientIdentifier(webdriver)
        objSeleniumPage.enterAadharNumber(webdriver, config.test_config("aadharNumber"))
        objSeleniumPage.selectNationality(webdriver)
        objSeleniumPage.selectVIP(webdriver)
        objSeleniumPage.selectEducation(webdriver)
        objSeleniumPage.selectOccupation(webdriver)
        objSeleniumPage.selectBloodGroup(webdriver)
        objSeleniumPage.selectCitizenship(webdriver)
        objSeleniumPage.selectSeniorCitizenProofSubmited(webdriver)
        objSeleniumPage.enterAddress1(webdriver, config.test_config("address1"))
        objSeleniumPage.enterPhoneNumber(webdriver, config.test_config("phoneNumber"))
        objSeleniumPage.selectCountry(webdriver)
        objSeleniumPage.enterPinNumber(webdriver, config.test_config("pinNumber"))
        objSeleniumPage.uploadImage(webdriver, config.test_config("image"))
        objSeleniumPage.clickOnSaveBtn(webdriver)
        mr_no, success = objSeleniumPage.getAlertText(webdriver)
        if success == 'Successfully.':
            logger.info("Registration form submitted successfully")
        else:
            logger.info("Registration form not submitted")
        print("\n" + "MR_NO : " + mr_no )
        objSeleniumPage.clickOnAlertOkBtn(webdriver)
        objSeleniumPage.navigateToSearchRegistration(webdriver)
        objSeleniumPage.searchWithMRNID(webdriver, mr_no)
        base.take_screenshot('Patient Details')
        data = []
        data = objSeleniumPage.getPatientDataFromRegistrationList(webdriver)
        logger.info("ID_NO : " + data[0])
        logger.info("MR_NO : " + data[1])
        logger.info("PNT_NAME : " + data[2])
        logger.info("Age : " + data[3])
        logger.info("REG_DATE : " + data[4])
        #print("EMAIL : " + )
        logger.info("ADDRESS : " + data[5])
        logger.info("BLOOD_GROUP : " + data[6])
        logger.info("STATUS : " + data[7])
