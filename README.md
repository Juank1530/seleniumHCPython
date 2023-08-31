# Selenium HC Python

## Automations with Selenium and Python (HC Downloads)

### Description
These automated scripts allow access to each section of the Manager platform and download the Clinical History of each patient on the local machine where it is executed.

### Requirements for Execution

To be able to run these scripts, make sure to meet the following requirements:

1. **Python**: You must have Python installed, preferably version 3. You can install Python by referring to the official Python documentation on the [Python website](https://www.python.org/).
2. **Selenium**: You need to have the Selenium package installed. You can install it using the following command: **pip install selenium** It is recommended to use the latest version of Selenium for optimal performance.
3. **Pyautogui**: You need to have the Pyautogui package installed. You can install it using the following command: **py -m pip install pyautogui** 
4. **WebDriver del Navegador**: You also need the WebDriver for the browser you plan to use with Selenium. Make sure to consult the official Selenium documentation for information on how to set up and download the appropriate WebDriver for your browser.
5. **Archivo config.py**: Within each script, there is a reference to the config.py file. This file contains:
	1. The URL of the platform where HC is downloaded.
	2. Username and password for login.
	3. A list of patient documents. 
	4. A list of names under which the files will be saved on the local machine.           

**Example**:

```
username = "user"  
password = "Password"  
url = "mysite.com"  
  
id_patient = [  
'id_paciente1',
id_paciente2',
etc...
]  
  
files_names = [  
'name1',
'name2',
etc...   
]
```

### Configuration

Before running the scripts, make sure to properly configure the WebDriver and any other necessary settings according to the Selenium documentation on the [Selenium website](https://www.selenium.dev/downloads/).

Ready! With these requirements met, you'll be ready to use the automation scripts and download the Clinical Histories of the patients from the Manager platform.
