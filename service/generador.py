from uuid import uuid4
from Faker import Faker
from sqlalchemy import insert
from database import SessionLocal
from models import Personal

def generar_personas(
    cantidad: int, 
    tamano_lote: int = 1000,
    locale: str = "es_CO",
)-> None:
    faker = Faker(locale)

    identificador_ejecucion = uuid4().hex
    for i in range(cantidad):

        fin= min(i + tamano_lote, cantidad)

        nombre = faker.first_name()
        apellido = faker.last_name()
        edad = faker.random_int(min=0, max=120)
        telefono = faker.phone_number()
        direccion = faker.address()
        profesion = faker.job()
        ciudad = faker.city()
        genero = faker.random_element(elements=("Masculino", "Femenino"))

        personas = [
            {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "correo": (
                    f"{faker.user_name}"
                    f"{identificador_ejecucion}"
                    f"{i}@{faker.free_email_domain()}"
                ),
                "telefono": telefono,
                "direccion": direccion,
                "profesion": profesion,
                "ciudad": ciudad,
                "genero": genero
            } 
            for persona in range(i, fin)
        ]

        with SessionLocal.begin() as session:
            session.execute(
                insert(Personal), personas)

