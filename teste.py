import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from cache import cache

# Define URL

whtasapp = "https://web.whatsapp.com/"

# Open WebBrowser
s = Service('.\chromedriver.exe')  # webdriver path
driver = webdriver.Chrome(service=s, options=cache.options)


# Get URL
driver.get(whtasapp)
time.sleep(10)  # Sleep 10 seconds beacuse some times the load takes too long

# Search for groups
driver.find_element_by_xpath(
    '//div[@title="Search input textbox"]').send_keys(f'BNA - Empregos {b}')

time.sleep(2)

# Click on describe group
driver.find_element_by_xpath(
    f'//span[@title="BNA - Empregos {n} 🇺🇸🇧🇷 CA"]').click()
time.sleep(1)

# Open de group menu
driver.find_elements_by_xpath(
    f'//span[@title="BNA - Empregos {n} 🇺🇸🇧🇷 NY"]')[1].click()
time.sleep(1)

# Click on search icon in group menu
driver.find_elements_by_xpath('//span[@data-icon="search"]')[0].click()
time.sleep(1)

# Search for participant
driver.find_elements_by_xpath(
    '//div[@title="Search input textbox"]')[0].send_keys(f'{numero}')
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
time.sleep(5)


# Close the webdriver
driver.quit()
