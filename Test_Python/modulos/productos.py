


def cargar_archivo(nombre_archivo):
    ruta = (f"utils/{nombre_archivo}.dat")
    try:
        with open(ruta, "r") as fd:
            cad=fd.read()
            return cad
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo} no existe")
        nombre_archivo={}



def leerProductos():
    productos = cargar_archivo('productos')
    productos2=productos.split(",")
    prod={}
    codigoProducto=0
    prod[codigoProducto] = {"DESCPROD": 1, "VALORUNIT":2}
    prod=productos
    return prod

def leerclientes():
    clientes = cargar_archivo('clientes')
    clientes2=clientes.split(",")
    client={}
    client[clientes] = {"nombre": 1, "telefono":2}
    return client

#print(type(leerProductos()))
#print(leerclientes()) 

clientes = cargar_archivo('clientes')
clientes2=clientes.split(",")
print(type(clientes2))
print(clientes2)
