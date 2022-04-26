import time


def remover:

    numero = str(input('Digite o numero para ser removido'))
    states = ['CA', 'FL', 'MA', 'NY']

    for s in states:
        for n in range(1, 4):
            # Search for groups
            driver.find_element_by_xpath(
                '//div[@title="Search input textbox"]').send_keys(f'BNA - Empregos {n} 🇺🇸🇧🇷 {s}')
            time.sleep(2)

            # Click on describe group
            driver.find_element_by_xpath(
                f'//span[@title="BNA - Empregos {n} 🇺🇸🇧🇷 {s}"]').click()
            time.sleep(1)

            # Open de group menu
            driver.find_elements_by_xpath(
                f'//span[@title="BNA - Empregos {n} 🇺🇸🇧🇷 {s}"]')[1].click()
            time.sleep(1)

            # Click on search icon in group menu
            driver.find_elements_by_xpath(
                '//span[@data-icon="search"]')[0].click()
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
