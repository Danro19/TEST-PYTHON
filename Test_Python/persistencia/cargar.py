def cargar_archivo(nombre_archivo):
    ruta = (f"utils/{nombre_archivo}.dat")
    try:
        with open(ruta, "r") as fd:
            cad=fd.read()
            return cad
    except FileNotFoundError:
        print(f"Archivo {nombre_archivo} no existe")
        nombre_archivo={}



productos = cargar_archivo('productos')
#productos = cargar_archivo('productos')

productos1=productos.split(",")
productos1=productos.split("\n")
prod={}
prod[0] = {"DESCPROD": 1, "VALORUNIT":2}
prod=productos
print(prod)






# fd = open ("utils/clientes.dat","r")

# cad=fd.read()#trae una lista de cadenas, con su respectivo "\n" cada elemento es una linea del archivo


# fd.close()