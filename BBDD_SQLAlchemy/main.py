import db
from models import Producto

def run():
    consulta = db.session.query(Producto) # generamos la variable consulta
    # print(consulta)

    # mostramos todos los registros de la tabla
    productos = db.session.query(Producto).all()
    print("Lista de todos los productos: ", productos)

    ob = db.session.get(Producto, 1) # obtenemos el primer registro de la tabla
    print("Primer producto: ", ob.nombre)

    num_productos = db.session.query(Producto).count() # total de registros
    print("Cantidad de productos en la tabla: ", num_productos)

    agua = db.session.query(Producto).filter_by(nombre='Agua').first() # filtramos por nombre
    print("Productos con nombre 'agua': ", agua)

    menos_de_1 = db.session.query(Producto).filter(Producto.precio < 1).all() # filtramos por precio
    print("Productos de menos de 1 eur.: ", menos_de_1)

if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Crea la tabla, si no existe. Se debe haber importado el modelo previamente.
    run()