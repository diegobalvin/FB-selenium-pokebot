from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

total_sec = float(input("How many minutes would you like to run the script?: ")) * 60
refresh = float(input("How many seconds between refresh?: "))

# Removes any pop-ups that may occure on the Chrome driver.
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.facebook.com/pokes/?notif_id=1546588370395323&notif_t=poke")

email = driver.find_element_by_name("email")
email.clear()
email.send_keys("##########") # replace with your email or phone number

password = driver.find_element_by_name("pass")
password.clear()
password.send_keys("##########") # replace with your login password

driver.find_element_by_id("loginbutton").click()

while total_sec > 0:
    poke_buttons = driver.find_elements_by_xpath('//a[text()="Poke Back"]')
    for poke in poke_buttons: poke.click()
    print(len(poke_buttons)) # prints how many people you poked
    time.sleep(refresh)
    total_sec -= refresh

driver.close()