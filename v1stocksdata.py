from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains
driver=webdriver.Chrome(executable_path='C:/Users/Prince/Downloads/chromedriver.exe')
print('getting page')
driver.get('https://www.dukascopy.com/swiss/english/marketwatch/historical/')
driver.implicitly_wait(7)
for i in range(10):
	try:
		print('waiting 15 second for eur/usd button to be loaded')
		wait =WebDriverWait(driver,15)
		element=wait.until(EC.element_to_be_clickable((By.ID,"main-center-col")))
		print('element found')
		print(element.get_attribute('innerHTML'))
		fr=element.find_element_by_tag_name('iframe')
		print('iframe found')
		driver.switch_to.frame(fr)
		htm=driver.find_element_by_id(':co')
		print('eur/usd found & selected')
		htm.click()
		print('finding date')
		date=driver.find_elements_by_class_name('a-ab-v-y-x')[5]
		print('date founded')
		datespan=date.find_element_by_tag_name('span')
		print('snap founded')
		datespan2=datespan.find_element_by_tag_name('span')
		print('snap2 founded')
		datespan2.click()
		print('cal opened')
		actions = ActionChains(driver)
		actions.send_keys(Keys.DOWN).perform()
		print('date changed')
		driver.find_element_by_class_name('d-wh-vg-Tg').click()
		print('download btn clicked')
		driver.find_element_by_css_selector('input[placeholder="Nickname or email"]').send_keys("princevatsalq@gmail.com")
		print('username input filled')
		driver.find_element_by_css_selector('input[type="password"]').send_keys("8273120126aA")
		print('password filled yeahh!')
		driver.find_element_by_class_name('d-e-v').click()
		print('file ready')
		wait2=WebDriverWait(driver,180)
		download=wait2.until(EC.element_to_be_clickable((By.CLASS_NAME,"a-ab-v-y-x")))
		download.click()
		break
	except Exception as e:
		print(str(e))
		print('refreshing '+str(i+1)+' times')
		driver.refresh()
		driver.implicitly_wait(7)
		print('error')
		
