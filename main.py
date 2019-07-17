from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path='C:/Users/Prince/Downloads/chromedriver.exe')
print('oepning site in html')
driver.get("https://www.dukascopy.com/swiss/english/marketwatch/historical/")
print(driver.title)
driver.implicitly_wait(30)
btn=driver.find_element_by_id(':co')
btn.click()
# user=driver.find_element_by_xpath("//*[@id='email']")
# password=driver.find_element_by_xpath("//*[@id='pass']")
# sub=driver.find_element_by_css_selector("input[data-testid=royal_login_button]")

# print("user dis ",user.is_displayed())
# print("user ena ",user.is_enabled())
# print("pass dis ",password.is_displayed())
# print("pass ena ",password.is_enabled())

# user.send_keys("8864995682")
# password.send_keys("node8273120126")

# sub.click()
# driver.implicitly_wait(300)
# driver.find_element_by_css_selector("snap[class=_1vp5]").click()
# driver.find_element_by_xpath("//*[@id='login_form']/table/tbody/tr[3]/td[2]/div/a").click()
# driver.close()
# driver.quit()
