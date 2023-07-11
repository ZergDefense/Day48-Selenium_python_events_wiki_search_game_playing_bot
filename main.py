from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="C:\ChromeDriver-for-Selenium\chromedriver.exe")

driver = webdriver.Chrome(service=service)


# driver.get("https://mstore.hu/xiaomi-smart-air-purifier-4-lite-okos-legtisztito-bhr5274gl-2507?keyword=Purifier")
# price = driver.find_element(by=By.XPATH, value='//*[@id="product"]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/span')
# print(price.text)

# Find some other stuff, just as example:
# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(by=By.CLASS_NAME, value="python-logo")
# print(logo.size)
#
# documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

def find_python_events():
    driver.get("http://www.python.org/")

    events = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")
    for event in events:
        print(event.text)

    dates = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li time")
    for date in dates:
        print(date.get_attribute("datetime").split("T")[0])

    events_dict = {}
    for index in range(len(events)):
        events_dict[index] = {
            'time': dates[index].get_attribute("datetime").split("T")[0],
            'name': events[index].text
        }

    print(events_dict)


find_python_events()
