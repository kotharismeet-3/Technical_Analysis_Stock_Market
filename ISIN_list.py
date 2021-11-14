import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('http://stockcare.net/ISINNumber.asp')
driver.switch_to.frame(1)
table = driver.find_element_by_xpath('/html/body/form/table')
print(table.get_attribute('innerHTML'))

time.sleep(5)
driver.quit()
