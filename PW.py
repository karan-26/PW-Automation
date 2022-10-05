from ast import Bytes
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import time

#option1= Options()
#option1.add_argument("--disable-notifications")

driver=webdriver.Firefox(executable_path="D:\Selenium browser drivers\geckodriver-v0.31.0-win64\geckodriver.exe")
#driver=webdriver.Chrome(executable_path="D:\Selenium browser drivers\chromedriver_win32\chromedriver.exe",chrome_options=option1)
driver.get("https://stage.physicswallah.live/study/auth")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[1]/div/a").click()
time.sleep(1)
driver.find_element(By.ID, "pno_ipt" ).click()
time.sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='Enter Mobile No.']").send_keys("8090237900")
time.sleep(2)
driver.find_element(By.ID, "otp_btn-1").click()
time.sleep(2)
driver.find_element(By.ID, "ngx-otp-input-0").send_keys("1")
time.sleep(1)
driver.find_element(By.ID, "ngx-otp-input-1").send_keys("2")
time.sleep(1)
driver.find_element(By.ID, "ngx-otp-input-2").send_keys("3")
time.sleep(1)
driver.find_element(By.ID, "ngx-otp-input-3").send_keys("4")
time.sleep(1)
driver.find_element(By.ID, "ngx-otp-input-4").send_keys("5")
time.sleep(1)
driver.find_element(By.ID, "ngx-otp-input-5").send_keys("6")
time.sleep(2)
driver.find_element(By.ID,  "cont_btn").click()
time.sleep(3)
driver.find_element(By.ID)


#options = webdriver.FirefoxOptions()
#options.set_preference("dom.push.enabled", True)
#browser = webdriver.Firefox(firefox_options=options)    

#_browser_profile = webdriver.FirefoxProfile()
#_browser_profile.set_preference("dom.webnotifications.enabled", False)
#webdriver.Firefox(firefox_profile=_browser_profile)

driver.find_element(By.ID,"side-nav_btn-4").click()


driver.quit
