from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class IPCAModel(Base):
   __tablename__ = "ipca_dados"

   id = Column(Integer, primary_key=True, autoincrement=True)
   periodo = Column(DateTime(timezone=True), nullable=False)
   valor = Column(Float, nullable=False)

