import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from cache import cache

# Define variables

whtasapp = "https://web.whatsapp.com/"

numero = str(input('Digite o numero para ser removido: '))

states = ['CA', 'FL', 'MA', 'NY']

nincho = ['Empregos', 'Apartments', 'Carros', 'Delivery',
          'Doação', 'Mercadão', 'Seguros', 'Comidas BR']

# Open WebBrowser
s = Service('.\chromedriver.exe')  # webdriver path
driver = webdriver.Chrome(service=s, options=cache.options)


# Get URL
driver.get(whtasapp)
time.sleep(20)  # Sleep 20 seconds beacuse some times the load takes too long

# Search for a number inside all groups

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
                time.sleep(1.5)

            except:
                # Clear the search input text
                driver.find_element_by_xpath(
                    '//div[@title="Search input textbox"]').clear()
                time.sleep(2)

            else:
                # Open de group menu
                driver.find_elements_by_xpath(
                    f'//span[@title="BNA - {i} {n} 🇺🇸🇧🇷 {s}"]')[1].click()
                time.sleep(1.5)

                # Click on search icon in group menu
                driver.find_elements_by_xpath(
                    '//span[@data-icon="search"]')[0].click()
                time.sleep(1.5)

                # Search for participant
                driver.find_elements_by_xpath(
                    '//div[@title="Search input textbox"]')[0].send_keys(f'{numero}')
                time.sleep(1.5)

                try:
                    # Click on the frist number on menu
                    driver.find_elements_by_xpath(
                        '//div[@tabindex="0"]')[0].click()
                    time.sleep(1.5)

                except:
                    # Close the Search Participants
                    driver.find_element_by_xpath(
                        '//span[@data-testid="x"]').click()
                    time.sleep(1.5)

                    # Clear the search input text
                    driver.find_element_by_xpath(
                        '//div[@title="Search input textbox"]').clear()
                    time.sleep(1.5)

                else:
                    # Remove the number of the group
                    driver.find_element_by_xpath(
                        '//div[@aria-label="Remove"]').click()
                    time.sleep(1.5)

                    # Close the Search Participants
                    driver.find_element_by_xpath(
                        '//span[@data-testid="x"]').click()
                    time.sleep(1.5)

                    # Close the Group menu
                    driver.find_element_by_xpath(
                        '//span[@data-testid="x"]').click()
                    time.sleep(1.5)

                    # Clear the search input text
                    driver.find_element_by_xpath(
                        '//div[@title="Search input textbox"]').clear()
                    time.sleep(1.5)

driver.quit()
