from datetime import time
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import NetSuiteConfig
import pyautogui

cord_x = 302
cord_y = 16

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
google = input('Please enter your Google Authenticator: ')
driver.find_element(By.ID, 'uif49').send_keys(google)
driver.find_element(By.ID, "uif64").click()
driver.find_element(By.ID, "uif68").click()
day = int(input('Please into the day that you want to generate the report : '))
month = int(input('Please into the month that you want to generate the report : '))

if day > 31 or month > 12:
    print('Invalid day or month :(')
else:
    driver.find_element(By.ID, "uif55").click()
    driver.find_element(By.ID, "uif55").send_keys('CA Facturas Medplus Detalle')
    driver.find_element(By.ID, "uif55").send_keys(Keys.ENTER)
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr[2]/td[1]/a[2]").click()
    time.sleep(10)


    # To get total pages to me a loop
    driver.find_element(By.CLASS_NAME, 'uir_filters_header').click()
    dates = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[1]/div[2]/div/div[2]/div[2]/span[2]/span/input').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[1]/div[2]/div/div[2]/div[2]/span[2]/span/input').send_keys(f'{day}/{month}/2023')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[1]/div[2]/div/div[2]/div[5]/span[2]/span/input').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[1]/div[2]/div/div[2]/div[5]/span[2]/span/input').send_keys(f'{day}/{month}/2023')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[1]/div[2]/div/div[2]/div[5]/span[2]/span/input').send_keys(Keys.TAB)
    time.sleep(10)

    element = driver.find_element(By.ID, 'uir_totalcount')
    text = element.text
    total_pages = text.split()[1]
    total_pages = int(int(total_pages) / 50)
    print(total_pages)

    for page in range(1, 2):
        # Find table by id
        table = driver.find_element(By.ID, 'div__bodytab')  # Reemplaza con el selector de tu tabla

        # Find all rows into the table
        rows = table.find_elements(By.TAG_NAME, 'tr')

        # Count all rows
        rows_quantity = len(rows)
        print(rows_quantity)
        time.sleep(5)

        invoices_list = []
        documents_list = []

        for rows in range(2, 51):

            # Encuentra el elemento utilizando una expresión XPath
            invoice = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr['+str(rows)+']/td[14]/a')
            invoice_value = invoice.text.strip()

            if invoice_value not in invoices_list:
                invoices_list.append(invoice_value)
                print(f'Se ha guardado el valor "{invoice_value}" en la lista.')
                invoice = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr[' + str(rows) + ']/td[14]/a').click()
                time.sleep(4)
                pyautogui.click(x = cord_x, y = cord_y)
                # Ahora estás en el contexto de la nueva ventana (visor de PDF)
                pyautogui.hotkey('Ctrl', 'p')
                time.sleep(2)
                pyautogui.press("Enter")
                time.sleep(10)



"""







            else:
                print(f'El valor "{invoice_value}" ya existe en la lista y no se ha guardado.')

            print(invoices_list)

        
            elemento = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr['+str(rows)+']/td[16]/a')
            # Obtiene el valor de la celda
            valor = elemento.text.strip()

            if valor not in documents_list:
                documents_list.append(valor)
                print(f'Se ha guardado el valor "{valor}" en la lista.')
                elemento = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr[' + str(rows) + ']/td[16]/a').click()
            else:
                print(f'El valor "{valor}" ya existe en la lista y no se ha guardado.')


            print(documents_list)



            # Elemento HTML del que deseas obtener el valor (reemplaza 'element_id' con el ID real)
            element_id = 'element_id'
            #element = driver.find_element_by_id(element_id)

    

            # Cerrar el navegador
        
    driver.quit()
"""
driver.quit()