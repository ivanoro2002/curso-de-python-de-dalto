# 2 listas, una con nombres otra con apellidos
nombres=["lucas","camila","ivan","franco","lautaro"]
apellidos=["dalto","orosco","gomez,","sanchez","gimenez"]

#registar esta informacion en un txt en forma optima

with open ("nombres_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son:\n")
    [arch.writelines (f'nombre:{n}\n apellido:{a}\n----------') for n,a in zip(nombres,apellidos)]