# Creamos el db engine
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///data.db') # Creamos el engine y, en el momento de crearlo, creamos la BBDD

Session = sessionmaker(bind=engine) # Crear una sesión de base de datos usando el engine y sessionmaker
session = Session() # Llamada a Session para obtener la sesión.

# Modelos

Base = declarative_base() # clase que nos permite definir nuestras clases de datos. Permite mapear las tablas de la BBDD.


