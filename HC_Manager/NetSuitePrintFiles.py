from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import NetSuiteConfig
import pyautogui


# Constants
CHROME_DRIVER_PATH = "C:/Drivers/64/chromedriver.exe"
LOG_FILE_PATH = "C:/Users/juan.tamara/Desktop/log.txt"

# Physical Click coordinates
CORD_X = 302
CORD_Y = 16

# Browser's driver setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver_service = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=driver_service)

# Browser's driver setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver.maximize_window()

# Login whit Google Authenticator
driver.get(NetSuiteConfig.url_base)
driver.find_element(By.ID, "email").send_keys(NetSuiteConfig.username)
driver.find_element(By.ID, "password").send_keys(NetSuiteConfig.password)
driver.find_element(By.ID, "rememberme").click()
driver.find_element(By.ID, "login-submit").click()
google = input('Please enter your Google Authenticator: ')
driver.find_element(By.ID, 'uif49').send_keys(google)
driver.find_element(By.ID, "uif64").click()
driver.find_element(By.ID, "uif68").click()

# Into Day and Month to generate the report
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

    # Send dates to generate the report
    driver.find_element(By.CLASS_NAME, 'uir_filters_header').click()
    dates = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[1]/div[2]/div/div[2]/div[2]/span[2]/span/input').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[1]/div[2]/div/div[2]/div[2]/span[2]/span/input').send_keys(f'{day}/{month}/2023')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[1]/div[2]/div/div[2]/div[5]/span[2]/span/input').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[1]/div[2]/div/div[2]/div[5]/span[2]/span/input').send_keys(f'{day}/{month}/2023')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[1]/div[2]/div/div[2]/div[5]/span[2]/span/input').send_keys(Keys.TAB)
    time.sleep(10)

    # Get total pages to make a loop
    element = driver.find_element(By.ID, 'uir_totalcount')
    text = element.text
    total_pages = text.split()[1]
    total_pages = int(int(total_pages) / 50) + 1

    invoices_list = []
    documents_list = []
    error_list = []

    for page in range(total_pages):
        time.sleep(5)
        # Find table by id
        table = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[2]/div[2]/table')

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
                invoice = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr[' + str(rows) + ']/td[14]/a')
                invoice_value = invoice.text.strip()

                # Validate name and add to the list and print if it is not exist
                if invoice_value not in invoices_list:
                    invoices_list.append(invoice_value)
                    invoice = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr[' + str(rows) + ']/td[14]/a').click()
                    time.sleep(4)
                    pyautogui.click(x = CORD_X, y = CORD_Y)
                    pyautogui.hotkey('Ctrl', 'p')
                    time.sleep(2)
                    pyautogui.press("Enter")
                    time.sleep(3)

            except NoSuchElementException:

                # Write a log if is not possible to find an element
                error1 = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr['+str(rows)+']/td[3]/a')
                error_value1 = error1.text.strip()
                if error_value1 not in error_list:
                    error_list.append(error_value1)
                    path_absolute = LOG_FILE_PATH
                    with open(path_absolute, "a") as file:
                        file.write('La factura # ' + str(error_value1) + ' No se generó.' + "\n")

            try:
                # Get cell value
                document = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr[' + str(rows) + ']/td[16]/a')
                value = document.text.strip()

                # Validate name and add to the list and print if it is not exist
                if value not in documents_list:
                    documents_list.append(value)
                    document = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr[' + str(rows) + ']/td[16]/a').click()
                    time.sleep(4)
                    pyautogui.click(x = CORD_X, y = CORD_Y)
                    pyautogui.hotkey('Ctrl', 'p')
                    time.sleep(2)
                    pyautogui.press("Enter")
                    time.sleep(3)

            except NoSuchElementException:

                # Write a log if is not possible to find an element
                error2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form[2]/div[2]/table/tbody/tr[' + str(
                    rows) + ']/td[3]/a')
                error_value2 = error2.text.strip()
                if error_value2 not in error_list:
                    error_list.append(error_value2)
                    path_absolute = LOG_FILE_PATH
                    with open(path_absolute, "a") as file:
                        file.write('La factura # ' + str(error_value2) + ' no tiene documentos asociados.' + "\n")

        print('Im clicking')
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'navig-next').click()

driver.quit()