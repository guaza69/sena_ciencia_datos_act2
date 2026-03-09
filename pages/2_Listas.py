import streamlit as st
import pandas as pd

st.title("Método 2: Desde una Lista de Listas")

st.markdown("""
### Ejercicio
En este ejercicio debes crear un DataFrame partiendo de una **lista de listas** que represente el inventario de una tienda de tecnología.

1. Crea una lista de listas donde cada sub-lista contenga información de un producto: 
   `[Nombre del producto, Categoría, Precio, Cantidad en stock]`
   Agrega al menos 4 productos diferentes.
2. Crea un DataFrame llamado `df_inventario` a partir de esta lista y pásale el parámetro `columns=[]` definiendo cómo se llamarán tus columnas.
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

# 1. Lista de listas con al menos 4 productos tecnológicos
productos = [
    ["iPhone 16",              "Smartphone",     5200000,  18],
    ["Samsung Galaxy S24",     "Smartphone",     4200000,   7],
    ["MacBook Air M3 13\"",    "Portátil",       5800000,  12],
    ["AirPods Pro 2",          "Accesorios",     1050000,  35],
    ["Monitor LG 27\" 4K",     "Periféricos",    1450000,  14]
]

# 2. Creamos el DataFrame con nombre exacto df_inventario y columnas definidas
df_inventario = pd.DataFrame(
    productos,
    columns=["Nombre del producto", "Categoría", "Precio", "Cantidad en stock"]
)

# 3. Mostramos el DataFrame (el ejercicio pide st.dataframe())
st.dataframe(df_inventario)