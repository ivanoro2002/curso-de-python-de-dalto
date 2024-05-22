#creando diccionarios con dict ()
diccionario = dict (nombre="ivan",apellido= "orosco")

#las listas no pueden ser claves y usamos frozenset para meter conjuntos

diccionario = {frozenset (["danilo","rancio"]) : "jajaja"}

#creando diccionarios con fromkeys
diccionario = dict.fromkeys ("nombre","apellido")

print (diccionario)





