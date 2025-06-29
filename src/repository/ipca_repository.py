from src.db.connection import SessionLocal
from src.models.ipca_model import IPCAModel

def save_ipca_data(data_list):
   db = SessionLocal()
   try:
      for i,item in enumerate(data_list):
         db_item = IPCAModel(
               valor=item.valor,
               periodo=item.periodo,
            )
         db.add(db_item)
      db.commit()
   except Exception as e:
      db.rollback()
      print(f"Erro ao salvar dados: {e}")
   finally:
      db.close()
