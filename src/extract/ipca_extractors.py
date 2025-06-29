import json
import requests
import pandas as pd

class HttpFipezap:
   def __init__(self, url: str = '', nomeApi: str = '', data: pd.DataFrame = None) -> None:
      self._nomeApi = nomeApi
      self._data = data or {}
      self._tables = []

   @classmethod
   def from_excel(cls, caminho_excel: str):
      try:
         excel_data_df = pd.ExcelFile(f'{caminho_excel}')
         nome_api = caminho_excel[9:16]
      except FileNotFoundError:
         print("Arquivo Excel não encontrado.")
         return None
      else:
         return cls(data=excel_data_df,nomeApi=nome_api)

   def __str__(self):
      return f'Nome: {self._nomeApi} dos dados'

   def get_excel_abas_fipezap(self):
      try:
         for i,abas in enumerate(self._data):

         return self._data
      except requests.exceptions.RequestException as e:

         return None

h = HttpFipezap().from_excel(r'src/data/fipezap.xlsx')
if h:
   h.get_excel_abas_fipezap()
