#creando una funcion que muestre la serie fibonacci entre el 0 y el numero dado
#entre el 0 y el argumento que pasamos 

def es_primo(num):
    for i in range (2,num-1):
        if num%i==0 : return False
    return True

def primos_hasta (num):
    primos= []
    for i in range (3,num+1):
        resultado= es_primo(i)  
        if resultado == True : primos.append (i)
    return primos
resultado = primos_hasta (98)
print(resultado)    