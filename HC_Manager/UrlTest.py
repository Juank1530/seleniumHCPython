from webdriver_manager.chrome import ChromeDriverManager

url = ChromeDriverManager().install()
print(url)