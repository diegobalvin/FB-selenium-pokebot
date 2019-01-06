from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.facebook.com/pokes/?notif_id=1546588370395323&notif_t=poke")

email = driver.find_element_by_name("email")
email.clear()
email.send_keys("##########")

password = driver.find_element_by_name("pass")
password.clear()
password.send_keys("##########")

driver.find_element_by_id("loginbutton").click()

while True:
    poke_buttons = driver.find_elements_by_xpath('//a[text()="Poke Back"]')
    print(len(poke_buttons))
    for poke in poke_buttons:
        poke.click()
    time.sleep(10)
    driver.refresh()
