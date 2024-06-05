import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.ebay.com/")
print(driver.current_url)

#time.sleep(2)

search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@class='gh-tb ui-autocomplete-input']")))
#search_box.click()
search_box.send_keys("women watch")
search_box.send_keys(Keys.RETURN)

header_element = driver.find_element(By.XPATH,"//*[@class='srp-controls__count-heading']//span[contains(text(),'women watch')]")
header_text = header_element.text

expected_results = "women watch"
if expected_results in header_text.lower():
    print("Header contains the results for women's watches.")
else:
    print("Header does NOT contain the results for women's watches.")

driver.quit()