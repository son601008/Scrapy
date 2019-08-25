from time import sleep, time
from random import uniform, randint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
class Test:
	url='https://uid.danseo.net/index.php'
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("user-data-dir=/Users/Kazami Akatsuki/AppData/Local/Google/Chrome")
	def wait_between(a,b):
		rand=uniform(a, b) 
		sleep(rand)
	'''prefs = {"profile.default_content_setting_values.notifications": 2}
   	chrome_options.add_experimental_option("prefs", prefs)'''
	driver = webdriver.Chrome(executable_path='D:/Downloads/Compossed/chromedriver',chrome_options=chrome_options)
	#mainWin = driver.current_window_handle
	driver.get(url)
	driver.find_element_by_xpath('//textarea[@class="form-control"]').send_keys("100035215281538")
	driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
	#wait.until(EC.element_to_be_clickable((By.XPATH ,'//div[@class="recaptcha-checkbox-checkmark"]')))
	CheckBox = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID ,"recaptcha-anchor"))        
		) 
	wait_between(0.5, 0.7)
	CheckBox.click()
	#driver.switch_to_window(mainWin)  
	submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH ,'//input[@type="submit"]')) 
		)   
	submit.click() 