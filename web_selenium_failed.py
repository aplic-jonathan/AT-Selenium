from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://acme-test.uipath.com/login")
formEmail = driver.find_element(By.ID, 'email').send_keys("firman.maulana@is-gs.com")
formPassword = driver.find_element(By.ID, 'passwordokokook').send_keys("P@ssw0rd")

buttonLogin = driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")

for element in buttonLogin:
    if element.text == "Login":
        element.click()
        break