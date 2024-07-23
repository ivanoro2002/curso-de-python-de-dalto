archivo = open("archivos\\texto_de_dalto.txt",enconding= "UTF-8")

#leer archivo completo
#archivo= archivo_sin_leer.read ()

#leer linea por linea
#lineas= archivo.readlines ()

#leer una sola linea
linea = archivo.readline ()

#cerrar el archivo
archivo.close ()
print(linea)