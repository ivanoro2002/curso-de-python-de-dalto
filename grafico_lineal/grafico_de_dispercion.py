import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Nombre del archivo CSV
filename = "dispersion.CSV"

# Crear un archivo CSV de ejemplo si no existe o está vacío
if not os.path.exists(filename) or os.stat(filename).st_size == 0:
    df_example = pd.DataFrame({
        'tiempo': [1, 2, 3, 4, 5],
        'dinero': [100, 150, 200, 250, 300]
    })
    df_example.to_csv(filename, index=False)

# Leer el archivo CSV
df = pd.read_csv(filename)

# Crear el gráfico de dispersión
sns.scatterplot(x="tiempo", y="dinero", data=df)

# Mostrar el gráfico
plt.show()
