def menu():
    
    while True:
       
        
        
            
        print( "╔╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╗")
        print( "╠╬╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╬╣")
        print( "╠╣                                                         ╠╣")
        print( "╠╣                                                         ╠╣")
        print( "╠╣      ▄▄▄▄███▄▄▄▄      ▄████████ ███▄▄▄▄   ███    █▄     ╠╣")
        print( "╠╣    ▄██▀▀▀███▀▀▀██▄   ███    ███ ███▀▀▀██▄ ███    ███    ╠╣")
        print( "╠╣    ███   ███   ███   ███    █▀  ███   ███ ███    ███    ╠╣")
        print( "╠╣    ███   ███   ███  ▄███▄▄▄     ███   ███ ███    ███    ╠╣")
        print( "╠╣    ███   ███   ███ ▀▀███▀▀▀     ███   ███ ███    ███    ╠╣")
        print( "╠╣    ███   ███   ███   ███    █▄  ███   ███ ███    ███    ╠╣")
        print( "╠╣    ███   ███   ███   ███    ███ ███   ███ ███    ███    ╠╣")
        print( "╠╣     ▀█   ███   █▀    ██████████  ▀█   █▀  ████████▀     ╠╣")
        print( "╠╣                                                         ╠╣")
        print( "╠╣                                                         ╠╣")
        print( "╠╬╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╦╬╣")
        print( "╚╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╩╝")
        
        print(""*10)   
        print("="*40)
        print("a. Imprimir Factura")
        print("b. Imprimir resumen de todas las facturas de un cliente determinado.")
        print("c. Imprimir Diagrama de barra")
        print("d. Informe de los productos mas comunes.")
        print(">> Ingresar a opcion: ", end="")
        try:
            opciones = ["a", "b", "c","d"]
            opc = input().lower()
            if opc not in opciones:
                print("Error opcion invalida")
                print("presione cualquier tecla para volver al menu. \n")
            return opc
        
        except ValueError:
            print("ingreso una opcion incorrecta")
            print("presione cualquier tecla para volver al menu. \n")