# This python script will log in to Infinias Access Control device and change the IP address
# DHCP must previously be turned off on controller for this to work.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Get IP and Log in info
ip = input('Enter Device IP:')
u = input('Enter username:')
p = input('Enter Password:')

# New IP Info
newip = input('Enter Change IP:')
sub = input('Enter Subnet Mask')
gate = input('Enter Gateway')


http = 'http://'
driver = webdriver.Chrome('chromedriver.exe')

driver.get(http + u + ":" + p + "@" + ip)

time.sleep(3)
frame = driver.find_element_by_name('Content')
driver.switch_to.frame(frame)

user = driver.find_element_by_id('txtUsername')
password = driver.find_element_by_id('txtPassword')
user.clear()
user.send_keys(u)
password.clear()
password.send_keys(p)

password.send_keys(Keys.RETURN)
time.sleep(5)

driver.find_element_by_id('cmdSystem').click()
time.sleep(.5)
driver.find_element_by_id('cmdControllers').click()
time.sleep(.5)
driver.find_element_by_id('cmdModify').click()
time.sleep(.5)

# Input New IP Address
chgip = driver.find_element_by_id('txtIPAddress')
chgip.clear()
chgip.send_keys(newip)

# Input New Subnet
subch = driver.find_element_by_id('txtSubnetMask')
subch.clear()
subch.send_keys(sub)

# Input new gateway
gatech = chgip = driver.find_element_by_id('txtGateway')
gatech.clear()
gatech.send_keys(gate)
time.sleep(3)

driver.find_element_by_id('cmdOK').click()

time.sleep(5)
driver.close()
