import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

email = (By.XPATH, "//input[@id='Email']")
# ele = driver.find_element(By.XPATH, "//input[@id='Email']")
ele = WebDriverWait(driver, 5).until( ec.presence_of_element_located(email))

ele.send_keys("admin@yourstore.com")

print(type(ele))
time.sleep(3)
driver.close()
