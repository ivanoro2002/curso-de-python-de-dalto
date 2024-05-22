animales= ["perro","gato","loro","cocodrilo"]
numeros= [10,50,22,40]

# recorriendo la lista de animales
for animal in animales : 
 print(f'ahora la vairable animal es igual : {animal}')

# recorriendo la lista de numeros y multiplicando * 10 
for numero in numeros:
    resultado = numero * 100
    print (resultado)
  
  #iternado dos listas del mismo tamaño al mismo tiempo  
for numero, animal in zip (animales,numeros):
    print(f' recorriendo la lista1 : {numero}')
    print(f' recorriendo la lista2: {animal}')
    
#forma no optima de recorrer una lista con su indice
for num in  range (len(numeros)) :
  print (numeros[num])
  
   
   
  
   # buscando el else
  for numero in numeros:
    print(f"ejecutando el ultimo bucle valor actual:{numero}")
  else: 
    print("el bucle termino")