from uuid import uuid4
from sqlachemy import func, select
from config import(
    TOTAL_PERSONAS,
    BATCH_SIZE,
    FAKER_LOCALE
)
from database import SessionLocal
from models import Personal
from services.tablas import crear_tablas
from services.generador import generar_personas
from services.personas import insertar_persona

def contar_personas() -> int:
    with SessionLocal.begin() as session:
        total = session.scalar(select(func.count(Personal.id)))
    return int(total or 0)

def main() -> None:
    crear_tablas()
    print("Tablas creadas correctamente.")
    correo_prueba= (f"daniela.{uuid4().hex}@{Faker().free_email_domain()}")
    persona_id = insertar_persona(
        nombre="Daniela",
        apellido="Gómez",
        edad=25,
        telefono="1234567890",
        direccion="Calle 123 # 45-67",
        profesion="Ingeniera",
        ciudad="Bogotá",
        genero="Femenino"
    )
    print(f"Persona insertada con ID: {persona_id}")

    generar_personas(
        cantidad=TOTAL_PERSONAS,
        tamano_lote=BATCH_SIZE,
        locale=FAKER_LOCALE
    )

    total= contar_personas()
    print(f"Total de personas en la base de datos: {total}")

if __name__ == "__main__":
    main()