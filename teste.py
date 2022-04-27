import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from cache import cache

# Define variables

whtasapp = "https://web.whatsapp.com/"


# Open WebBrowser
s = Service('.\chromedriver.exe')  # webdriver path
driver = webdriver.Chrome(service=s, options=cache.options)


# Get URL11951569460
driver.get(whtasapp)
time.sleep(20)  # Sleep 20 seconds beacuse some times the load takes too long

# Search for a number inside all groups
