import csv
import json
import pandas as pd
import os
class Arquivo():

    def scrapy(self):
        os.system('cmd /c "scrapy crawl Vagas -o resultados.json"')


    def save(self):

        jsonfile = 'C:/Users/junio/OneDrive/Documentos/ScrapVagas/ScrapVagas/resultados.json'
        data = pd.read_json(jsonfile)
        data = data[pd.Index(['Titulo', 'Cidade', 'Salario', 'Descricao'])]
        df = pd.DataFrame(data)
        
        #Limpeza dos dados com o panda

        #Titulo
        df['Titulo'] = df['Titulo'].str.replace("'", "")
        df['Titulo'] = df['Titulo'].str.replace('"', '')
        df['Titulo'] = df['Titulo'].str.replace(',', '')
        df['Titulo'] = df['Titulo'].str.replace('!', '')
        df['Titulo'] = df['Titulo'].str.replace('<meta content=', '')
        df['Titulo'] = df['Titulo'].str.replace('>', '')
        #Cidade
        df['Cidade'] = df['Cidade'].str.replace('<span class=\"locality\"', '')
        df['Cidade'] = df['Cidade'].str.replace('>', '')
        df['Cidade'] = df['Cidade'].str.replace('span', '')
        df['Cidade'] = df['Cidade'].str.replace('<', '')
        df['Cidade'] = df['Cidade'].str.replace('/', '')
        df['Cidade'] = df['Cidade'].str.replace('"', '')
        df['Cidade'] = df['Cidade'].str.replace("'", "")
        #Salário
        df['Salario'] = df['Salario'].str.replace('<meta content=', '')
        df['Salario'] = df['Salario'].str.replace('>', '')
        df['Salario'] = df['Salario'].str.replace('"', '')
        df['Salario'] = df['Salario'].str.replace("'", "")
        df['Salario'] = df['Salario'].str.replace('null', 'A combinar')
        #Descricao
        df['Descricao'] = df['Descricao'].str.replace('<p>', '')
        df['Descricao'] = df['Descricao'].str.replace('</p>', '')
        df['Descricao'] = df['Descricao'].str.replace('#', '')
        df['Descricao'] = df['Descricao'].str.replace('<wbr>', '')
        df['Descricao'] = df['Descricao'].str.replace('</wbr>', '')

        #Saving
        df.to_csv('Vagas.csv')
        print('Armazenado com sucesso!')