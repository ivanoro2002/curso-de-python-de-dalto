#utilizando el parametro args 
def suma (nombre,*numeros):
 return f"sum{nombre}la suma de tus numeros es {sum(numeros)}"

resultado = suma("lucas",4,5,6,7,8)
print (resultado)