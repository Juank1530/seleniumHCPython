from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import datetime
import time
import NetSuiteConfig
import pyautogui
import sys

try:
    # Get current date and year
    current_year = datetime.datetime.now().year

    # Browser's driver setup
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver_service = Service(executable_path=NetSuiteConfig.CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
except Exception as e:
    print(f'Error in driver setup: {e}')
    print(
        'Also you can check the Google driver and update it. Please go to https://chromedriver.chromium.org/downloads  and download the last stable version.')
    sys.exit(1)


# Login whit Google Authenticator
driver.get(NetSuiteConfig.BASE_URL)
driver.find_element(By.ID, NetSuiteConfig.email).send_keys(NetSuiteConfig.username)
driver.find_element(By.ID, NetSuiteConfig.password).send_keys(NetSuiteConfig.password)
driver.find_element(By.ID, NetSuiteConfig.remenberme).click()
driver.find_element(By.ID, NetSuiteConfig.submit_btn).click()
google = input('Please enter your Google Authenticator: ')
driver.find_element(By.ID, NetSuiteConfig.google_authenticator).send_keys(google)
driver.find_element(By.ID, NetSuiteConfig.remenberme_authenticator).click()
driver.find_element(By.ID, NetSuiteConfig.authenticator_btn).click()

# Into Day and Month to generate the report
day = int(input('Please into the day that you want to generate the report : '))
month = int(input('Please into the month that you want to generate the report : '))

if day > 31 or month > 12:
    print('Invalid day or month :(')
else:
    driver.find_element(By.ID, NetSuiteConfig.search_box).click()
    driver.find_element(By.ID, NetSuiteConfig.search_box).send_keys('CA Facturas Medplus Detalle')
    driver.find_element(By.ID, NetSuiteConfig.search_box).send_keys(Keys.ENTER)
    time.sleep(10)
    driver.find_element(By.XPATH, NetSuiteConfig.open_view).click()
    time.sleep(10)

    # Send dates to generate the report
    driver.find_element(By.CLASS_NAME, NetSuiteConfig.filters_class).click()
    driver.find_element(By.XPATH, NetSuiteConfig.start_date).click()
    driver.find_element(By.XPATH, NetSuiteConfig.start_date).send_keys(f'{day}/{month}/{current_year}')
    driver.find_element(By.XPATH, NetSuiteConfig.end_date).click()
    driver.find_element(By.XPATH, NetSuiteConfig.end_date).send_keys(f'{day}/{month}/{current_year}')
    driver.find_element(By.XPATH, NetSuiteConfig.end_date).send_keys(Keys.TAB)
    time.sleep(10)

    # Get total pages to make a loop
    element = driver.find_element(By.ID, NetSuiteConfig.total_pages)
    text = element.text
    total_pages = text.split()[1]
    total_pages = int(int(total_pages) / 50) + 1

    invoices_list = []
    documents_list = []
    error_list = []

    for page in range(total_pages):
        time.sleep(5)
        # Find table by id
        table = driver.find_element(By.ID, NetSuiteConfig.id_table)

        # Find all rows into the table
        rows = table.find_elements(By.TAG_NAME, 'tr')

        # Count all rows
        rows_quantity = len(rows)
        rows_quantity = rows_quantity - 2
        print(rows_quantity)
        time.sleep(5)

        for rows in range(2, rows_quantity):
            try:
                # Get cell value
                invoice = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/form[2]/div[2]/table/tbody/tr[{str(rows)}]/td[14]/a')
                invoice_value = invoice.text.strip()

                # Validate name and add to the list and print if it is not exist
                if invoice_value not in invoices_list:
                    invoices_list.append(invoice_value)
                    invoice = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/form[2]/div[2]/table/tbody/tr[{str(rows)}]/td[14]/a'.click())
                    time.sleep(4)
                    pyautogui.click(x=NetSuiteConfig.CORD_X, y=NetSuiteConfig.CORD_Y)
                    pyautogui.hotkey('Ctrl', 'p')
                    time.sleep(2)
                    pyautogui.press("Enter")
                    time.sleep(3)

            except NoSuchElementException:

                # Write a log if is not possible to find an element
                error1 = driver.find_element(By.XPATH, f'/html/body/div[1]/div[3]/form[2]/div[2]/table/tbody/tr[{str(rows)}]/td[3]/a')
                error_value1 = error1.text.strip()
                if error_value1 not in error_list:
                    error_list.append(error_value1)
                    path_absolute = NetSuiteConfig.LOG_FILE_PATH
                    with open(path_absolute, "a") as file:
                        file.write('La factura # ' + str(error_value1) + ' No se generó.' + "\n")

            try:
                # Get cell value
                document = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form[2]/div[2]/table/tbody/tr[{str(rows)}]/td[16]/a')
                value = document.text.strip()

                # Validate name and add to the list and print if it is not exist
                if value not in documents_list:
                    documents_list.append(value)
                    document = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form[2]/div[2]/table/tbody/tr[{str(rows)}]/td[16]/a').click()
                    time.sleep(4)
                    pyautogui.click(x=NetSuiteConfig.CORD_X, y=NetSuiteConfig.CORD_Y)
                    pyautogui.hotkey('Ctrl', 'p')
                    time.sleep(2)
                    pyautogui.press("Enter")
                    time.sleep(3)

            except NoSuchElementException:

                # Write a log if is not possible to find an element
                error2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form[2]/div[2]/table/tbody/tr[{str(rows)}]/td[3]/a')
                error_value2 = error2.text.strip()
                if error_value2 not in error_list:
                    error_list.append(error_value2)
                    path_absolute = NetSuiteConfig.LOG_FILE_PATH
                    with open(path_absolute, "a") as file:
                        file.write('La factura # ' + str(error_value2) + ' no tiene documentos asociados.' + "\n")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, NetSuiteConfig.next_page_class).click()

driver.quit()
##except NoSuchElementException:
##    print('You have to check the Google driver and update it. Please go to https://chromedriver.chromium.org/downloads  and download the last stable version.')



