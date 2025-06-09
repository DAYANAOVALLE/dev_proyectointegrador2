from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Reemplaza estos valores con tu cadena real de conexión
# Ejemplo:
import os
DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencia para usar en FastAPI
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
