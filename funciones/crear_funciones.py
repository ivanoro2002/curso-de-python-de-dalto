# creando uhn a funcion simple 
#def saludar():
  #  print ("hola lucas, mi maestro ¿como andas? ")
    
#saludar ()

#crear una funcion que tenga parametro

def saludar (nombre,sexo):
    sexo= sexo.lower ()
    adjetivo= ""
    if(sexo == "hombre"):
      adjetivo = "titan"
  
    elif (sexo ==  "mujer" ):
     adjetivo = "reina"

    print(f'hola {nombre},mi {adjetivo} ¿como andas?')
saludar ("hombre","lucas")
saludar ("camila","mujer")

# creeando una funcion que nos retonre valores

def crear_contraseña_ramdom (num):
    chars = "buenas noches"
    num_entero = str (num)
    num = int (num_entero [0])
    c1= num - 2
    c2= num 
    c3= num - 5
    contraseña = f"{chars[c1]}{chars [c2]}{chars [c3]}{num*2}"
    print (contraseña)
    return contraseña,num
#desempleando la funcion 

password,primer_numero = crear_contraseña_ramdom (398)  

#mostrando los resultados obtenidos y los datos utilixados para obtenerlo
print(f' tu contraseña nueva es : {password}')
print(f' el numero utilizado para crearla fue :{primer_numero}')