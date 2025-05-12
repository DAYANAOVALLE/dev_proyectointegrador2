import csv
from models import Asset

RUTA_ASSETS = "assets.csv"

def cargar_assets() -> list[Asset]:
    try:
        with open(RUTA_ASSETS, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [Asset(**{
                "id": int(row["id"]),
                "nombre": row["nombre"],
                "tipo": row["tipo"],
                "autor": row["autor"],
                "año": int(row["año"]),
                "activo": row["activo"].lower() == "true"
            }) for row in reader]
    except FileNotFoundError:
        return []

def guardar_assets(assets: list[Asset]):
    with open(RUTA_ASSETS, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nombre", "tipo", "autor", "año", "activo"])
        writer.writeheader()
        for asset in assets:
            writer.writerow(asset.dict())

def agregar_asset(asset: Asset):
    assets = cargar_assets()
    if any(a.id == asset.id for a in assets):
        raise ValueError("ID ya existente")
    assets.append(asset)
    guardar_assets(assets)

FILE_PATH_ASSETS = 'assets.csv'
def eliminar_asset_por_id(asset_id: int):
    filas_actualizadas = []
    encontrado = False

    with open(FILE_PATH_ASSETS, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if int(fila["id"]) == asset_id:
                fila["activo"] = "False"
                encontrado = True
            filas_actualizadas.append(fila)

    if not encontrado:
        return False

    with open(FILE_PATH_ASSETS, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ["id", "nombre", "tipo", "autor", "año", "activo"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas_actualizadas)

    return True

def buscar_por_nombre(nombre: str) -> list[Asset]:
    return [a for a in cargar_assets() if a.activo and nombre.lower() in a.nombre.lower()]

def filtrar_por_tipo(tipo: str) -> list[Asset]:
    resultados = [a for a in cargar_assets() if a.activo and a.tipo.lower() == tipo.lower()]
    if not resultados:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No se encontraron assets del tipo '{tipo}'."
        )
    return resultados

def actualizar_asset(asset_actualizado: Asset) -> bool:
    assets = cargar_assets()
    actualizado = False

    for i, asset in enumerate(assets):
        if assets[i].id == asset_actualizado.id:
            assets[i] = asset_actualizado
            actualizado = True
            break

    if actualizado:
        guardar_assets(assets)
    return actualizado

