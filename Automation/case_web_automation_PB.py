from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# Configuraões do navegador
webDriver = webdriver.ChromeOptions()
webDriver.add_argument('--start-maximized')  # Inicia o navegador maximizado

# Inicializa o navegador
driver = webdriver.Chrome(options=webDriver)

# Elementos responsávis para destacar visualização dos botões que estão sendo clicados
def highlight_element(element):
    """Adiciona destaque visual a um elemento."""
    style = element.get_attribute('style')
    new_style = "border: 2px solid red; background-color: green;"

    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, new_style)
    sleep(0.5)

    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, style)

try:
    # Acessando o site proposto para automação
    driver.get("https://the-internet.herokuapp.com/challenging_dom")

    # a) Clicando nos 3 botões apresentados em tela
    for i in range(1, 4):
        button_initial = f'/html/body/div[2]/div/div/div/div/div[1]/a[{i}]'
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_initial)))
        sleep(2)
        highlight_element(button)
        button.click()

        # Clicando nos botões "Edit" e "Delete" considerando o botão selecionado anteriormente
        rows = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div/div/div[2]/table/tbody/tr')
        for row in rows:
            button_delete = row.find_element(By.XPATH, './td[7]/a[1]')
            button_edit= row.find_element(By.XPATH, './td[7]/a[2]')

            sleep(1)
            highlight_element(button_delete)
            button_delete.click()

            sleep(1)
            highlight_element(button_edit)
            button_edit.click()

finally:
    # Fim
    driver.quit()
