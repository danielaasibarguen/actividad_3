from database import SessionLocal
from models import Personal

def insertar_persona(
nombre: str, apellido: str, edad: int, correo: str, telefono: str, direccion: str, profesion: str, ciudad: str, genero: str) -> Personal:
    db = SessionLocal()
    if not 0<= edad <= 120:
        raise ValueError("La edad debe estar entre 0 y 120")

    nueva_persona = Personal(
        nombre=nombre,
        apellido=apellido,
        edad=edad,            
        correo=correo,
        telefono=telefono,
        direccion=direccion,
        profesion=profesion,
        ciudad=ciudad,
        genero=genero
    )
    with SessionLocal.begin() as session:
        session.add(nueva_persona)
        #session.commit()
        #session.refresh(nueva_persona)
        session.flush()
        persona_id = nueva_persona.id
    return persona_id
   
        