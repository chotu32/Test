from _dummy_thread import error

import time
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class Selenium4TestingPage:

    # to enter user name
    def enterUserName(self, driver, Username):
        driver.find_element(By.XPATH, '//input[@name="username"]').send_keys(Username)

    # to enter password
    def enterPassword(self, driver, Password):
        driver.find_element(By.XPATH, '//input[@name="password"]').send_keys(Password)

    # to click on login button
    def clickOnLoginBtn(self, driver):
        driver.find_element(By.XPATH, '//input[@name="submit"]').click()

    # to click on Registration Link
    def clickOnRegistrationLink(self, driver):
        driver.find_element(By.XPATH, '//ul[@id="navigation"]/li[1]/a').click()

    # to select patient category
    def selectPatientCategory(selfself, driver, patientCategory):
        select = Select(driver.find_element_by_name('PATIENT_CAT'))
        select.select_by_visible_text(patientCategory)

    # to select title
    def selectTitle(selfself, driver, title):
        select = Select(driver.find_element_by_name('TITLE'))
        #select = Select(driver.find_element(By.XPATH, ("//select[@name='TITLE']")))
        select.select_by_visible_text(title)

    # to enter first name
    def enterFirstName(self, driver, firstName):
        driver.find_element(By.XPATH, '//input[@name="PNT_NAME"]').send_keys(firstName)

    # to enter last name
    def enterLastName(self, driver, lastName):
        driver.find_element(By.XPATH, '//input[@name="LAST_NAME"]').send_keys(lastName)

    # to enter date of birth
    def enterDateOfBirth(self, driver, dateOfBirth):
        driver.find_element(By.XPATH, '//input[@name="DOB"]').send_keys(dateOfBirth)

    # to enter age
    def enterAge(self, driver, age):
        driver.find_element(By.XPATH, '//input[@name="AGE"]').send_keys(age)

    # to select gender
    def selectGender(selfself, driver):
        select = Select(driver.find_element_by_name('SEX'))
        select.select_by_index('1')

    # to select marital status
    def selectMaritalStatus(selfself, driver):
        select = Select(driver.find_element_by_name('MTRL_STATUS'))
        select.select_by_index('1')

    # to select religion
    def selectReligion(selfself, driver, religion):
        select = Select(driver.find_element_by_name('RELIGION'))
        select.select_by_visible_text(religion)

    # to select Primary Language
    def selectPrimaryLanguage(selfself, driver):
        select = Select(driver.find_element_by_name('PLANGUAGE'))
        select.select_by_index('1')

    # to select relation
    def selectRelation(selfself, driver):
        select = Select(driver.find_element_by_name('RELATION'))
        select.select_by_index('1')

    # to select Patient Identifier
    def selectPatientIdentifier(selfself, driver):
        select = Select(driver.find_element_by_name('PAT_IDENTITY'))
        select.select_by_index('3')

    # to enter aadhar number
    def enterAadharNumber(selfself, driver, aadharNumber):
        driver.find_element(By.NAME, 'PAT_IDENTITY_PROOF').send_keys(aadharNumber)

    # to select Nationality
    def selectNationality(selfself, driver):
        select = Select(driver.find_element_by_name('NATIONALITY'))
        select.select_by_index('1')

    # to select VIP
    def selectVIP(selfself, driver):
        select = Select(driver.find_element_by_name('IS_MLC'))
        select.select_by_index('2')

    # to select Education
    def selectEducation(selfself, driver):
        select = Select(driver.find_element_by_name('EDUCATION'))
        select.select_by_index('2')

    # to select occupation
    def selectOccupation(selfself, driver):
        select = Select(driver.find_element_by_name('OCCUPATION'))
        select.select_by_index('1')

    # to select Blood Group
    def selectBloodGroup(selfself, driver):
        select = Select(driver.find_element_by_name('BLOOD_GRP_CODE'))
        select.select_by_index('1')

    # to select Citizenship
    def selectCitizenship(selfself, driver):
        select = Select(driver.find_element_by_name('CITIZENSHIP'))
        select.select_by_index('2')

    # to select Senior Citizen Proof Submited
    def selectSeniorCitizenProofSubmited(selfself, driver):
       select = Select(driver.find_element_by_name('SC_PROOF'))
       select.select_by_index('2')

    # to enter Address1
    def enterAddress1(selfself, driver, address1):
         driver.find_element(By.NAME, 'ADDRESS1').send_keys(address1)

    # to enter Phone Number
    def enterPhoneNumber(selfself, driver, phoneNumber):
        driver.find_element(By.NAME, 'MOBILE_NO').send_keys(phoneNumber)

    # to select country
    def selectCountry(self, driver):
        select = Select(driver.find_element_by_name('COUNTRY_CODE'))
        select.select_by_index('1')

    # to enter pin number
    def enterPinNumber(self, driver, pinNumber):
        driver.find_element(By.NAME, 'ZIP').send_keys(pinNumber)

    # to upload Image
    def uploadImage(self, driver, image):
        driver.find_element(By.NAME, 'image').send_keys(image)

    # to click on save button
    def clickOnSaveBtn(selfs, driver):
        driver.find_element(By.NAME, 'submit').click()

    # to get alert text
    def getAlertText(selfs, driver):
        #time.sleep(30)
        alert_obj = driver.switch_to.alert
        print("Alert Text : " + alert_obj.text)
        #time.sleep(30)
        alertText = alert_obj.text
        a,b,c,d,mr_no = alertText.split(" ")
        print("C : " + c)
        return mr_no,c

    # to click on alert ok button
    def clickOnAlertOkBtn(selfs, driver):
        alert_obj = driver.switch_to.alert
        #time.sleep(30)
        alert_obj.accept()

    # to navigate Search Registration
    def navigateToSearchRegistration(selfs, driver):
        driver.find_element(By.XPATH, '//ul[@id="navigation"]/li[1]/ul/li[3]/a').click()

    # to search patient details with MRN ID
    def searchWithMRNID(self, driver, mr_no):
        action = driver.find_element(By.NAME, 'search')
        action.send_keys(mr_no)
        action.send_keys(Keys.ENTER)
        time.sleep(3)


    # to get id from registration list
    def getPatientDataFromRegistrationList(self, driver):
        total_data = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/form/div/table[3]/tbody/tr').text
        print("Total Text : " + total_data)
        data = total_data.split(" ")
        #id = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/form/div/table[3]/tbody/tr/td[1]').text
        return data

    # to get MR number from registration list
    def getMRNoFromRegistrationList(self, driver):
        mrn = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/form/div/table[3]/tbody/tr/td[2]').text
        return mrn

    # to get MR number from registration list
    def getPNTNameFromRegistrationList(self, driver):
        pnt_name = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[2]/form/div/table[3]/tbody/tr/td[3]').text
        return pnt_name

    # to get MR number from registration list
    def getPNTAgeFromRegistrationList(self, driver):
        pnt_name = driver.find_element(By.XPATH,
                                           '/html/body/div[2]/div[1]/div[2]/form/div/table[3]/tbody/tr/td[4]').text
        return pnt_name
