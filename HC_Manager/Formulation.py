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

xpath_specialty = "/html/body/div/div/div/div[2]/div/div[2]/div/div[1]"
patient_id = "identificacion"
cord_x = 1004
cord_y = 232
btn_print_id = "B_imprimir"
xpath_btn_close = "/html/body/div/div[1]/div/div[1]/div/div[6]/div/div/div[1]/div[2]"
table_id = '/html/body/div/div[1]/div/div[1]/div/div[3]/div[1]/div[1]/div/div/div[2]/div[2]'


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
wait = WebDriverWait(driver, 30)
hc = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/div/div[1]")))
hc.click()

# Looking for patient
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/div/input").send_keys(config.id_patient[0])
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[3]/div/button").click()
time.sleep(15)

# Open HC
fa = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/aside[1]/div/section/div[3]/ul/li[16]/a/span")))
fa.click()

for list in range(len(config.id_patient)):

    time.sleep(2)
    # To get total pages to me a loop
    element = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[3]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[1]/span")
    text = element.text
    total_pages = text.split()[9]
    total_pages = int(int(total_pages) / 5) + 1

    if total_pages == 1:
        total_pages = 2
    else:
        total_pages = total_pages

    for pages in range (1,total_pages):

        time.sleep(6)
        # Find table by id
        table = driver.find_element(By.XPATH,table_id)  # Reemplaza con el selector de tu tabla

        # Find all rows into the table
        rows = table.find_elements(By.TAG_NAME,'tr')

        # Count all rows
        rows_quantity = len(rows)
        time.sleep(2)

        if rows_quantity == 1:
            rows_quantity = 2
        else:
            total_pages = total_pages

        for n in range(1, rows_quantity):

            driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div/div[1]/div/input').send_keys('Keys.TAB')
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[3]/div[1]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[' + str(n) + ']/td[2]').click()

            # Open HC
            time.sleep(3)

            # Select print button
            wait = WebDriverWait(driver, 30)
            btn_print = wait.until(EC.element_to_be_clickable((By.ID, btn_print_id)))
            btn_print.click()

            # Wait
            time.sleep(15)

            # Click on download button
            pyautogui.click(x = cord_x, y = cord_y)

            # Wait for the files manager
            time.sleep(8)

            # Generate a code to set a new name to the file
            characters = "abcdefghijklmnopqrstuvwxyz0123456789"
            random_strings = ""
            for i in range(10):
                random_character = random.choice(characters)
                random_strings += random_character
            pyautogui.write(config.files_names[list] + '_' + random_strings)

            # To Press Enter to confirm and save the file
            pyautogui.press("enter")
            time.sleep(4)

            # To close the pdf view
            window = driver.window_handles
            driver.switch_to.window(window[-1])
            close = driver.find_element(By.XPATH, xpath_btn_close)
            close.click()
            time.sleep(3)

            # Log file
            path_absolute = "C:/Users/juan.tamara/Desktop/log.txt"
            with open(path_absolute, "a") as file:
                file.write(str(config.id_patient[list]) + '_Page_' + str(pages) + '_Row_' + str(n) + "\n")

        if pages != total_pages - 1:
            time.sleep(3)
            driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[3]/div[1]/div[1]/div/div/div[2]/div[2]/div/div[2]/nav/ul/li[2]/button/i').click()

    driver.find_element(By.XPATH, '/html/body/div/div[1]/div/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div/div[1]/div/input').clear()
    for tab in range(1,11):
        driver.find_element(By.ID, 'option-search-left').send_keys(Keys.TAB)

    # To send the new patient
    id = driver.find_element(By.ID, patient_id)
    id.click()
    id.clear()
    id.send_keys(config.id_patient[list+1])

    #To change the focus for the new patient
    id.send_keys(Keys.TAB)
    time.sleep(4)

driver.quit()
