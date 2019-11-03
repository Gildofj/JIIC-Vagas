import csv
import json
import pandas as pd
class Arquivo():

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

        #Saving
        df.to_csv('Vagas.csv')
        print('Armazenado com sucesso!')