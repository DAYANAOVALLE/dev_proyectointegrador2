from sqlalchemy.orm import Session
from models import Asset
from fastapi import HTTPException
import che

def get_all_assets(db: Session):
    return db.query(Asset).filter(Asset.activo ==True).all()

def get_asset_by_id(db: Session, asset_id: int):
    asset = db.query(Asset).filter(Asset.id == asset_id, Asset.activo == True).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset no encontrado")
    return asset

def create_asset(db: Session, asset: che.AssetCreate):
    db_asset = Asset(**asset.dict())
    db.add(db_asset)
    db.commit()
    db.refresh(db_asset)
    return db_asset

def delete_asset(db: Session, asset_id: int):
    asset = db.query(Asset).filter(Asset.id == asset_id).first()
    if not asset:
        raise HTTPException(status_code=404, detail="Asset no encontrado")
    asset.activo = False
    db.commit()
    return {"mensaje": "Asset eliminado lógicamente"}

def buscar_asset_por_nombre(db: Session, nombre: str):
    return db.query(Asset).filter(Asset.activo == True, Asset.nombre.ilike(f"%{nombre}%")).all()

def filtrar_asset_por_tipo(db: Session, tipo: str):
    resultados = db.query(Asset).filter(Asset.activo == True, Asset.tipo.ilike(tipo)).all()
    if not resultados:
        raise HTTPException(status_code=404, detail=f"No se encontraron assets del tipo '{tipo}'.")
    return resultados

def actualizar_asset(db: Session, asset: che.AssetRead):
    db_asset = db.query(Asset).filter(Asset.id == asset.id).first()
    if not db_asset:
        raise HTTPException(status_code=404, detail="Asset no encontrado")
    for key, value in asset.dict().items():
        setattr(db_asset, key, value)
    db.commit()
    db.refresh(db_asset)
    return db_asset
