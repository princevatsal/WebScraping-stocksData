from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
import os,datetime,time
def findingdate():
	r=os.listdir('realdata')
	data=[]
	for i in range (len(r)):
		if(r[i][0:13]=='EURUSD_Ticks_'):
			data.append(r[i][13:23])
	for i in range(len(data)):
		temp=date(int(data[i][6:10]),int(data[i][3:5]),int(data[i][0:2]))
		data[i]=temp
	if(len(data)==0):
		big='empty'
	else:
		big=data[0]
		for i in range(len(data)):
			if(data[i]>big):
				big=data[i]
	if(big=='empty'):
		reqdate=date(2019,1,1)
	else:
		big+=datetime.timedelta(days=1)
		reqdate=big
	return(reqdate)
# driver=webdriver.Chrome(executable_path='C:/Users/Prince/Downloads/chromedriver.exe')
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : 'C:/Users/Prince/Desktop/my code goes here/selenium/realdata'}
chrome_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path='C:/Users/Prince/Downloads/chromedriver.exe',chrome_options=chrome_options)
print('getting page')
driver.get('https://www.dukascopy.com/swiss/english/marketwatch/historical/')
driver.implicitly_wait(7)
for q in range(365):
	d0=findingdate()
	if(d0==date(2019,3,1)):
		print('all file downloaded')
		break
	else:
		for i in range(10):
			try:
				d1=date(2019,3,11)
				delta=d1-d0
				print('waiting 15 second for eur/usd button to be loaded')
				wait =WebDriverWait(driver,15)
				element=wait.until(EC.element_to_be_clickable((By.ID,"main-center-col")))
				print('element found')
				print(element.get_attribute('innerHTML'))
				fr=element.find_element_by_tag_name('iframe')
				print('iframe found')
				driver.switch_to.frame(fr)
				htm=driver.find_element_by_css_selector('li[data-instrument="EUR/USD"]')
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
				for ia in range(delta.days):
					actions = ActionChains(driver)
					actions.send_keys(Keys.LEFT).perform()
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
		driver.refresh()
		time.sleep(10)
		
