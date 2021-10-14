from Funciones import suma, resta, division, multiplicacion, pares_impares, acumulador

menu = ("""   
        -------Menú--------              
        1-> suma           
        2-> resta          
        3-> division       
        4-> multiplicacion 
        5-> pares e impares 
        6-> acumulador     
        7-> Salir          
        -------------------
        """)

print(menu)


opcionElegida = int(input("Ingrese una opción del menu: "))
print("Opcion elegida: ", opcionElegida)


#Si la opcion elegia es una de las primeras cuatro utiliza este if para darle valor a los parametros
while True:
    if(opcionElegida == 1 or opcionElegida == 2 or opcionElegida == 3 or opcionElegida == 4):
    
        num1 = int(input("Ingrese su primer numero: "))
        num2 = int(input("Ingrese su segundo numero: "))
    
        if (opcionElegida == 1):
            suma(num1, num2 )
            opcionElegida = int(input("ingrese una nueva opcion: "))
        
        elif (opcionElegida == 2):
            resta(num1, num2 )
            opcionElegida = int(input("ingrese una nueva opcion: "))
        
        elif (opcionElegida == 3):
            division(num1, num2 )
            opcionElegida = int(input("ingrese una nueva opcion: ")) 
        
        elif (opcionElegida == 4):
            multiplicacion(num1, num2 )
            opcionElegida = int(input("ingrese una nueva opcion: "))    
          
    elif (opcionElegida == 5):
        pares_impares()
        opcionElegida = int(input("ingrese una nueva opcion: "))
    
    elif (opcionElegida == 6):
        acumulador()
        opcionElegida = int(input("ingrese una nueva opcion: ")) 

    elif (opcionElegida == 7):
        print("A salido con exito")
        break
    
    else:
        print("Su opcion no se encuentra en el menu, por favor reintentelo")
        opcionElegida = int(input("ingrese una nueva opcion: "))