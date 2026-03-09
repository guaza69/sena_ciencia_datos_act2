import streamlit as st
import pandas as pd

st.title("Carga de datos: Archivos JSON")

st.markdown("""
### Ejercicio
JSON es el formato preferido en el desarrollo web para intercambiar información. 

1. Crea manualmente en la carpeta de tu proyecto un pequeño archivo llamado `catalogo_juegos.json`. 
   El archivo debe contener una lista (arreglo) de diccionarios, donde cada diccionario represente un videojuego con claves como `"Titulo"`, `"Año"`, y `"Consola"`. Añade al menos 3 videojuegos a la lista.
2. Lee este archivo utilizando Pandas y almacénalo en un DataFrame llamado `df_json`.
3. Muestra el DataFrame en la aplicación usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

import json

try:
    # Opción 1: La más simple y directa (recomendada para este ejercicio)
    df_json = pd.read_json("catalogo_juegos.json")
    
    # Mostramos el DataFrame
    st.dataframe(df_json)
    
except FileNotFoundError:
    st.error("No se encontró el archivo 'catalogo_juegos.json'. Créalo en la misma carpeta del proyecto con al menos 3 videojuegos.")
except ValueError:
    st.error("El archivo JSON tiene un formato incorrecto. Verifica que sea una lista de objetos (diccionarios).")
except Exception as e:
    st.error(f"Error al leer el archivo JSON: {e}")

# Opcional: mostrar también la forma alternativa con json.load (muy útil para entender)
st.markdown("**Forma alternativa usando json.load (solo referencia):**")
st.code("""
with open("catalogo_juegos.json", "r", encoding="utf-8") as f:
    data = json.load(f)
df_json = pd.DataFrame(data)
""", language="python")