# 1.Go to Facebook
# Enter username & password
# Wait for login button to be clickable
# Click login
# Validate login success
# -----------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.facebook.com")
#
# driver.find_element('xpath', '//input[@name="email"]').send_keys("email")
# driver.find_element('xpath','//input[@name="pass"]').send_keys("password")
#
# login_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable(('xpath', '(//span)[3]'))
# )
# login_btn.click()
#
#
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located(('xpath', '//label'))
# )

# -----------------------------------------------------------
#
# 2.Go to myntra
# search for puma
# select any option from the auto-suggestions and click on it
# select the product(will open in new tab)
# handle the new tab
# add product to cart
# -----------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.maximize_window()
#
# driver.get("https://www.myntra.com")
# time.sleep(5)
#
# wait = WebDriverWait(driver, 10)
# search_box = wait.until(EC.presence_of_element_located(('xpath', '//input[@placeholder="Search for products, brands and more"]')))
# search_box.send_keys("puma")
#
#
# suggestion = wait.until(EC.presence_of_element_located(
#     ('xpath', '//li[contains(@class,"desktop-suggestion")][2]')
# ))
# suggestion.click()
#
# product = wait.until(EC.presence_of_element_located(
#     ('xpath', '(//li[@class="product-base"])[1]')
# ))
# product.click()
#
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
#
# add_to_bag = wait.until(EC.element_to_be_clickable(
#     ('xpath', '//div[text()="ADD TO BAG"]')
# ))
# time.sleep(5)
# add_to_bag.click()
#
# print("Product added to cart successfully!")
# -----------------------------------------------------------
#
# 3.Go to https://www.icici.bank.in/
# click on accounts
# click on apply(opens in new tab, handle it)
# enter the details(fake data)
# click on apply now
# validate unsuccessfull message
# -----------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=opts)
#
# driver.get("https://www.icicibank.com/")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 15)
#
#
# accounts = wait.until(
#     EC.visibility_of_element_located(('xpath', '//span[text()="Accounts"]'))
# )
#
# ActionChains(driver).move_to_element(accounts).perform()
#
# apply_btn = wait.until(
#     EC.element_to_be_clickable(('xpath', '(//a[contains(text(),"APPLY*")])[2]'))
# )
# apply_btn.click()
#
#
# windows = driver.window_handles
# driver.switch_to.window(windows[1])
#
#
# wait.until(EC.visibility_of_element_located(("name", "fullName"))).send_keys("Test User")
# driver.find_element("name", "mobileNumber").send_keys("9999999999")
# driver.find_element("name", "email").send_keys("test@gmail.com")
#
#
# # driver.find_element(By.NAME, "city").send_keys("Mumbai")
#
#
# driver.find_element('xpath', "//button[contains(text(),'Apply')]").click()
#
#
# error_msg = wait.until(
#     EC.visibility_of_element_located(('xpath', "//*[contains(text(),'invalid') or contains(text(),'error')]"))
# )
#
# print("Validation Message:", error_msg.text)

# -----------------------------------------------------------
#
# 4.Go to https://www.netmeds.com/
# hover to medicines using ActionChains
# click on order online
# Go to order using prescription
# upload some text file using file upload popup
# -----------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://www.netmeds.com")
#
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 10)
#
#
# medicines_menu = wait.until(
#     EC.presence_of_element_located(('xpath', '//a[contains(text(),"Medicines")]'))
# )
#
# actions = ActionChains(driver)
# actions.move_to_element(medicines_menu).perform()
#
#
# order_online = wait.until(
#     EC.element_to_be_clickable(('xpath', '//a[contains(text(),"Order Online")]'))
# )
# order_online.click()
#
#
# prescription = wait.until(
#     EC.element_to_be_clickable(('xpath', '//a[contains(text(),"Order with Prescription")]'))
# )
# prescription.click()
#
#
# upload = wait.until(
#     EC.presence_of_element_located(('xpath', '//input[@type="file"]'))
# )
#
#
# upload.send_keys("C:\\Users\\YourName\\Desktop\\testfile.txt")


