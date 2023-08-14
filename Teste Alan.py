from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Robo_Pesquisa:
    def __init__(self):
        self.SITE_LINK = "https://google.com.br/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def abrir_pesquisa(self):
        self.driver.get(self.SITE_LINK)
        time.sleep(5)

    def realizar_pesquisa_google(self, query):
        text_box = self.driver.find_element(By.NAME, "q")
        text_box.send_keys(query)
        text_box.send_keys(Keys.RETURN)
        time.sleep(10)

    def extrair_informacoes_resultado(self):
        #informações do Titulo
        result_titulo = self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]')
        text_titulo = result_titulo.text
        print("Resultado da pesquisa:", text_titulo)
        #informações do Subtitulo
        result_subtitulo = self.driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[2]/div/span')
        text_subtitulo = result_subtitulo.text
        print(text_subtitulo)
        time.sleep(20)

    def fechar_navegador(self):
        self.driver.quit()

# Instância da classe Robo_Pesquisa
pesquisa = Robo_Pesquisa()

# Abrir a pesquisa
pesquisa.abrir_pesquisa()

# Fazer a pesquisa
pesquisa.realizar_pesquisa_google("Autovist")

# Extrair informações do resultado
pesquisa.extrair_informacoes_resultado()

# Fechar o navegador
pesquisa.fechar_navegador()