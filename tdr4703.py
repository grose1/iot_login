# This python script will log in to Geovision GV-TDR-4703 IP cameras and pull up the settings page.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

ip = input('Enter Camera IP:')
u = input('Enter username:')
p = input('Enter Password:')
http = 'http://'
driver = webdriver.Chrome('chromedriver.exe')

driver.get(http + ip)



frame = driver.find_element_by_css_selector('iframe')
driver.switch_to.frame(frame)

user = driver.find_element_by_id('userName')
password = driver.find_element_by_id('password')
user.clear()
user.send_keys(u)
password.clear()
password.send_keys(p)

password.send_keys(Keys.RETURN)
time.sleep(.5)


driver.find_element_by_id('nav_config').click()
