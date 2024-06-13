#creando una funcion que nos devuelva los numeros primos
# entre el 0 y el argumento que pasamos

def es_primo (num):
    for i in range (2,num -1):
        if num%i==0: return False
    return True   

def primos_hasta (num):
    primos = []
    for i in range (3,num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
#devolvemos la lista
    return primos


#creamos el resultado llamando a la funcion y la mostramos
resultado = es_primo(13)      
print (resultado)