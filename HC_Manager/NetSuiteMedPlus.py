from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import NetSuiteConfig
import pyautogui


# Browser's driver setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver_service = Service(executable_path="C:/Drivers/64/chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

# Browser's driver setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver.maximize_window()

# Opening URL
driver.get(NetSuiteConfig.url_base)
driver.find_element(By.ID, "email").send_keys(NetSuiteConfig.username)
driver.find_element(By.ID, "password").send_keys(NetSuiteConfig.password)
driver.find_element(By.ID, "rememberme").click()
driver.find_element(By.ID, "login-submit").click()
time.sleep(15)
driver.find_element(By.ID, "uif64").click()
driver.find_element(By.ID, "uif68").click()
time.sleep(5)

for list in range(len(NetSuiteConfig.files_names)):
    driver.get(NetSuiteConfig.files_names[list])
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'p')
    time.sleep(3)
    pyautogui.press("enter")

