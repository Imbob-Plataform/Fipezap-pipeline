from src.schemas.ipca_schema import IPCASchema

def df_to_pydantic_list(df):
   records = df.to_dict(orient='records')
   pydantic_objs = [IPCASchema(**record) for record in records]
   return pydantic_objs
