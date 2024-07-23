import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer el archivo CSV
df = pd.read_csv("confla_ingresos.CSV")

# Función para asignar colores
def assign_colors(df):
    colors = ['red', 'blue', 'green', 'purple', 'orange']
    unique_fuentes = df['fuente'].unique()
    color_dict = {fuente: colors[i % len(colors)] for i, fuente in enumerate(unique_fuentes)}
    return df['fuente'].map(color_dict)

# Asignar colores a cada barra
bar_colors = assign_colors(df)

# Crear el gráfico de barras con colores personalizados
plt.figure(figsize=(10, 6))
bars = plt.bar(x=df['fuente'], height=df['ingresos'], color=bar_colors)

# Obtener el total de ingresos
total_ingresos = df['ingresos'].sum()

# Mostrar el total de ingresos
print(f'El total de ingresos es de: ${total_ingresos} USD')

# Mostrar el gráfico
plt.show()
