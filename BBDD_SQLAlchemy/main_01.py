import db
from models import Producto

def run():
    pass


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Crea la tabla, si no existe. Se debe haber importado el modelo previamente.
    run()