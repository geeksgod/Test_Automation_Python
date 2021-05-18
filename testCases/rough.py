from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://uahep-grmss.staging.yipl.com.np/login")
textbox_username_css = '#email'
textbox_password_css = '#password'
button_login_css = 'div>button'

driver.find_element_by_css_selector(textbox_username_css).clear()
driver.find_element_by_css_selector(textbox_username_css).send_keys('superadmin@uahep.com')
driver.find_element_by_css_selector(textbox_password_css).clear()
driver.find_element_by_css_selector(textbox_password_css).send_keys("password")
driver.find_element_by_css_selector(button_login_css).click()
driver.get("https://uahep-grmss.staging.yipl.com.np/admin/complainant/create")
driver.find_element_by_css_selector("#select2-preferred_language-container").click()
options = driver.find_elements_by_css_selector(".select2-results__option")
for option in options:
    if option.text.lower() == "Nepali".lower():
        option.click()
        break
def drop_down_selector(drop_down_locator, menu_class_locator, value):
    driver.find_element_by_css_selector(drop_down_locator).click()
    items = driver.find_elements_by_css_selector(menu_class_locator)
    for item in items:
        print(item.text)
        if item.text.lower() == value.lower():
            item.click()
            break


drop_down_selector('#select2-complainant_type-container', ".select2-results__option", "self")
driver.find_element_by_css_selector("#js-next-btn").click()
driver.find_element_by_css_selector('#descImgDrop').send_keys("/home/geeksgod/Downloads/1856736.jpg")
time.sleep(5)
driver.close()
