from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')

# number_link = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# number_link.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, value='Content portals')
# # all_portals.click()
#
# search = driver.find_element(By.NAME, value='search')
# search.send_keys('Python', Keys.ENTER)

first_name = driver.find_element(By.NAME, value='fName')
second_name = driver.find_element(By.NAME, value='lName')
email= driver.find_element(By.NAME, value='email')

first_name.send_keys('Ian')
second_name.send_keys('Mahia')
email.send_keys('ian@gmail.com')

submit = driver.find_element(By.CSS_SELECTOR, value='form button')
submit.click()