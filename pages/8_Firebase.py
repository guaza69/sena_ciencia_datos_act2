import streamlit as st
import pandas as pd

st.title("Bases de Datos en la Nube: Firebase Firestore")

st.markdown("""
### Ejercicio
Firebase es otra opción excelente adoptada por múltiples startups para almacenar datos en tiempo real.

**Instrucciones:**
1. Asume que se te proporcionó un archivo de credenciales de servicio `llave_secreta.json`.
2. Escribe el **código teórico (usando st.code() o conectándote si tienes tu propia bd)** que emplearías con `firebase_admin` para arrancar la aplicación y obtener el cliente de la base de datos.
3. El objetivo sería conectarse a la colección `vehiculos` de tu Firestore y traer todos los documentos.
4. Indica cómo convertirías la respuesta iterando los documentos para extraer su `to_dict()`.
5. Convierte esa lista a un DataFrame `df_firebase` final.
""")

st.subheader("Tu resultado:")
st.markdown("Escribe en la parte de abajo el código que usarías para lograr el objetivo. Si usas código comentado/teórico, compártelo adentro de `st.code()`.")



# ESTUDIANTE: Escribe tu código a continuación

st.markdown("### Código teórico para conectar a Firebase Firestore y cargar datos a Pandas")

st.code("""
# Importamos las librerías necesarias
# (requiere: pip install firebase-admin)
import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

# ────────────────────────────────────────────────
# PASO 1: Inicializar Firebase con credenciales de servicio
# Nota: NUNCA subas este archivo .json a GitHub o entregas públicas
try:
    # cred = credentials.Certificate("llave_secreta.json")
    # firebase_admin.initialize_app(cred)
    st.info("Firebase inicializado (simulado en este ejercicio teórico)")
except Exception as e:
    st.error(f"Error al inicializar Firebase: {e}")

# ────────────────────────────────────────────────
# PASO 2: Obtenemos el cliente de Firestore
db = firestore.client()

# ────────────────────────────────────────────────
# PASO 3: Accedemos a la colección 'vehiculos'
coleccion_vehiculos = db.collection("vehiculos")

# ────────────────────────────────────────────────
# PASO 4: Traemos todos los documentos (streaming)
# .stream() es más eficiente para grandes colecciones que .get()
documentos = coleccion_vehiculos.stream()

# ────────────────────────────────────────────────
# PASO 5: Convertimos cada documento a diccionario
datos = []
for doc in documentos:
    datos_vehiculo = doc.to_dict()
    # Opcional: agregamos el ID del documento como columna
    datos_vehiculo["id_documento"] = doc.id
    datos.append(datos_vehiculo)

# ────────────────────────────────────────────────
# PASO 6: Creamos el DataFrame final
df_firebase = pd.DataFrame(datos)

# En un caso real mostraríamos:
# st.dataframe(df_firebase)

# Opcional: si hay campos con timestamps de Firestore, convertirlos
# (por ejemplo: df_firebase['fecha_compra'] = pd.to_datetime(df_firebase['fecha_compra'], unit='s'))
""", language="python")

st.info("""
**Notas importantes para este ejercicio teórico:**
- El archivo `llave_secreta.json` debe estar en la carpeta del proyecto (o en una ruta segura).
- En producción real se recomienda usar variables de entorno o `st.secrets`.
- Nunca dejes credenciales reales en el código visible.
- El DataFrame final se llama exactamente **`df_firebase`** como pide el ejercicio.
- Se incluye el manejo del **id del documento** (muy útil en Firestore).
""")