# -----------------------------------------------------------
#
# 5.Go to https://www.netmeds.com/
# click on signin
# enter your valid mobile number
# click get otp
# enter the otp and validate the succesfull login
# -----------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://www.netmeds.com")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 15)
#
#
# signin_btn = wait.until(
#     EC.element_to_be_clickable(("xpath", "//span[contains(text(),'Sign in')]"))
# )
# signin_btn.click()
#
#
# mobile_input = wait.until(
#     EC.presence_of_element_located(("xpath", "//input[@type='tel']"))
# )
# mobile_input.send_keys("9999999999")  # replace with valid number
#
#
# get_otp = wait.until(
#     EC.element_to_be_clickable(("xpath", "//button[contains(text(),'Get OTP')]"))
# )
# get_otp.click()
#
#
# otp = input("Enter OTP: ")
#
# otp_input = wait.until(
#     EC.presence_of_element_located(("xpath", "//input[@type='number']"))
# )
# otp_input.send_keys(otp)
#
#
# verify_btn = wait.until(
#     EC.element_to_be_clickable(("xpath", "//button[contains(text(),'Verify')]"))
# )
# verify_btn.click()
#
#
# wait.until(
#     EC.presence_of_element_located(("xpath", "//span[contains(text(),'My Account')]"))
# )
#
# print("Login Successful!")

# -----------------------------------------------------------
#
# 6.Go to https://www.irctc.co.in/nget/train-search
# enter from, to, select the date, handle the dropdowns and click on search trains
# try to book a train
# -----------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://www.irctc.co.in/nget/train-search")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 15)
#
#
# try:
#     wait.until(EC.element_to_be_clickable(('xpath', '//button[@class="btn btn-primary"]'))).click()
# except:
#     pass
#
# from_station = wait.until(
#     EC.presence_of_element_located(('xpath', '//input[@placeholder="From*"]'))
# )
# from_station.send_keys("Delhi")
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//span[contains(text(),"DELHI")]'))
# ).click()
#
# to_station = wait.until(
#     EC.presence_of_element_located(('xpath', '//input[@placeholder="To*"]'))
# )
# to_station.send_keys("Mumbai")
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//span[contains(text(),"MUMBAI")]'))
# ).click()
#
# date_box = wait.until(
#     EC.element_to_be_clickable(('xpath', '//input[@placeholder="Journey Date(dd-mm-yyyy)*"]'))
# )
# date_box.clear()
# date_box.send_keys("25-03-2026")
#
# search_btn = wait.until(
#     EC.element_to_be_clickable(('xpath', '//button[contains(text(),"Search")]'))
# )
# search_btn.click()
#
# book_btn = wait.until(
#     EC.element_to_be_clickable(('xpath', '(//button[contains(text(),"Book Now")])[1]'))
# )
# book_btn.click()
#
# print("Train search and booking step executed")

# -----------------------------------------------------------
#
# 7.Go to https://www.purplle.com/
# hover to brands
# search for lakme and click on it
# scroll until the first item is visible
# click on first product
# Enter pincode and check if it is available
# -----------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get("https://www.purplle.com/")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 15)
# actions = ActionChains(driver)
#
#
# brands_menu = wait.until(
#     EC.presence_of_element_located(('xpath', '//a[contains(text(),"Brands")]'))
# )
# actions.move_to_element(brands_menu).perform()
#
#
# search_box = wait.until(
#     EC.presence_of_element_located(('xpath', '//input[@placeholder="Search Brands"]'))
# )
# search_box.send_keys("lakme")
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//a[contains(text(),"Lakme")]'))
# ).click()
#
# first_product = wait.until(
#     EC.presence_of_element_located(('xpath', '(//div[contains(@class,"product")])[1]'))
# )
#
# driver.execute_script("arguments[0].scrollIntoView();", first_product)
#
#
# first_product.click()
#
#
# pincode_box = wait.until(
#     EC.presence_of_element_located(('xpath', '//input[@placeholder="Enter Pincode"]'))
# )
# pincode_box._

