from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Asset(Base):
    __tablename__ = "assets"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    tipo = Column(String)
    autor = Column(String)
    anio = Column(Integer)
    activo = Column(Boolean)

class Herramienta(Base):
    __tablename__ = "herramientas"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    version = Column(String)
    licencia = Column(String)
    activo = Column(Boolean)
