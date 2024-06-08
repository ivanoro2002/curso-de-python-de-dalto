# falto el profe y los pibes van a armar la clase
#pedir el nombre y la edad de los compañeros que vinieron hoy a clase
def obtener_compañeros(cantidad_de_compañeros):
   
#creando la lista de compañeros
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        
        nombre = input("Ingrese el nombre del compañero: ") 
        edad = int(input("Ingrese la edad del compañero: "))
        compañero = (nombre, edad)
        
        #agregando la informacion a la lista
        compañeros.append(compañero)
        
 #ordenandolos de menor a mayor segun su edad       
    compañeros.sort(key=lambda x: x[1])
    
 # compañeros [x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre  
 # para definir al asistente y el profesor
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

# Llama a la función y pasa la cantidad de compañeros como argumento
asistente, profesor = obtener_compañeros(3)

print(f'el profesor es: {profesor} y su asistente es: {asistente}')