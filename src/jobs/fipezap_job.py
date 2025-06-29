from src.extract.fipezap_extractors import HttpFipezap
from src.transform.fipezap_transform import TransformFipezap
# from src.utils.df_to_pydantic import df_to_pydantic_list
# from src.repository.ipca_repository import save_ipca_data
# from src.db.init_db import init_db

import pandas as pd

class PipelineIPCA:
   def __init__(self) -> None:
      self.extract = HttpFipezap.getExcelJson().getHttpData('src/data/')
      if self.extract is None:
         raise ValueError("Falha ao carregar configuração do arquivo 'src/data/'")

   def run_pipeline(self):
      data = self.extract.readExcelAbas() # type: ignore

      if not data or data is None:
         print("Falha ao obter dados da api")
         return

      data_process = TransformFipezap(data).transform()

      # if data_process is None or data_process.empty:
      #    print('falha na transformação da api')
      #    return

      # try:
      #    valid_data = df_to_pydantic_list(data_process)
      #    save_ipca_data(valid_data)
      # except Exception as e:
      #    raise ValueError("Não consegui validar os dados.")
      # else:
      #    print('dados processados')

if __name__ == '__main__':
   pipeline = PipelineIPCA()
   pipeline.run_pipeline()
