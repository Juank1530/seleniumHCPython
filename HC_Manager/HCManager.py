import os
import time
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Browser's driver setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

# Setup Driver Browser
driver_service = Service(executable_path='C:\Drivers')
driver = webdriver.Chrome(service=driver_service)

# Browser's driver setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver.maximize_window()

# Setup Driver Browser another option
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

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
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[1]/div/input").send_keys(config.id_patient[0])
driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[2]/div[3]/div/button").click()
time.sleep(10)

# Go to report section
driver.find_element(By.XPATH, "/html/body/div[1]/aside[1]/div/section/div[3]/ul/li[22]").click()

for list in range(len(config.id_patient)):

    # Select all clinical reports
    wait = WebDriverWait(driver, 15)
    all = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div/table/tbody/tr/td/form/div/div/div[1]/div[1]/div/div/div")))
    all.click()

    # Setup patient id
    driver.find_element(By.ID, "documento-paciente").send_keys(config.id_patient[list])
    time.sleep(2)
    driver.find_element(By.NAME, 'nombre_paciente').click()

    # Select type report
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div/div/div/table/tbody/tr/td/form/div/div/div[6]/div[3]/div/div').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/section[2]/div/div/div/div/div/table/tbody/tr/td/form/div/div/div[6]/div[2]/div/ins').click()

    # Generate report and wait for its download
    driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div/table/tbody/tr/td/form/div/div/div[7]/div/div[1]").click()
    time.sleep(35)
    ####
    # Obtener los identificadores de ventana (ventana principal + popup)
    ventanas = driver.window_handles

    # Cambiar el control al último identificador de ventana (el popup más reciente)
    driver.switch_to.window(ventanas[-1])
    ###
    text = driver.find_element(By.XPATH, '/html/body/div[17]/div/div[6]')
    text = text.text
    error1 = 'No se ha podido generar el informe debido al gran volumen de datos, por favor simplifique los filtros e intente nuevamente.'
    error2 = 'No se encontraron registros con los filtros aplicados.'

    if text != error1 and text != error2:

        # Rename file and save in the specific path
        os.rename(f"C:/Users/juan.tamara/Downloads/{config.id_patient[list]}.pdf",
                  f"C:/Users/juan.tamara/Downloads/{config.files_names[list]}.pdf")

        # Click in confirmation button
        wait = WebDriverWait(driver, 20)
        button_popup = driver.find_element(By.XPATH, '/html/body/div[17]/div/div[10]/button[1]')
        button_popup.click()
    else:

        path_absolute ="C:/Users/juan.tamara/Desktop/error.txt"
        with open(path_absolute, "a") as file:
                file.write(str(config.id_patient[list]) + "\n")

        btn_error = driver.find_element(By.XPATH, '/html/body/div[17]/div/div[10]/button[1]').click()

        # Select all clinical reports
        wait = WebDriverWait(driver, 15)
        all = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                     "/html/body/div[1]/div[1]/section[2]/div/div/div/div/div/table/tbody/tr/td/form/div/div/div[1]/div[1]/div/div/div")))
        all.click()

        # Clear Patient id field
        patient = wait.until(EC.element_to_be_clickable((By.ID, "documento-paciente")))
        patient.clear()

        # Select type report
        driver.find_element(By.XPATH,
                            '/html/body/div[1]/div[1]/section[2]/div/div/div/div/div/table/tbody/tr/td/form/div/div/div[6]/div[3]/div/div').click()


# Close browser
driver.quit()


