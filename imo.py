from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

driver = webdriver.Chrome()

with open('links.txt') as f:
    links = [line.rstrip('\n') for line in f]

counter = 0
for link in links:
    if counter == 0:
        driver.get(link)
        counter += 1
    else:
        control_string = "window.open('{0}')".format(link)
        driver.execute_script(control_string)
