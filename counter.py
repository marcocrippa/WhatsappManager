import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from cache import cache

# Define variables

whtasapp = "https://web.whatsapp.com/"

states = ['CA', 'FL', 'MA', 'NY']

nincho = ['Empregos', 'Apartments', 'Carros', 'Delivery',
          'Doação', 'Mercadão', 'Seguros', 'Comidas BR']

a = []


# Open WebBrowser
s = Service('.\chromedriver.exe')  # webdriver path
driver = webdriver.Chrome(service=s, options=cache.options)


# Get URL
driver.get(whtasapp)
time.sleep(20)  # Sleep 20 seconds beacuse some times the load takes too long

# Count the members of all groups
for s in states:
    for i in nincho:
        for n in range(1, 4):

            # Search for group
            driver.find_element_by_xpath(
                '//div[@title="Search input textbox"]').send_keys(f'BNA - {i} {n}')
            time.sleep(2)

            try:
                # Click on describe group
                driver.find_element_by_xpath(
                    f'//span[@title="BNA - {i} {n} 🇺🇸🇧🇷 {s}"]').click()
                time.sleep(2.5)

            except:
                # Clear the search input text
                driver.find_element_by_xpath(
                    '//div[@title="Search input textbox"]').clear()
                time.sleep(1.5)

            else:
                # Get the content above the name of the group = all numbers in the group
                a = a + driver.find_element_by_xpath(
                    '//*[@id="main"]/header/div[2]/div[2]/span').get_attribute("title").split(', ')
                time.sleep(1.5)

                # Clear the search input text
                driver.find_element_by_xpath(
                    '//div[@title="Search input textbox"]').clear()
                time.sleep(1.5)

printf(f'Total number in groups: {len(a)}')
print('')
print('###########################################################/////////////////////////////////////////////////////########################################################')
print('')
print(f'Unique number in groups: {len(set(a))}')
