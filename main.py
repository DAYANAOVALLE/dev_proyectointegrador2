from fastapi import FastAPI, HTTPException
from models import Asset, AssetVisual, HerramientaDigital, HerramientaVisual
from crud_assets import cargar_assets, agregar_asset, guardar_assets, buscar_por_nombre,eliminar_asset_por_id, filtrar_por_tipo, actualizar_asset
from crud_herramientas import cargar_herramientas, agregar_herramienta, guardar_herramientas,eliminar_herramienta_por_id, buscar_por_nombre_h, filtrar_por_licencia, actualizar_herramienta

app = FastAPI(
    title="Recurso Artístico de videojuegos API",
    description="API para gestionar assets y herramientas digitales relacionadas al desarrollo artistico de videojuegos"
)

@app.get("/")
def home():
    return {"mensaje": "Bienvenido a la API de recursos artísticos"}

# ---------------- ASSETS ----------------

@app.get("/assets/", response_model=list[AssetVisual], tags=["Assets"])
def get_assets():
    return [AssetVisual(**a.dict()) for a in cargar_assets() if a.activo]

@app.post("/assets/", status_code=201, tags=["Assets"])
def crear_asset(asset: Asset):
    try:
        agregar_asset(asset)
        return {"mensaje": "Asset agregado"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/assets/{asset_id}", response_model=AssetVisual, tags=["Assets"])
def get_asset(asset_id: int):
    for a in cargar_assets():
        if a.id == asset_id and a.activo:
            return AssetVisual(**a.dict())
    raise HTTPException(status_code=404, detail="Asset no encontrado")
@app.delete("/assets/{asset_id}", tags=["Assets"])
def delete_asset(asset_id: int):
    resultado = eliminar_asset_por_id(asset_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Asset no encontrado")
    return {"mensaje": "Asset eliminado (lógicamente)"}

@app.get("/assets/buscar/", tags=["Assets"])
def buscar_asset(nombre: str):
    return buscar_por_nombre(nombre)

@app.get("/assets/filtrar/", tags=["Assets"])
def filtrar_assets(tipo: str):
    return filtrar_por_tipo(tipo)

@app.put("/assets/", tags=["Assets"])
def endpoint_actualizar_asset(asset: Asset):
    if actualizar_asset(asset):  # Esta es la del crud_assets
        return {"mensaje": "Asset actualizado"}
    raise HTTPException(status_code=404, detail="Asset no encontrado")

# ---------------- HERRAMIENTAS ----------------

@app.get("/herramientas/", response_model=list[HerramientaVisual], tags=["Herramientas"])
def get_herramientas():
    return [HerramientaVisual(**h.dict()) for h in cargar_herramientas() if h.activo]

@app.post("/herramientas/", status_code=201, tags=["Herramientas"])
def crear_herramienta(h: HerramientaDigital):
    try:
        agregar_herramienta(h)
        return {"mensaje": "Herramienta agregada"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/herramientas/{herramienta_id}", response_model=HerramientaVisual, tags=["Herramientas"])
def get_herramienta(herramienta_id: int):
    for h in cargar_herramientas():
        if h.id == herramienta_id and h.activo:
            return HerramientaVisual(**h.dict())
    raise HTTPException(status_code=404, detail="No encontrada")

@app.delete("/herramientas/{herramienta_id}", tags=["Herramientas"])
def delete_herramienta(herramienta_id: int):
    resultado = eliminar_herramienta_por_id(herramienta_id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Herramienta no encontrada")
    return {"mensaje": "Herramienta eliminada correctamente"}

@app.get("/herramientas/buscar/", tags=["Herramientas"])
def buscar_herramienta(nombre: str):
    return buscar_por_nombre_h(nombre)

@app.get("/herramientas/filtrar/", tags=["Herramientas"])
def filtrar_herramientas(licencia: str):
    return filtrar_por_licencia(licencia)

@app.put("/herramientas/", tags=["Herramientas"])
def endpoint_actualizar_herramienta(h: HerramientaDigital):
    if actualizar_herramienta(h):  # Esta es la del crud_herramientas
        return {"mensaje": "Herramienta actualizada"}
    raise HTTPException(status_code=404, detail="Herramienta no encontrada")
