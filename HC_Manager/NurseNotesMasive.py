from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
import time
import config
import pyautogui


xpath_specialty = "/html/body/div/div/div/div[2]/div/div[2]/div/div[1]"
patient_id = "id_paciente_presbicia"
cord_x = 1025
cord_y = 197
btn_print_id = "btn-imprimir"
xpath_btn_close = "/html/body/div[22]/div[1]/div"
table_id = '/html/body/div[1]/div[1]/section[2]/div[3]/div/div[2]/form/div/div[2]/div[4]/div[2]/table'
max_rows = '/html/body/div[1]/div[1]/section[2]/div[3]/div/div[2]/form/div/div[2]/div[1]/label/select'

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
wait = WebDriverWait(driver, 10)
hc = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_specialty)))
hc.click()

# Looking for patient
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/div/input").send_keys(config.id_patient[0])
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[3]/div/button").click()
time.sleep(10)

# Open HC
driver.find_element(By.XPATH, "/html/body/div[1]/aside[1]/div/section/div[3]/ul/li[12]/a/span[1]").click()
driver.find_element(By.XPATH, "/html/body/div[1]/aside[1]/div/section/div[3]/ul/li[12]/ul/li[1]/a").click()

for list in range(len(config.id_patient)):

    # Select max rows
    select_element = driver.find_element(By.XPATH, max_rows)
    select = Select(select_element)
    time.sleep(8)
    select.select_by_index(3)
    time.sleep(5)

    # To get total pages to me a loop
    element = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/section[2]/div[3]/div/div[2]/form/div/div[2]/div[5]")
    text = element.text
    total_pages = text.split()[9]
    total_pages = int(int(total_pages) / 50) + 1

    for page in range(1, total_pages):

        time.sleep(6)
        # Find table by id
        table = driver.find_element(By.XPATH,table_id)  # Reemplaza con el selector de tu tabla

        # Find all rows into the table
        rows = table.find_elements(By.TAG_NAME,'tr')

        # Count all rows
        rows_quantity = len(rows)
        time.sleep(2)

        for n in range(1, rows_quantity):
            
            driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div[3]/div/div[2]/form/div/div[2]/div[4]/div[2]/table/tbody/tr[' + str(n) + ']/td[2]/div').click()

            # Open HC
            #driver.find_element(By.XPATH, "/html/body/div[1]/aside[1]/div/section/div[3]/ul/li[11]/a").click()
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
            pyautogui.write(config.files_names[list]+random_strings)
    
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
                file.write(str(config.id_patient[list]) + '_Page_' + str(page) + '_Row_' + str(n) + "\n")

        # Scroll to asure the page change and click in next page
        driver.execute_script("window.scrollBy(0, 500);")
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.ID, 'div-controles_next'))).click()

    # To send the new patient
    id = driver.find_element(By.ID, patient_id)
    id.click()
    id.clear()
    id.send_keys(config.id_patient[list+1])

    #To change the focus for the new patient
    id.send_keys(Keys.TAB)
    time.sleep(4)

driver.quit()

