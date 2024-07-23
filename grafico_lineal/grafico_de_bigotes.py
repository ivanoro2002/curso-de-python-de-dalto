import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df= pd.read_csv("bigotes.CSV")


# Crear el gráfico de dispersión
sns.boxplot(x="categoria", y="valor", data=df)


#Mostrar el gráfico
plt.show()
