frase = input ("decime una frase maestro y te calculo cuanto tardarias en decirla: ")
palabras_separadas = frase.split (" ")
cantidad_de_palabras = len ( palabras_separadas)
print (f'dijiste{cantidad_de_palabras} y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print (f'dalto lo diria en {cantidad_de_palabras * 100 // 2* 1.3 / 100 } segundos')
if cantidad_de_palabras > 120:
 print ("para flaco no te pedi un testamento")


