from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configurações do Selenium
chrome_options = Options()
chrome_options.add_argument('--headless')  # Executar em modo headless (sem interface gráfica)
driver = webdriver.Chrome(options=chrome_options)

# Abrir a página do 4devs
driver.get('https://www.4devs.com.br/gerador_de_pessoas')
while (True):
    try:
        # Aguardar o carregamento da página
        time.sleep(2)

        # Clicar no botão "Gerar Pessoa"
        driver.find_element(By.ID, 'bt_gerar_pessoa').click()

        # Aguardar um tempo para que os dados sejam gerados
        time.sleep(2)

        # Obter os dados gerados
        nome = driver.find_element(By.ID, 'nome')#.get_attribute('value')
        cpf = driver.find_element(By.ID, 'cpf')#.get_attribute('value')
        email = driver.find_element(By.ID, 'email')#.get_attribute('value')
        senha = driver.find_element(By.ID, 'senha')#.get_attribute('value')
        print('-' * 50)

        # Imprimir os dados gerados
        print('Nome:', nome.text)
        print('CPF:', cpf.text)
        print('Email:', email.text)
        print('Senha:', senha.text)

    except Exception as e:
        print(e)        
        # Fechar o navegador
        driver.quit()

