import streamlit as st
import pandas as pd
import requests

st.title("Conexiones Avanzadas: API REST")

st.markdown("""
### Ejercicio
A veces los datos están "vivos" y debes consultarlos a través de una API en internet.

1. Vamos a usar la PokéAPI para obtener algunos datos de Pokémon de forma sencilla. 
2. Realiza una petición `GET` a la siguiente URL: `https://pokeapi.co/api/v2/pokemon?limit=10`
3. Verifica que la petición fue exitosa (`status_code == 200`).
4. Convierte la respuesta a formato JSON.
5. Extrae la lista que viene dentro de la llave `"results"`.
6. Convierte esa lista extraída en un DataFrame llamado `df_pokemon` y muéstralo con Streamlit mediante `st.dataframe()`.
""")

st.subheader("Tu resultado:")
# ESTUDIANTE: Escribe tu código a continuación

url = "https://pokeapi.co/api/v2/pokemon?limit=10"

respuesta = requests.get(url)

if respuesta.status_code == 200:
    # Éxito: convertimos a diccionario Python
    datos_json = respuesta.json()
    
    # La clave "results" contiene la lista de Pokémon
    # Cada elemento es un diccionario con "name" y "url"
    resultados = datos_json.get("results", [])
    
    # Creamos el DataFrame directamente desde la lista
    df_pokemon = pd.DataFrame(resultados)
    
    # Mostramos la tabla
    st.dataframe(df_pokemon)
    
    # Opcional: mostramos cuántos Pokémon se obtuvieron
    st.success(f"Se obtuvieron {len(df_pokemon)} Pokémon de la PokéAPI")
else:
    st.error(f"Error al consultar la API. Código: {respuesta.status_code}")