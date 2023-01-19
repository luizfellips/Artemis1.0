from time import sleep
from selenium import webdriver
import pandas as pd
from Structures import Functionalities

class InitializeProgram(Functionalities.DriverFunctions):
    def __init__(self) -> None:
        print('*'*10)
        print('Seja bem-vindo ao Artemis 1.0')
        print('*'*10)
        input('Pressione qualquer tecla para inicializar os processos.')
        sleep(1)
        print('Inicializando...')
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.driver = webdriver.Chrome(executable_path='C:\\Users\\LENOVO T430\\Documents\\GitHub\\Bot2.0\\chromedriver.exe',options=self.options)
        self.driver.get('https://web.whatsapp.com')
        input('Conecte-se ao WhatsApp e pressione qualquer tecla para continuar.')
        sleep(1)
        self.print_system_informations()
        self.LoadMenu()

    def print_system_informations(self):
        string_phrase = 'ARTEMIS 1.0'
        print('*'*(len(string_phrase)+5))
        print(string_phrase)
        print('*'*(len(string_phrase)+5))

    def LoadMenu(self) -> None:
        self.products_df = pd.read_excel('C:\\Users\\LENOVO T430\\Documents\\GitHub\\Bot2.0\\files\\products.xlsx')
        self.contacts_df = pd.read_excel('C:\\Users\\LENOVO T430\\Documents\\GitHub\\Bot2.0\\files\\contacts.xlsx')
        locations_list = self.products_df['LOCATION'].tolist()
        descriptions_list = self.products_df['DESCRIPTION'].tolist()
        while True:
            print(f'[1] Iniciar envios \n[2]Sair')
            operation = int(input('\n>'))
            if operation == 1:
                for i in range(0,len(self.contacts_df)):
                    self.get_contacts(self.contacts_df.loc[i,'CONTACTS'])
                    sleep(1)
                    for j in range(0,len(locations_list)):
                        self.send_message(locations_list[j],descriptions_list[j])
                        sleep(2)
                print('*'*15)
                print('ENVIOS FINALIZADOS')
                print('*'*15)
                self.print_system_informations()
            else:
                break
