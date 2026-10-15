from database import Base, engine
from models import Personal

def crear_tablas()->None:
    Base.metadata.create_all(bind=engine)
