from pydantic import BaseModel

class AssetBase(BaseModel):
    nombre: str
    tipo: str
    autor: str
    anio: int
    activo: bool

class AssetCreate(AssetBase):
    pass

class AssetRead(AssetBase):
    id: int

    class Config:
        orm_mode = True

class HerramientaBase(BaseModel):
    nombre: str
    version: str
    licencia: str
    activo: bool

class HerramientaCreate(HerramientaBase):
    pass

class HerramientaRead(HerramientaBase):
    id: int

    class Config:
        orm_mode = True
