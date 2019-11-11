import os
import time
from datetime import datetime
from os.path import dirname

import pyautogui
from selenium import webdriver
from utilities.ConfigUtility import ConfigUtility


class BaseClass():
    global config
    config = ConfigUtility()
    global project_root
    projectpath = dirname(dirname(__file__))
    global chromedriverpath
    global screenshotpath
    global final_directory
    global tf
    print(projectpath)
    chromedriverpath = os.path.join(projectpath, "Resources", "chromedriver.exe")
    current_directory = os.getcwd()
    final_directory = os.path.join(projectpath, r'screenshot')
    print("Final directory path : " + final_directory)
    print("Chrome driver path : " + chromedriverpath)
    print("Project path : " + projectpath + "\n")
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    tf = time.mktime(time.gmtime())

    # for launch browser
    def setUp(self):
        driver = webdriver.Chrome(chromedriverpath)
        driver.maximize_window()
        driver.get(config.test_config("url"))
        return driver

    # to take screenshot
    def take_screenshot(self, screenshotName):
        pic = pyautogui.screenshot()
        print(final_directory + '\\' + screenshotName + str(tf) + '.png')
        pic.save(final_directory + '\\' + screenshotName + str(tf) + '.png')