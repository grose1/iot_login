from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

ip = input('Enter URL:')
u = input('Enter username:')
p = input('Enter Password:')
http = 'https://'
driver = webdriver.Chrome('chromedriver.exe')

driver.get(http + ip)

user = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')


user.clear()
user.send_keys(u)
password.clear()
password.send_keys(p)

password.send_keys(Keys.RETURN)
time.sleep(3)
driver.find_element_by_css_selector('ul.navbar-nav:nth-child(1) > li:nth-child(2) > a:nth-child(1)').click()
time.sleep(3)
driver.find_element_by_css_selector('li.sidebar-list:nth-child(2) > a:nth-child(1)').click()

