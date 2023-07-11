import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path="C:\ChromeDriver-for-Selenium\chromedriver.exe")

driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(by=By.XPATH, value='//*[@id="articlecount"]/a[1]')
# article_count.click()

# print(article_count.text)

# all_portals = driver.find_element(by=By.LINK_TEXT, value="Content portals")
# all_portals.click()

search_icon = driver.find_element(by=By.CLASS_NAME, value="search-toggle")
search_icon.click()
time.sleep(1)
search_bar = driver.find_element(by=By.CLASS_NAME, value='cdx-text-input__input')
search_bar.send_keys("Python")
search_bar.send_keys(Keys.ENTER)
