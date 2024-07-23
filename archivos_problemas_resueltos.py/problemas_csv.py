#cambiar el tipo de dato de una columna
import pandas as pd

#convertir a string los datos de una columna
df=pd.read_csv ("archivos_problemas_resueltos\\datos.csv")
print(df)

#mostar el tipo de dato del primer elemento de la columna edad 
df ['edad'] = df['edad'].astype (str)


print (type(df['edad'][0]))