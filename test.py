from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

edge_options = EdgeOptions()
edge_options.add_argument("--start-maximized")  

path_to_msedgedriver = "C:/path/to/your/msedgedriver.exe"

def start_browser_or_new_tab():
    # Intentar conectar a una sesión existente
    try:
        driver = webdriver.Remote(
            command_executor='http://127.0.0.1:9515',
            options=edge_options
        )
        print("Sesión existente encontrada, abriendo una nueva pestaña.")
        driver.execute_script("window.open('');")  # Abrir nueva pestaña
        driver.switch_to.window(driver.window_handles[-1])  # Cambiar a la nueva pestaña
    except Exception as e:
        print("No se encontró una sesión existente, abriendo un nuevo navegador.")
        service = EdgeService(path_to_msedgedriver)
        driver = webdriver.Edge(service=service, options=edge_options)

    return driver

# Iniciar navegador o nueva pestaña
driver = start_browser_or_new_tab()

# Navegar a la página de Google
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
