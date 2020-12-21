from selenium import webdriver

PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("http://www.python.org")
print(driver.title)

