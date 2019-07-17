from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
driver=webdriver.Chrome(executable_path='C:/Users/Prince/Downloads/chromedriver.exe')
driver.get('http://www.xpedia.com')
driver.maximize_window()
driver.find_element_by_id('tab-flight-tab-hp').click()
btn1=driver.find_element_by_id('flight-origin-hp-flight')
driver.implicitly_wait(2)
btn1.send_keys("PAR")
btn2=driver.find_element_by_id('flight-destination-hp-flight')
driver.implicitly_wait(2)
btn2.send_keys("NYC")
driver.find_element_by_id('flight-departing-hp-flight').clear()
driver.find_element_by_id('flight-departing-hp-flight').send_keys("11/04/2019")
driver.find_element_by_id('flight-returning-hp-flight').clear()
driver.find_element_by_id('flight-returning-hp-flight').send_keys("11/04/2019")
print('cliking btn')
driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()
print('yeah testing neww page')
wait =WebDriverWait(driver,5)
element=wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='stops']/div/label[1]/div/div[1]")))
element.click()
print('everythin ok')