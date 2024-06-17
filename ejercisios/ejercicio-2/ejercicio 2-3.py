#creando una funcion que muestre la serie fibonacci entre el 0 y el numero dado
#entre el 0 y el argumento que pasamos 

#creando una funcion que verifique si es un numero primo
def es_primo(num):
    
 # verificamos que el numeropasado no pueda dividirse
 #por ningun numero entre 2 y ese mismo numero -1
    for i in range (2,num-1):
        #si es divisible por alguno retomamos false y termina el bucle
        
        if num%i==0 : return False
     # si termina el bucle, significa que no fue divisible entonces es primo   
    return True

#creando una funcion que retome una lista con todos los primos
def primos_hasta (num):
    #creamos la lista
    primos= []
    for i in range (3,num+1):
        #verificamos si el valor es primo
        
        resultado= es_primo(i)  
        # en caso de que sea lo agregamos a la lista
        if resultado == True : primos.append (i)
     #devolvemos la lista   
    return primos
#creamos el resultado llamando a la funcion
resultado = primos_hasta (98)
print(resultado)    