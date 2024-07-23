import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df= pd.read_csv("pedos.CSV")

sns.lineplot(x="Fecha",y="Número de Pedos",data=df)

plt.plot("2024-07-07",8,"o")

plt.show()
