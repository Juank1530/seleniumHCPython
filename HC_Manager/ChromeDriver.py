from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request

try:
        service = Service(ChromeDriverManager().install())
except ValueError:
        latest_chromedriver_version_url = "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
        latest_chromedriver_version = urllib.request.urlopen(latest_chromedriver_version_url).read().decode('utf-8')
        service = Service(ChromeDriverManager(version=latest_chromedriver_version).install())
driver = webdriver.Chrome(options=chrome_options, driver_executable_path=driver_executable_path)
driver_executable_path = service.path