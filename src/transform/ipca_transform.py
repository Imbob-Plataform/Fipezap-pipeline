import pandas as pd

class TransformIPCA:
   def __init__(self, data) -> None:
      self._data = pd.DataFrame(data)
      self._df = None

   def transform(self):
      self.rename_columns()
      self.transform_column_date()
      self.transform_column_value()
      return self._data

   def rename_columns(self):
      rename_columns = {'data': 'periodo', 'valor': 'valor'}
      self._data =  self._data.rename(columns=rename_columns)

   def transform_column_date(self):
      self._data['periodo'] = self._data['periodo'].astype(str)
      self._data['periodo']= pd.to_datetime(self._data['periodo'], dayfirst=True)

   def transform_column_value(self):
      self._data['valor'] = self._data['valor'].astype(float)
