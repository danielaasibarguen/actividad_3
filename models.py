from sqlalchemy import CheckConstraint, Column, Integer, String
from alchemy.orm import Mapped, mapped_column
from database import Base

class Personal(Base):
    __tablename__ = "personas_Daniela_Alejandra_Salazar_Ibarguen"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    apellido: Mapped[str] = mapped_column(String(50), nullable=False)
    edad: Mapped[int] = mapped_column(Integer, nullable=False)
    correo: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    telefono: Mapped[str] = mapped_column(String(20), nullable=False)
    direccion: Mapped[str] = mapped_column(String(200), nullable=False)
    profesion: Mapped[str] = mapped_column(String(100), nullable=False)
    ciudad: Mapped[str] = mapped_column(String(100), nullable=False)
    genero: Mapped[str] = mapped_column(String(10), nullable=False)

