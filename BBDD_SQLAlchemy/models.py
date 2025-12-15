import db
# MAPEO CLASE - TABLA
from sqlalchemy import Column, Integer, String, Float

class Producto(db.Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    precio = Column(Float)

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f'Producto {self.nombre}, {self.precio}'

    def __str__(self):
        return self.nombre
