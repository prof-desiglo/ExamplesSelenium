from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
from selenium import webdriver



label_buscar_locator = (By.XPATH, "//textarea[1]")
bnt_buscar_locator = (By.XPATH, "(//input[@name='btnK'])[2]")
txt = "Felipe Desiglo Ferrare"

# Abra o Navegador
browser = webdriver.Chrome()

# Abra a página
browser.get('https://www.google.com.br/')

# Espera a página carregar com o elemento disponível
WebDriverWait(browser, 20).until(
            expected_conditions.presence_of_element_located(label_buscar_locator))
 
 # envia o texto
label_buscar = browser.find_element(label_buscar_locator[0], label_buscar_locator[1])
label_buscar.send_keys(txt)

label_buscar.send_keys(Keys.TAB);

bnt_buscar = browser.find_element(bnt_buscar_locator[0], bnt_buscar_locator[1])
bnt_buscar.click()
