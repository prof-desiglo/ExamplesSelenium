from selenium import webdriver
from selenium.webdriver.common.by import By
from testLog import getTestLogPath

if __name__ == "__main__":
    print("Iniciando...")
    browser = webdriver.Firefox()
    browser.get("http://google.com")
    browser.save_screenshot(getTestLogPath("01"))
    txtPesquisar = browser.find_element(By.XPATH, "//textarea[@title='Pesquisar']")
    txtPesquisar.clear()
    txtPesquisar.send_keys("selenium")
    bntPesquisar = browser.find_element(By.XPATH, "(//input[@value='Pesquisa Google'])[2]")
    bntPesquisar.click()
    browser.save_screenshot(getTestLogPath("02"))
    txtURL = browser.find_element(By.XPATH, "//*[text()='https://www.selenium.dev']")
    assert txtURL.is_displayed
    browser.close()
    print("Finalizando")
    pass