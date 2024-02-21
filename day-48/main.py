from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.python.org/')
# price_dollar = driver.find_element(By.CLASS_NAME, value='a-price-whole')
# price_cents = driver.find_element(By.CLASS_NAME, value='a-price-fraction')
# # print(f'The price is {price_dollar.text}.{price_cents.text}')
# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute('placeholder'))
# button = driver.find_element(By.ID, value='submit')
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value='documentation-widget a')
# print(documentation_link.text)
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')

event_time = driver.find_elements(By.CSS_SELECTOR, value='.event-widget time')
event_name = driver.find_elements(By.CSS_SELECTOR, value='.event-widget li a')
events = {}
for n in range(len(event_time)):
    events[n] = {
        'time': event_time[n].text,
        'name': event_time[n].text,
    }
print(events)
print(bug_link.text)
driver.quit()
