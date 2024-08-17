from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

edge_options = EdgeOptions()
edge_options.add_argument("--start-maximized")  

path_to_msedgedriver = "C:/path/to/your/msedgedriver.exe"

try:
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:9515',
        options=edge_options
    )
except Exception as e:
    print("No se encontró una sesión existente, abriendo un nuevo navegador.")
    service = EdgeService(path_to_msedgedriver)
    driver = webdriver.Edge(service=service, options=edge_options)

driver.get("https://www.google.com")

time.sleep(2)

try:
    lucky_button = driver.find_element(By.NAME, "btnI")
    lucky_button.click()
except Exception as e:
    print("No se encontró el botón, intentando nuevamente.")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("I'm Feeling Lucky")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

time.sleep(5)
