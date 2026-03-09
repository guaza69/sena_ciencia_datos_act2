import streamlit as st
import pandas as pd

st.title("Bases de Datos en la Nube: MongoDB")

st.markdown("""
### Ejercicio
MongoDB es una base de datos NoSQL muy popular que almacena la información de forma muy similar a JSON.

**Instrucciones:**
1. Imagina que tienes acceso a un clúster de MongoDB Atlas. Para este ejercicio no necesitas conectarte realmente a la base de datos a menos que tengas un clúster de prueba.
2. Basándote en el material de clase, escribe el **código necesario (comentado si no tienes conexión)** para conectarte usando `pymongo` y la clase `MongoClient`.
3. Supón que la base de datos se llama `Veterinaria` y la colección se llama `mascotas`.
4. El código debe incluir cómo extraer los documentos y convertirlos en el DataFrame `df_mongo`.
""")

st.subheader("Tu resultado:")
st.markdown("Si no tienes la conexión real, escribe tu código usando `st.code()` para demostrar cómo lo harías teóricamente.")

# ESTUDIANTE: Escribe tu código a continuación

st.markdown("### Código teórico para conectar a MongoDB Atlas y cargar datos a Pandas")

st.code("""
# Importamos las librerías necesarias
from pymongo import MongoClient
import pandas as pd

# ────────────────────────────────────────────────
# PASO 1: Cadena de conexión (URI) de MongoDB Atlas
# ¡NUNCA subas la contraseña real a GitHub o entregas!
uri = "mongodb+srv://<usuario>:<contraseña>@<nombre-cluster>.abcdef.mongodb.net/?retryWrites=true&w=majority"

# ────────────────────────────────────────────────
# PASO 2: Creamos el cliente y nos conectamos
try:
    client = MongoClient(uri)
    # Forzamos una verificación rápida de conexión (opcional)
    client.admin.command('ping')
    st.success("¡Conexión a MongoDB Atlas exitosa! (simulada)")
except Exception as e:
    st.error(f"Error de conexión: {e}")
    # Aquí el código se detendría en un caso real

# ────────────────────────────────────────────────
# PASO 3: Seleccionamos la base de datos y la colección
db = client["Veterinaria"]           # Nombre de la base de datos
coleccion = db["mascotas"]           # Nombre de la colección

# ────────────────────────────────────────────────
# PASO 4: Extraemos todos los documentos (o con filtro si queremos)
# Ejemplo: todos los documentos
cursor = coleccion.find()

# Convertimos el cursor a lista de diccionarios
lista_mascotas = list(cursor)

# ────────────────────────────────────────────────
# PASO 5: Creamos el DataFrame con Pandas
df_mongo = pd.DataFrame(lista_mascotas)

# Opcional: si hay columna '_id' (ObjectId), la podemos convertir a string
if '_id' in df_mongo.columns:
    df_mongo['_id'] = df_mongo['_id'].astype(str)

# ────────────────────────────────────────────────
# Mostrar resultado (en un caso real)
# st.dataframe(df_mongo.head(10))
# print(df_mongo.head())

""", language="python")

st.info("""
**Notas importantes:**
- Este código es **teórico** y está comentado para no ejecutarse.
- En un proyecto real, **nunca** dejes la contraseña en el código.
- Lo correcto es usar variables de entorno o `st.secrets` en Streamlit.
- Si tuvieras conexión real, descomentarías las líneas de ejecución.
""")