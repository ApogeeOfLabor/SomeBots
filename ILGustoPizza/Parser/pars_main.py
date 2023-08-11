import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

link = 'https://ilgustopizza.uds.app/c/goods'

browser = uc.Chrome(headless=True)
root_dir = f'{os.path.dirname(__file__)}'

print(browser.find_element(By.CSS_SELECTOR, '[]'))
