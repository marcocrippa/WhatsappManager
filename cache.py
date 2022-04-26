import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Define URL

whtasapp = "https://web.whatsapp.com/"

# Save Profile - Cookies
dir_path = os.getcwd()
profile = os.path.join(dir_path, "profile", "wpp")
options = webdriver.ChromeOptions()
options.add_argument(
    r"user-data-dir={}".format(profile))

# Open WebBrowser
s = Service('.\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)


# Get URL
driver.get(whtasapp)
time.sleep(10)

# Search for groups
driver.find_element_by_xpath(
    '//div[@title="Search input textbox"]').send_keys('BNA - Empregos 1')

time.sleep(2)

# Click on describe group
driver.find_element_by_xpath(
    '//span[@title="BNA - Empregos 1 🇺🇸🇧🇷 NY"]').click()
time.sleep(1)

# Open de group menu
driver.find_elements_by_xpath(
    '//span[@title="BNA - Empregos 1 🇺🇸🇧🇷 NY"]')[1].click()
time.sleep(1)

# Click on search icon in group menu
driver.find_elements_by_xpath('//span[@data-icon="search"]')[0].click()
time.sleep(1)

# Search for participants
driver.find_elements_by_xpath(
    '//div[@title="Search input textbox"]')[0].send_keys('1 850 631 5')
time.sleep(1)

# Click on the frist number on menu
driver.find_elements_by_xpath('//div[@tabindex="0"]')[0].click()
time.sleep(1)

# Remove the number of the group
driver.find_element_by_xpath('//div[@aria-label="Remove"]').click()
time.sleep(1)

# Close the Search Participants
driver.find_element_by_xpath('//span[@data-testid="x"]').click()
time.sleep(1)

# Close the Group menu
driver.find_element_by_xpath('//span[@data-testid="x"]').click()
