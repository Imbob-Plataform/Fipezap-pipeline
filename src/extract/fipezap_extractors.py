import json
import requests
import pandas as pd
import os


class HttpFipezap:
   def __init__(self, url: str = '', nomeApi: str = '') -> None:
      self._nomeApi = nomeApi
      self._url = url
      self.dataframe = None

   @classmethod
   def getExcelJson(cls):
      try:
         with open('api.json', 'r') as file:
            content = json.load(file)
      except FileNotFoundError:
         raise ValueError('Não encontrei o arquivo')
      except FileExistsError:
         raise ValueError('Não existe o arquivo')
      else:
         return cls(url=content['url'],nomeApi=content['nomeApi'])

   def getHttpData(self,root):
      try:
         r = requests.get(self._url)
         print(f"Status code: {r.status_code}")
         if r.status_code == 200:
            with open(f'{root}{self._nomeApi}.xlsx', 'wb') as f:
               f.write(r.content)
            print("extração concluída!")
         return self
      except requests.exceptions.RequestException as e:
         raise ValueError('Não consegui fazer o metodo HTTP -> GET')

   def readExcelAbas(self):
      file_path = 'src/data/fipezap-serieshistoricas.xlsx'
      try:
         if os.path.exists(file_path):
            self.dataframe = pd.read_excel(file_path, sheet_name=None)
            print("Consegui ler o excel")
         else:
            print("Arquivo não encontrado", file_path)
      except Exception as e:
         raise ValueError("Erro ao ler o Excel", e)
      return self.dataframe
