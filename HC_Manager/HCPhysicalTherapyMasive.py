from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import config
import pyautogui


xpath_specialty = "/html/body/div/div/div/div[2]/div/div[6]/div/div[1]"
xpath_thc = "/html/body/div[1]/aside[1]/section/ul/li[2]/a/span"
patient_id = "nit_cli"
cord_x = 1061
cord_y = 201
btn_print_id = "btn-imprimir"
xpath_btn_close = "/html/body/div[13]/div[1]/div/a[1]"
patient_name = '/html/body/div[1]/div[1]/section[2]/div[2]/div[2]/form/div[1]/div[2]/div[1]/input'

# Browser's driver setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver_service = Service(executable_path='C:/Drivers/64/chromedriver.exe')
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
wait = WebDriverWait(driver, 60)
hc = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_specialty)))
hc.click()

# Looking for patient
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/div/input").send_keys(config.id_patient[0])
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[3]/div/button").click()
time.sleep(15)

# Open HC
fa = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_thc)))
fa.click()

for list in range(len(config.id_patient)):
    # Open HC
    #driver.find_element(By.XPATH, "/html/body/div[1]/aside[1]/div/section/div[3]/ul/li[11]/a").click()
    time.sleep(4)

    #Get id name to can break the loop
    btn_next = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div[3]/form/div[2]/button[1]')
    attribute = btn_next.get_attribute("id")

    # Get variables to set a file name
    name = driver.find_element(By.XPATH, patient_name)
    nameAttribute = name.get_attribute("value")
    nameAttribute = nameAttribute.strip()

    while attribute == 'btn-primero':

        # Get date to set a file name
        date = driver.find_element(By.XPATH,
                                   '/html/body/div[1]/div[1]/section[2]/div[3]/form/div[1]/div[2]/div[2]/div[1]/div/input')
        dateAttribute = date.get_attribute("value")
        dateAttribute = dateAttribute.split()[0]
        dateAttribute = dateAttribute.replace("/","-")
        dateAttribute = dateAttribute.strip()
        dateAttribute = dateAttribute.split('-')
        dateAttribute = dateAttribute[2] + '-' + dateAttribute[1] + '-' + dateAttribute[0]

        time.sleep(5)
        # Select print button
        wait = WebDriverWait(driver, 60)
        btn_print = wait.until(EC.element_to_be_clickable((By.ID, btn_print_id)))
        btn_print.click()

        # Wait
        time.sleep(9)

        # Change the context to the iframe
        #driver.switch_to.frame("iframe-impresion")

        # Click on download button
        pyautogui.click(x = cord_x, y = cord_y) #Local
        ##pyautogui.click(x=1278, y=254) #Server

        # Wait for the files manager
        time.sleep(8)

        # Generate a code to set a new name to the file
        characters = "abcdefghijklmnopqrstuvwxyz0123456789"
        random_strings = ""
        for i in range(10):
            random_character = random.choice(characters)
            random_strings += random_character
        pyautogui.write(dateAttribute + '_' + nameAttribute + '_' + config.id_patient[list] + '_' + random_strings)

        # To Press Enter to confirm and save the file
        pyautogui.press("enter")
        time.sleep(4)

        # To close the pdf view
        window = driver.window_handles
        driver.switch_to.window(window[-1])
        close = driver.find_element(By.XPATH, xpath_btn_close)
        close.click()

        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div[3]/form/div[2]/button[2]/i').click()
        btn_next = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div[3]/form/div[2]/button[1]')
        attribute = btn_next.get_attribute("id")
        if attribute != 'btn-primero':
            attribute = 'btn-next'
            time.sleep(3)

    # To send the new patient
    id = driver.find_element(By.NAME, patient_id)
    id.click()
    id.clear()
    id.send_keys(config.id_patient[list+1])

    #To change the focus for the new patient
    id.send_keys(Keys.TAB)
    time.sleep(4)

driver.quit()


