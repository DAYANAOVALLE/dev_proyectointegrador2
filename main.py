from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from database import get_db
from crud_assets import *
from crud_herramientas import *
import che
import os

port = int(os.environ.get("PORT", 8000))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=port)


app = FastAPI()

# ---------- ASSETS ----------
@app.get("/assets/", response_model=list[che.AssetRead], tags=["Assets"])
def get_assets(db: Session = Depends(get_db)):
    return get_all_assets(db)

@app.post("/assets/", response_model=che.AssetRead, status_code=201, tags=["Assets"])
def crear_asset(asset: che.AssetCreate, db: Session = Depends(get_db)):
    return create_asset(db, asset)

@app.get("/assets/{asset_id}", response_model=che.AssetRead, tags=["Assets"])
def get_asset(asset_id: int, db: Session = Depends(get_db)):
    return get_asset_by_id(db, asset_id)

@app.delete("/assets/{asset_id}", tags=["Assets"])
def eliminar_asset(asset_id: int, db: Session = Depends(get_db)):
    return delete_asset(db, asset_id)

@app.get("/assets/buscar/", response_model=list[che.AssetRead], tags=["Assets"])
def buscar_asset(nombre: str, db: Session = Depends(get_db)):
    return buscar_asset_por_nombre(db, nombre)

@app.get("/assets/filtrar/", response_model=list[che.AssetRead], tags=["Assets"])
def filtrar_assets(tipo: str, db: Session = Depends(get_db)):
    return filtrar_asset_por_tipo(db, tipo)

@app.put("/assets/", response_model=che.AssetRead, tags=["Assets"])
def actualizar_asset_endpoint(asset: che.AssetRead, db: Session = Depends(get_db)):
    return actualizar_asset(db, asset)

# ---------- HERRAMIENTAS ----------
@app.get("/herramientas/", response_model=list[che.HerramientaRead], tags=["Herramientas"])
def get_herramientas(db: Session = Depends(get_db)):
    return get_all_herramientas(db)

@app.post("/herramientas/", response_model=che.HerramientaRead, status_code=201, tags=["Herramientas"])
def crear_herramienta(h: che.HerramientaCreate, db: Session = Depends(get_db)):
    return create_herramienta(db, h)

@app.get("/herramientas/{herramienta_id}", response_model=che.HerramientaRead, tags=["Herramientas"])
def get_herramienta(herramienta_id: int, db: Session = Depends(get_db)):
    return get_herramienta_by_id(db, herramienta_id)

@app.delete("/herramientas/{herramienta_id}", tags=["Herramientas"])
def eliminar_herramienta(herramienta_id: int, db: Session = Depends(get_db)):
    return delete_herramienta(db, herramienta_id)

@app.get("/herramientas/buscar/", response_model=list[che.HerramientaRead], tags=["Herramientas"])
def buscar_herramienta(nombre: str, db: Session = Depends(get_db)):
    return buscar_herramienta_por_nombre(db, nombre)

@app.get("/herramientas/filtrar/", response_model=list[che.HerramientaRead], tags=["Herramientas"])
def filtrar_herramientas(licencia: str, db: Session = Depends(get_db)):
    return filtrar_herramienta_por_licencia(db, licencia)

@app.put("/herramientas/", response_model=che.HerramientaRead, tags=["Herramientas"])
def actualizar_herramienta_endpoint(h: che.HerramientaRead, db: Session = Depends(get_db)):
    return actualizar_herramienta(db, h)
