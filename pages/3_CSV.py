import streamlit as st
import pandas as pd

st.title("Carga de datos: Archivos CSV locales y desde URL")

st.markdown("""
### Ejercicio
Aprenderás a cargar información desde archivos de texto plano (CSV).

1. **Desde un archivo local:** Crea manualmente un archivo en la carpeta de tu proyecto llamado `calificaciones.csv` e ingresa al menos 3 filas simulando las notas de algunos estudiantes en un curso. Luego cárgalo en un DataFrame llamado `df_local`. Maneja el error si el archivo no existe usando un bloque `try-except`.
2. **Desde internet:** Carga un DataFrame llamado `df_internet` usando la siguiente URL de prueba (datos genéricos de pingüinos): 
   `https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv`
3. Muestra las primeras diez filas de la información procedente del internet y todo tu CSV local usando `st.dataframe()`.
""")

st.subheader("Tu resultado:")
st.write("**Datos desde archivo local:**")
# ESTUDIANTE: Escribe tu código a continuación para el CSV local

st.write("**Datos desde archivo local:**")

try:
    df_local = pd.read_csv("calificaciones.csv")
    st.dataframe(df_local)
except FileNotFoundError:
    st.warning("Archivo 'calificaciones.csv' no encontrado. Créalo con al menos 3 filas de calificaciones.")
except Exception as e:
    st.error(f"Error: {e}")


# ────────────────────────────────────────────────

st.write("**Datos desde internet (Pingüinos de Palmer):**")

try:
    url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"
    df_internet = pd.read_csv(url)
    st.dataframe(df_internet.head(10))
except Exception as e:
    st.error(f"No se pudo cargar el CSV desde internet: {e}")