from sqlalchemy.orm import Session
from models import Herramienta
from fastapi import HTTPException
import che

def get_all_herramientas(db: Session):
    return db.query(Herramienta).filter(Herramienta.activo == True).all()

def get_herramienta_by_id(db: Session, herramienta_id: int):
    herramienta = db.query(Herramienta).filter(Herramienta.id == herramienta_id, Herramienta.activo == True).first()
    if not herramienta:
        raise HTTPException(status_code=404, detail="Herramienta no encontrada")
    return herramienta

def create_herramienta(db: Session, herramienta: che.HerramientaCreate):
    db_herramienta = Herramienta(**herramienta.dict())
    db.add(db_herramienta)
    db.commit()
    db.refresh(db_herramienta)
    return db_herramienta

def delete_herramienta(db: Session, herramienta_id: int):
    herramienta = db.query(Herramienta).filter(Herramienta.id == herramienta_id).first()
    if not herramienta:
        raise HTTPException(status_code=404, detail="Herramienta no encontrada")
    herramienta.activo = False
    db.commit()
    return {"mensaje": "Herramienta eliminada lógicamente"}

def buscar_herramienta_por_nombre(db: Session, nombre: str):
    return db.query(Herramienta).filter(Herramienta.activo == True, Herramienta.nombre.ilike(f"%{nombre}%")).all()

def filtrar_herramienta_por_licencia(db: Session, licencia: str):
    resultados = db.query(Herramienta).filter(Herramienta.activo == True, Herramienta.licencia.ilike(licencia)).all()
    if not resultados:
        raise HTTPException(status_code=404, detail=f"No se encontraron herramientas con licencia '{licencia}'.")
    return resultados

def actualizar_herramienta(db: Session, herramienta: che.HerramientaRead):
    db_herramienta = db.query(Herramienta).filter(Herramienta.id == herramienta.id).first()
    if not db_herramienta:
        raise HTTPException(status_code=404, detail="Herramienta no encontrada")
    for key, value in herramienta.dict().items():
        setattr(db_herramienta, key, value)
    db.commit()
    db.refresh(db_herramienta)
    return db_herramienta
