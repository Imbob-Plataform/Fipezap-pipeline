from src.extract.ipca_extractors import HttpIPCA
from src.transform.ipca_transform import TransformIPCA
from src.utils.df_to_pydantic import df_to_pydantic_list
from src.repository.ipca_repository import save_ipca_data
from src.db.init_db import init_db

import pandas as pd

class PipelineIPCA:
   def __init__(self) -> None:
      self.extract = HttpIPCA.from_json('api.json')
      if self.extract is None:
         raise ValueError("Falha ao carregar configuração do arquivo 'api.json'")

   def run_pipeline(self):
      data = self.extract.get_http_ipca() # type: ignore
      if not data or data is None:
         print("Falha ao obter dados da api")
         return

      data_process = TransformIPCA(data).transform()

      if data_process is None or data_process.empty:
         print('falha na transformação da api')
         return

      try:
         valid_data = df_to_pydantic_list(data_process)
         save_ipca_data(valid_data)
      except Exception as e:
         raise ValueError("Não consegui validar os dados.")
      else:
         print('dados processados')

if __name__ == '__main__':
   init_db()
   pipeline = PipelineIPCA()
   pipeline.run_pipeline()
