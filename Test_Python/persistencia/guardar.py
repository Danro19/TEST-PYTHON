


def guardar(datos, nombre):
    ruta_archivo = f"utils/{nombre}.dat"

    
    try:
        with open(ruta_archivo, "r") as fd:
            contenido=fd.read()
            if not isinstance(contenido, dict):
                fd=open(ruta_archivo, "W")    
                contenido = {}
    except FileNotFoundError:
        contenido = {}

    
    if datos:  
        contenido.setdefault(datos) 
  
    with open(ruta_archivo, 'w') as fd:
        fd.write(contenido)



def cargar_datos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos=file.write(file)
    return datos
    



fd = open("utils/data4.dat","w")
contenido=["listo para divertirme" ]
contenido1=("Phyton es divertido...\n")
contenido.append(contenido1)
fd.writelines(contenido)
fd.close()

    