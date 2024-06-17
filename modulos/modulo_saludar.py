#importamos un modulo y asignandole un nombre
#import modulo_saludar

#desde ese modulo importamos dos funciones
from modulo_saludar import saludar,saludar_raro

#creamos las variables con los saludos
saludo=saludar ("ivan")
saludo_raro=saludar_raro("ivo")

#mostramos los resultados
print (saludo)
print(saludar_raro)