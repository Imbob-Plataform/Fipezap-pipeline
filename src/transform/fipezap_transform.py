import pandas as pd

class TransformFipezap:
   def __init__(self, data) -> None:
      self._data = data
      self._df = None

   def transform(self):
      for aba, df in self._data.items():
         print(f"Aba: {aba}")
         print(f"{df.tail()}")
