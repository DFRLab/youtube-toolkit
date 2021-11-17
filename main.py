# -*- coding: utf-8 -*-

# import modules
import time
import argparse

# import submodules
from configparser import ConfigParser

# reading config file
config = ConfigParser()
config.read('./config/config.ini')

# arguments
parser = argparse.ArgumentParser(description='Arguments.')

# import Selenium modules
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import \
	DesiredCapabilities

# exceptions
from urllib3.exceptions import NewConnectionError, MaxRetryError

# import utils
from utils import preparing_driver, sign_in_process

# display options
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('-private-window')

# profile
profile_path = config['Firefox Profile']['profile']
profile = webdriver.FirefoxProfile(profile_path)

# preferences in Firefox browsers
profile.set_preference('dom.webdriver.enabled', False)
profile.set_preference('useAutomationExtension', False)
profile.update_preferences()

# desired capabilities
desired = DesiredCapabilities.FIREFOX

# get driver
driver = webdriver.Firefox(
	executable_path='./driver/geckodriver.exe',
	firefox_profile=profile,
	options=firefox_options,
	desired_capabilities=desired
)

# maximize window
driver.maximize_window()

# get url
url = 'https://www.youtube.com/'
driver.get(url)

# preparing driver
preparing_driver()

# get access to Google's account manually
sign_in_process()


# Closing driver
time.sleep(15)
driver.close()
