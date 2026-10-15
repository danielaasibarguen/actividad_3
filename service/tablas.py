from database import BASE, engine
from models import Persona

def crear_tablas()->None:
    BASE.metadata.create_all(bind=engine)
    