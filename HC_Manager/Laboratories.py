from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import config
import pyautogui


xpath_specialty = "/html/body/div/div/div/div[2]/div/div[2]/div/div[1]"
patient_id = "id_paciente_presbicia"
cord_x = 1025
cord_y = 197
btn_print_id = "btn-imprimir"
xpath_btn_close = "/html/body/div[17]/div[1]/div/a[1]"
table_id = '/html/body/div[1]/div[1]/section[2]/div[3]/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div'
max_rows = '/html/body/div[1]/div[1]/section[2]/div[3]/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/div[1]/div/label/select'

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
fa = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/aside[1]/div/section/div[3]/ul/li[18]/a/span")))
fa.click()

for list in range(len(config.id_patient)):

    # Select max rows
    select_element = driver.find_element(By.XPATH, max_rows)
    select = Select(select_element)
    time.sleep(8)
    select.select_by_index(3)
    time.sleep(5)

    time.sleep(6)
    # Find table by id
    table = driver.find_element(By.XPATH, table_id)  # Reemplaza con el selector de tu tabla

    # Find all rows into the table
    rows = table.find_elements(By.TAG_NAME, 'tr')

    # Count all rows
    rows_quantity = len(rows)
    print(rows_quantity)
    time.sleep(2)

    for n in range(1, rows_quantity):

        driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div[3]/div[3]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div[2]/div/table/tbody/tr[' + str(n) + ']/td[1]/div').click()

        # Open HC
        #driver.find_element(By.XPATH, "/html/body/div[1]/aside[1]/div/section/div[3]/ul/li[11]/a").click()
        time.sleep(3)

        # Select print button
        wait = WebDriverWait(driver, 60)
        btn_print = wait.until(EC.element_to_be_clickable((By.ID, btn_print_id)))
        btn_print.click()

        # Wait
        time.sleep(7)

        # Change the context to the iframe
        #driver.switch_to.frame("iframe-impresion")

        # Click on download button
        pyautogui.click(x = cord_x, y = cord_y) #Local
        ##pyautogui.click(x=1278, y=254) #Server

        # Wait for the files manager
        time.sleep(8)

        # Set a new name to the file
        pyautogui.write(config.files_names[list] + '_' + str(n))

        # To Press Enter to confirm and save the file
        pyautogui.press("enter")
        time.sleep(4)

        # To close the pdf view
        window = driver.window_handles
        driver.switch_to.window(window[-1])
        close = driver.find_element(By.XPATH, xpath_btn_close)
        close.click()

    # To send the new patient
    id = driver.find_element(By.ID, patient_id)
    id.click()
    id.clear()
    id.send_keys(config.id_patient[list+1])

    #To change the focus for the new patient
    patient_name = driver.find_element(By.ID, "nombre_paciente_presbicia").send_keys(Keys.TAB)
    time.sleep(4)

driver.quit()
