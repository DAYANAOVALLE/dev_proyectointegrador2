from pydantic import BaseModel

class Asset(BaseModel):
    id: int
    nombre: str
    tipo: str
    autor: str
    año: int
    activo: bool = True

class AssetVisual(BaseModel):
    id: int
    nombre: str
    tipo: str
    autor: str
    año: int

class HerramientaDigital(BaseModel):
    id: int
    nombre: str
    version: str
    licencia: str
    activo: bool = True

class HerramientaVisual(BaseModel):
    id: int
    nombre: str
    version: str
    licencia: str