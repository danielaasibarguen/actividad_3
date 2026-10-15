from uuid import uuid4
from faker import Faker
from sqlalchemy import insert

from database import SessionLocal
from models import Personal


def generar_personas(
    cantidad: int,
    tamano_lote: int = 1000,
    locale: str = "es_CO",
) -> None:

    # Inicializar Faker.
    faker = Faker(locale)

    # Generar un identificador único por ejecución.
    identificador_ejecucion = uuid4().hex

    # Validar parámetros.
    if cantidad <= 0:
        raise ValueError("La cantidad debe ser mayor que cero")

    if tamano_lote <= 0:
        raise ValueError("El tamaño del lote debe ser mayor que cero")

    # Recorrer los registros por lotes.
    for inicio in range(0, cantidad, tamano_lote):

        # Calcular el límite del lote actual.
        fin = min(inicio + tamano_lote, cantidad)

        # Lista que almacenará las personas del lote.
        personas = []

        # Generar una persona diferente en cada iteración.
        for i in range(inicio, fin):

            persona = {
                "nombre": faker.first_name(),

                "apellido": faker.last_name(),

                "edad": faker.random_int(
                    min=0,
                    max=120
                ),

                # El identificador y el contador
                # permiten generar correos únicos.
                "correo": (
                    f"persona_{identificador_ejecucion}_{i}"
                    "@example.com"
                ),

                "telefono": faker.phone_number(),

                "direccion": faker.address(),

                "profesion": faker.job(),

                "ciudad": faker.city(),

                "genero": faker.random_element(
                    elements=("Masculino", "Femenino")
                )
            }

            # Agregar la persona a la lista.
            personas.append(persona)

        # Insertar todas las personas del lote.
        with SessionLocal.begin() as session:

            session.execute(
                insert(Personal),
                personas
            )

        print(
            f"Insertados {fin} de {cantidad} registros"
        )