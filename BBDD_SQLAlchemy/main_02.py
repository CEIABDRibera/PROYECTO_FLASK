import db
from models import Producto

def run():
    arroz = Producto('Arroz', 1.25) # preparamos el objeto
    db.session.add(arroz) # se añade a la sesión
    print(arroz.id) # imprimimos el id (None por ahora)
    agua = Producto('Agua', 0.3)
    db.session.add(agua)
    db.session.commit() # guardamos los cambios
    print(arroz.id) # mostramos el id del nuevo producto ya en la tabla


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Crea la tabla, si no existe. Se debe haber importado el modelo previamente.
    run()