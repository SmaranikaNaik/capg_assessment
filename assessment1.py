
'''
1.Write a script to:
Open https://www.demowebshop.tricentis.com
Navigate to Books
Add first book to cart
Click Shopping Cart
Verify the product is present in the cart.
'''
#
# from selenium import webdriver
# import time
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com")
# time.sleep(1)
# driver.find_element('xpath','//a[contains(text(),"Books")]').click()
# time.sleep(1)
# driver.find_element('xpath','(//input[@value="Add to cart"])[1]').click()
# time.sleep(5)
# driver.find_element('xpath','//span[text()="Shopping cart"]').click()
# time.sleep(2)
#
# product = driver.find_element('xpath','//table[@class="cart"]//a')
#
# if product.is_displayed():
#     print("Product successfully added to cart")
# else:
#     print("Product not found in cart")

'''
2.Write a Selenium script to:
Open https://www.demowebshop.tricentis.com
Navigate to Electronics
Use XPath contains() to locate the Cell Phones category
Click it.
'''
# from selenium import webdriver
# import time
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
#
# driver.get("https://demowebshop.tricentis.com")
# time.sleep(1)
# driver.find_element('xpath','//a[contains(text(),"Electronics")]').click()
# time.sleep(1)
# driver.find_element('xpath','(//a[contains(text(),"Cell phones")])[4]').click()

'''
3.Write a Selenium script to:
Open https://the-internet.herokuapp.com/dynamic_loading/1
Click Start
Wait until the Hello World text appears
Print the text.
'''
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.implicitly_wait(30)
#
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
# time.sleep(2)
#
# driver.find_element('xpath','//button[text()="Start"]').click()
#
# time.sleep(5)
#
# text = driver.find_element('xpath','//div[@id="finish"]/h4').text
#
# print(text)

'''
4.Write a script to:
Open https://the-internet.herokuapp.com/dynamic_controls
Click Remove
Wait until Add button becomes clickable
Click Add
'''
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.implicitly_wait(30)
#
# driver.get("https://the-internet.herokuapp.com/dynamic_controls")
# time.sleep(2)
# driver.find_element('xpath','//button[text()="Remove"]').click()
# time.sleep(5)
# driver.find_element('xpath','//button[text()="Add"]').click()
'''
5.Write a Selenium script to:
Open https://demoqa.com/select-menu
Select "Group 2, option 1" from the Select Value dropdown
Verify the selected value.
'''
# from selenium import webdriver
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.implicitly_wait(30)
#
# driver.get("https://demoqa.com/select-menu")
#
# time.sleep(2)
#
# driver.find_element("id","withOptGroup").click()
# driver.find_element('xpath','//div[text()="Group 2, option 1"]').click()
# selected_value = driver.find_element('xpath','//div[@id="withOptGroup"]//div[contains(@class,"singleValue")]').text
#
# print("Selected value:", selected_value)
#
# if selected_value == "Group 2, option 1":
#     print("Verification Successful")
# else:
#     print("Verification Failed")

'''
6.Write a Selenium script to:
Open https://demoqa.com/select-menu
Scroll to Standard multi select
Select Volvo, Saab, and Opel
Print all selected options.
'''
# from selenium import webdriver
# from selenium.webdriver.support.ui import Select
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# driver = webdriver.Chrome(opts)
# driver.implicitly_wait(30)
#
# driver.get("https://demoqa.com/select-menu")
# dropdown = driver.find_element("id", "cars")
# driver.execute_script("arguments[0].scrollIntoView();", dropdown)
# select = Select(dropdown)
# select.select_by_visible_text("Volvo")
# select.select_by_visible_text("Saab")
# select.select_by_visible_text("Opel")
# selected_options = select.all_selected_options
#
# print("Selected Options:")
# for option in selected_options:
#     print(option.text)

'''
7.Write a Selenium script to:
Open https://demoqa.com/menu/
Hover over Main Item 2
Hover over SUB SUB LIST
Click Sub Sub Item 1
'''
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import time
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.implicitly_wait(10)
#
# driver.get("https://demoqa.com/menu/")
# time.sleep(2)
#
# ac= ActionChains(driver)
#
# main_item = driver.find_element('xpath', '//a[text()="Main Item 2"]')
# ac.move_to_element(main_item).perform()
# time.sleep(1)
#
# sub_list = driver.find_element('xpath', '//a[text()="SUB SUB LIST »"]')
# ac.move_to_element(sub_list).perform()
# time.sleep(1)
#
# sub_item = driver.find_element('xpath', '//a[text()="Sub Sub Item 1"]')
# sub_item.click()

'''
8.Write a Selenium script to:
Open https://demoqa.com/droppable
Drag Drag me element
Drop it on Drop here
Verify text changes to Dropped!
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.implicitly_wait(10)

driver.get("https://demoqa.com/droppable")

time.sleep(2)

actions = ActionChains(driver)

# Locate elements
drag = driver.find_element('id', "draggable")
drop = driver.find_element('id', "droppable")

actions.drag_and_drop(drag, drop).perform()
time.sleep(2)

text = driver.find_element('id', "droppable").text

if text == "Dropped!":
    print("Drag and Drop Successful")
else:
    print("Drag and Drop Failed")

'''
Write a Selenium script to:
Open https://the-internet.herokuapp.com/javascript_alerts
Click JS Confirm
Accept the alert
Verify result text shows You clicked: Ok


Write a Selenium script to:
Open https://the-internet.herokuapp.com/upload
Upload a file from local system
Click Upload
Verify uploaded file name.


Write a Selenium script to:
Open https://the-internet.herokuapp.com/download
Download any file
Verify the file is downloaded in the Downloads folder using Python.


Write a script to:
Open https://demowebshop.tricentis.com
Add any two products from Books
Navigate to Shopping Cart
Verify total number of products added is 2.


Write a Selenium script that:
Open https://demowebshop.tricentis.com
Navigate to Books
Add all books priced below $20 to cart


Write the steps to read the data from excel


Write the syntax for the xpath to locate the elements using
	*	attributes
	ans: //tagname[@attr_name="attr_val"]
	*	text
	ans: //tagname[text()="Text"]
	*	group indexing
	ans: (//tagname[@attr_name="attr_val"])[index]
	*	contains
	ans: //tagname[contains(text(),"partial text")]


#########################################################################################################

1. Which locator is generally the fastest in Selenium?
2. Which wait is recommended for handling dynamic elements in Selenium?
3. Which Selenium class is used to handle dropdown listbox
'''

from selenium import webdriver
import time
