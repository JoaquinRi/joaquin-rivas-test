def suma(numero1, numero2):
    resultadoSuma = numero1 + numero2
    print("El resultado de la suma es: ", resultadoSuma)
    
#  -------------------------------------------------------------------------------------   
def resta(numero1, numero2):
    resultadoResta = numero1 - numero2
    print("El resultado de la resta es: ", resultadoResta)    
    
#  -------------------------------------------------------------------------------------   
def division(numero1, numero2):
    try:
        resultado = numero1 / numero2
            
    except ZeroDivisionError:
        print("No se puede dividir por 0, vuelva a intentarlo")
    print("El resultado de la division es: ", resultado)  
    
#  -------------------------------------------------------------------------------------   
def multiplicacion(numero1, numero2):
    resultadoMultiplicacion = numero1 * numero2
    print("El resultado de la multiplicacion es: ", resultadoMultiplicacion)  
    
# --------------------------------------------------------------------------------------
def acumulador():

    i = 0
    numeros = []
    
    print("Ingrese seis números: ")
    while i < 6:
        
        variable = int(input())
        
        if(variable <= 0):
            print("El numero ingresado es menor o igual a 0 , vuelva a intentarlo")
            print("Ingrese numeros validos hasta completar el cupo")
            
            continue
        
        else:
            numeros.append(variable)
        i += 1
        
    print("Numeros ingresados validos: ", numeros)   

#  -------------------------------------------------------------------------------------       
def pares_impares():
    
    pares = []
    impares = []
    
    
    print("Ingrese diez números: ")
    variable = 0
    while (variable < 10):
        numero = int(input( ))
        
        if numero % 2 == 0:
            pares.append(numero)
        else: 
            impares.append(numero)
            
        variable += 1
        
    print ("Los numeros pares son: ", pares )
    print ("Los numeros impares son: ", impares )