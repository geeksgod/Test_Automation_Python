

def handle_dropdown(driver, locator, value):
    flag = 0
    try:
        driver.find_element_by_css_selector(locator).click()
    except:
        driver.find_element_by_xpath(locator).click()

    items = driver.find_elements_by_css_selector(".select2-results__option")

    for item in items:
        print(item.text)
        if item.text.lower() == value.lower():
            flag = 1
            item.click()
            break

    if flag == 0:
        items[len(items)-1].click()


def handle_dropdown_with_keywords(driver, locator, value):
    flag = 0
    try:
        driver.find_element_by_css_selector(locator).click()
    except:
        driver.find_element_by_xpath(locator).click()

    items = driver.find_elements_by_css_selector(".select2-results__option")

    for item in items:
        print(item.text)
        if value.lower() in item.text.lower():
            flag = 1
            item.click()
            break

    if flag == 0:
        items[len(items)-1].click()