# -----------------------------------------------------------
#
# 8.Go to https://lifeinsurance.adityabirlacapital.com/
# click on her insurance
# enter the data using data driven testing
# -----------------------------------------------------------
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# data = pd.read_csv("data.csv")
#
# driver = webdriver.Chrome()
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 15)
#
# for i in data.index:
#
#     driver.get("https://lifeinsurance.adityabirlacapital.com/")
#
#
#     wait.until(
#         EC.element_to_be_clickable(('xpath', '//span[contains(text(),"Her Insurance")]'))
#     ).click()
#
#
#     wait.until(
#         EC.presence_of_element_located(('xpath', '//input[@name="name"]'))
#     ).send_keys(data["name"][i])
#
#
#     driver.find_element('xpath', '//input[@type="tel"]').send_keys(str(data["phone"][i]))
#
#
#     driver.find_element('xpath', '//input[@type="email"]').send_keys(data["email"][i])
#
#
#     wait.until(
#         EC.element_to_be_clickable(('xpath', '//button[contains(text(),"Continue")]'))
#     ).click()
#
#     print(f"Test case {i+1} executed")
#
# driver.quit()

# -----------------------------------------------------------
#
# 9.Go to https://www.apollopharmacy.in/
# click on find doctors
# click on general physician
# click on the first doctor available
# select the date
# select the time
# click on continue
# -----------------------------------------------------------
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://www.apollopharmacy.in/")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 15)
#
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//a[contains(text(),"Find Doctors")]'))
# ).click()
#
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//h3[contains(text(),"General Physician")]'))
# ).click()
#
#
# first_doctor = wait.until(
#     EC.element_to_be_clickable(('xpath', '(//div[contains(@class,"doctor")])[1]'))
# )
# first_doctor.click()
#
#
# date = wait.until(
#     EC.element_to_be_clickable(('xpath', '(//button[contains(@class,"date")])[1]'))
# )
# date.click()
#
#
# time = wait.until(
#     EC.element_to_be_clickable(('xpath', '(//button[contains(@class,"time")])[1]'))
# )
# time.click()
#
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//button[contains(text(),"Continue")]'))
# ).click()
#
# print("Doctor appointment booking flow executed")

# -----------------------------------------------------------
#
# 10.Go to https://porter.in/
# enter city
# click on packers and movers
# enter pickup location
# enter drop location
# enter phone num
# enter shifting date
# check the price
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Chrome()
# driver.get("https://porter.in/")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 15)
#
#
# city = wait.until(
#     EC.presence_of_element_located(('xpath', '//input[@placeholder="Enter city"]'))
# )
# city.send_keys("Bangalore")
#
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//div[contains(text(),"Bangalore")]'))
# ).click()
#
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//div[contains(text(),"Packers & Movers")]'))
# ).click()
#
#
# pickup = wait.until(
#     EC.presence_of_element_located(('xpath', '//input[@placeholder="Pickup location"]'))
# )
# pickup.send_keys("Indiranagar")
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//div[contains(text(),"Indiranagar")]'))
# ).click()
#
#
# drop = wait.until(
#     EC.presence_of_element_located(('xpath', '//input[@placeholder="Drop location"]'))
# )
# drop.send_keys("Whitefield")
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//div[contains(text(),"Whitefield")]'))
# ).click()
#
#
# phone = wait.until(
#     EC.presence_of_element_located(('xpath', '//input[@type="tel"]'))
# )
# phone.send_keys("9999999999")
#
#
# date = wait.until(
#     EC.presence_of_element_located(('xpath', '//input[@type="date"]'))
# )
# date.send_keys("25-03-2026")
#
#
# wait.until(
#     EC.element_to_be_clickable(('xpath', '//button[contains(text(),"Check Price")]'))
# ).click()
#
# print("Price check flow executed")
