import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver.exe')                                                #1 Launch Gmail page
base_url = 'https://www.gmail.com'
driver.get(base_url)
driver.maximize_window()


login_user = "testmail7956@gmail.com"                 #User's Information
password_user = "Test1_23"
invalid_password = "Test1_2"
empty_password = ""
us_first_name = "test"
us_second_name = "51"


login_field = driver.find_element(By.XPATH, "//*[@id='identifierId']")                    #2 Enter Email
login_field.send_keys(login_user)
time.sleep(1)
print("Input Login")

button_next1 = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span")
button_next1.click()
time.sleep(1)
print("Button Next Is Clicked")
time.sleep(3)



password_field = driver.find_element(By.XPATH, "//input[@type='password']")              #3.1 Enter Correct Password
password_field.send_keys(password_user)
print("Input Password")
time.sleep(1)

show_password = driver.find_element(By.XPATH, "//div[@class='d3GVvd jGAaxb']")
show_password.click()
print("Show Password")
time.sleep(1)

button_next2 = driver.find_element(By.XPATH, "//*[@id='passwordNext']")
button_next2.click()
time.sleep(1)
print("Button Next Is Clicked")

time.sleep(6)
print("Page Is Closed")
driver.quit()



driver = webdriver.Chrome('chromedriver.exe')                                         #3.2 Enter Incorrect Password
base_url = 'https://www.gmail.com'
driver.get(base_url)
driver.maximize_window()

login_field = driver.find_element(By.XPATH, "//*[@id='identifierId']")
login_field.send_keys(login_user)
time.sleep(1)
print("Input Login")

button_next1 = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span")
button_next1.click()
time.sleep(1)
print("Button Next is Clicked")
time.sleep(3)

password_field = driver.find_element(By.XPATH, "//input[@type='password']")
password_field.send_keys(invalid_password)
time.sleep(1)
print("Input Invalid Password")

show_password = driver.find_element(By.XPATH, "//div[@class='d3GVvd jGAaxb']")
show_password.click()
print("Show Password")
time.sleep(1)

button_next2 = driver.find_element(By.XPATH, "//*[@id='passwordNext']")
button_next2.click()
time.sleep(2)
print("Button Next Is Clicked")

time.sleep(3)
print("Page Is Closed")
driver.quit()



driver = webdriver.Chrome('chromedriver.exe')                                             #3.3 Enter Empty Password
base_url = 'https://www.gmail.com'
driver.get(base_url)
driver.maximize_window()

login_field = driver.find_element(By.XPATH, "//*[@id='identifierId']")
login_field.send_keys(login_user)
time.sleep(1)
print("Input Login")

button_next1 = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span")
button_next1.click()
time.sleep(1)
print("Button Next Is Clicked")
time.sleep(3)

password_field = driver.find_element(By.XPATH, "//input[@type='password']")
password_field.send_keys(empty_password)
time.sleep(1)
print("Input Empty Password")

show_password = driver.find_element(By.XPATH, "//div[@class='d3GVvd jGAaxb']")
show_password.click()
print("Show Password")
time.sleep(1)

button_next2 = driver.find_element(By.XPATH, "//*[@id='passwordNext']")
button_next2.click()
time.sleep(1)
print("Button Next Is Clicked")

time.sleep(3)
print("Page Is Closed")
driver.quit()



driver = webdriver.Chrome('chromedriver.exe')                                              #4 Forgot Email
base_url = 'https://www.gmail.com'
driver.get(base_url)
driver.maximize_window()

button_next1 = driver.find_element(By.XPATH, "//button[@type='button']")
button_next1.click()
print("Forgot Email Button Is Clicked")
time.sleep(1)

find_email = driver.find_element(By.XPATH, "//input[@type='email']")
find_email.send_keys(login_user)
print("Input Second Login")
time.sleep(1)

recover_button_next = driver.find_element(By.XPATH, "//span[@class='VfPpkd-vQzf8d']")
recover_button_next.click()
print("Button Next Is Clicked")
time.sleep(1)

first_name_field = driver.find_element(By.XPATH, "//input[@name='firstName']")
first_name_field.send_keys(us_first_name)
print("First Name Filled")
time.sleep(1)

second_name_field = driver.find_element(By.XPATH, "//input[@name='lastName']")
second_name_field.send_keys(us_second_name)
print("Last Name Filled")
time.sleep(1)

find_name_button = driver.find_element(By.XPATH, "//span[@class='VfPpkd-vQzf8d']")
find_name_button.click()
print("Button Next Is Clicked")
time.sleep(3)
print("Page Is Closed")
driver.quit()



driver = webdriver.Chrome('chromedriver.exe')                                                #5 Forgot Password
base_url = 'https://www.gmail.com'
driver.get(base_url)
driver.maximize_window()


login_field = driver.find_element(By.XPATH, "//*[@id='identifierId']")
login_field.send_keys(login_user)
print("Input Login")
time.sleep(1)

button_next1 = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span")
button_next1.click()
time.sleep(1)
print("Button Next Is Clicked")
time.sleep(3)

recover_field = driver.find_element(By.XPATH, "//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 uRo0Xe TrZEUc lw1w4b']")
recover_field.click()
print("Forgot Password Button Clicked")
time.sleep(3)
driver.quit()





































