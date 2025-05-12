import csv
from models import HerramientaDigital

FILE_PATH_HERRAMIENTAS = "herramientas.csv"

def cargar_herramientas() -> list[HerramientaDigital]:
    try:
        with open(FILE_PATH_HERRAMIENTAS, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [HerramientaDigital(**{
                "id": int(row["id"]),
                "nombre": row["nombre"],
                "version": row["version"],
                "licencia": row["licencia"],
                "activo": row["activo"].lower() == "true"
            }) for row in reader]
    except FileNotFoundError:
        return []

def guardar_herramientas(herramientas: list[HerramientaDigital]):
    with open(FILE_PATH_HERRAMIENTAS, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "nombre", "version", "licencia", "activo"])
        writer.writeheader()
        for h in herramientas:
            writer.writerow(h.dict())

def agregar_herramienta(h: HerramientaDigital):
    herramientas = cargar_herramientas()
    if any(x.id == h.id for x in herramientas):
        raise ValueError("ID ya existente")
    herramientas.append(h)
    guardar_herramientas(herramientas)

FILE_PATH_HERRAMIENTAS = 'herramientas.csv'

def eliminar_herramienta_por_id(herramienta_id: int):
    filas_actualizadas = []
    encontrado = False

    with open(FILE_PATH_HERRAMIENTAS, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if int(fila["id"]) == herramienta_id:
                fila["activo"] = "False"
                encontrado = True
            filas_actualizadas.append(fila)

    if not encontrado:
        return False

    with open(FILE_PATH_HERRAMIENTAS, mode='w', newline='', encoding='utf-8') as archivo:
        campos = ["id", "nombre", "version", "licencia", "activo"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(filas_actualizadas)

    return True


def buscar_por_nombre_h(nombre: str) -> list[HerramientaDigital]:
    return [h for h in cargar_herramientas() if h.activo and nombre.lower() in h.nombre.lower()]

def filtrar_por_licencia(licencia: str) -> list[HerramientaDigital]:
    return [h for h in cargar_herramientas() if h.activo and h.licencia.lower() == licencia.lower()]

def actualizar_herramienta(h: HerramientaDigital) -> bool:
    herramientas = cargar_herramientas()
    actualizado = False

    for i, herramienta in enumerate(herramientas):
        if herramienta.id == h.id:
            herramientas[i] = h
            actualizado = True
            break




