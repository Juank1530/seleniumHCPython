from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config
import pyautogui

# Browser's driver setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")


driver_service = Service(executable_path='C:\Drivers')
driver = webdriver.Chrome(service=driver_service)

# Browser's driver setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver.maximize_window()



#driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="LATEST").install()), options=options)

# Opening URL
driver.get(config.url)
time.sleep(2)

# Sing in
driver.find_element(By.ID, "usuario").send_keys(config.username)
driver.find_element(By.ID, "clave").send_keys(config.password)
driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/form/input[2]").click()
time.sleep(3)

# Select HC
wait = WebDriverWait(driver, 10)
hc = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div/div[1]")))
hc.click()

# Looking for patient
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/div/input").send_keys('999999')
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[3]/div/button").click()
time.sleep(10)

# Open HC
driver.find_element(By.XPATH, "/html/body/div[1]/aside[1]/div/section/div[3]/ul/li[15]/a/span").click()

# To send the new patient
id = wait.until(EC.element_to_be_clickable((By.ID, "id_paciente_presbicia")))
id.click()
id.clear()
id.send_keys(config.id_patient[0])

#To change the focus for the new patient
patient_name = driver.find_element(By.ID, "nombre_paciente_presbicia").send_keys(Keys.TAB)
time.sleep(6)

for list in range(len(config.id_patient)):
    # Open HC
    #driver.find_element(By.CLASS_NAME, "medical-icon-i-medical-records").click()
    time.sleep(3)

    # Select print button
    wait = WebDriverWait(driver, 60)
    btn_print = wait.until(EC.element_to_be_clickable((By.ID, "btn-imprimir")))
    btn_print.click()

    # Wait
    time.sleep(5)

    # Change the context to the iframe
    #driver.switch_to.frame("iframe-impresion")

    # Click on download button
    pyautogui.click(x=1025, y=198) #local

    # Wait for the files manager
    time.sleep(5)

    # Set a new name to the file
    pyautogui.write(config.files_names[list])

    # To Press Enter to confirm and save the file
    pyautogui.press("enter")
    time.sleep(4)

    # To close the pdf view
    window = driver.window_handles
    driver.switch_to.window(window[-1])
    close = driver.find_element(By.XPATH, "/html/body/div[17]/div[1]/div")
    close.click()

    # To send the new patient
    id = wait.until(EC.element_to_be_clickable((By.ID, "id_paciente_presbicia")))
    id.click()
    id.clear()
    id.send_keys(config.id_patient[list+1])

    # To change the focus for the new patient
    patient_name = driver.find_element(By.ID, "nombre_paciente_presbicia").send_keys(Keys.TAB)
    time.sleep(4)


driver.quit()




