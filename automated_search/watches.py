from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0")

# first part of Rolex watch test
# check Rolex checkbox then verify that first 2 results contain word 'rolex' in title
rolex_check = driver.find_element(By.XPATH, "//*[@class='checkbox__control'][@aria-label='Rolex']")
rolex_check.click()
time.sleep(5)

#  wait for result to load
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//ul[@class='srp-results srp-grid clearfix']//div[@class=s-item__wrapper clearfix]")))

# empty list to store found title, price rolex data
# rolex_results = []
# time.sleep(5)

# need to collect the first 2 of 60 results on the page
# results = driver.find_elements(By.XPATH,"//*[@class='srp-results srp-grid clearfix']//div[@class='s-item__wrapper clearfix']")
# print(results)
driver.implicitly_wait(10)
# time.sleep(5)
results = driver.find_elements(By.XPATH,"//*[@class='srp-results srp-grid clearfix']//div[@class='s-item__wrapper clearfix']")
results_data = {}
mismatches = []

for i in range(2):
    title_element = results[i].find_element(By.CLASS_NAME,"s-item__title")
    title = title_element.text.lower()
    if "rolex" not in title:
        mismatches.append(f"Title mismatch at index {i + 1}: Expected 'rolex' in title, but got: {title}")

    price_element = results[i].find_element(By.CLASS_NAME,"s-item__price")
    price = price_element.text
    results_data[i] = {'title': title, 'price': price}

# Open each item in a new tab and verify title and price
for idx, data in results_data.items():
    # time.sleep(2)
    # item_link = driver.find_element(By.LINK_TEXT,(data['title']))
    item_link = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME, "s-item__title")))
    #  item_link.send_keys(Keys.CONTROL + Keys.RETURN)
    # use action chains to click?
    time.sleep(5)
    item_link.click()
    # time.sleep(2)
    # need to let the new tab load

    driver.switch_to.window(driver.window_handles[-1])

    current_title = driver.find_element(By.CLASS_NAME,"x-item-title__mainTitle").text.lower()
    if data['title'] not in current_title:
        mismatches.append(
            f"Title mismatch for item '{data['title']}': Expected '{data['title']}', but got: {current_title}")

    current_price = driver.find_element(By.CLASS_NAME,"x-price-primary").text
    if data['price'] != current_price:
        mismatches.append(
            f"Price mismatch for item '{data['title']}': Expected {data['price']}, but got: {current_price}")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    # rolex  test  DONE

time.sleep(5)
# need to print if any mismatches found
if mismatches:
    print("Mismatches found:")
    for mismatch in mismatches:
        print(mismatch)
else:
    print("No mismatches found.")


# need to close tab and switch back to main tab
# driver.close()
# driver.switch_to.window(driver.window_handles[0])

time.sleep(5)
# Casio  test  (2nd test)
rolex_check.click()

casio_check = driver.find_element(By.XPATH, "//*[@class='checkbox__control'][@aria-label='Casio']")
casio_check.click()

# WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME,"s-item")))
time.sleep(5)
casio_mismatch = []

casio_results = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME,"s-item")))
print(casio_results)

for result in casio_results[-2:]:
    casio_title = result.find_element(By.CLASS_NAME,"//*[@class='srp-results srp-grid clearfix']//div[@class='s-item__wrapper clearfix']").text.lower()

# verify casio is present in title
    if 'casio' not in casio_title:
        casio_mismatch.append(casio_title)

# need to print out any text mismatch
if casio_mismatch:
    print("Mismatches found in Casio results:")
    for mismatch in casio_mismatch:
        print(mismatch)
else:
    print("There are NO title mismatches found in the last 2 Casio results.")

# close the driver - complete
driver.quit()

