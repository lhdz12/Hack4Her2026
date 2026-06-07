import streamlit as st
from backend.auth import authenticate_user
from backend.database import load_database, get_client_data
from backend.model import load_model, get_churn_reasons, preprocess_data, predict_churn_for_file, predict_churn
import os

# Configuración de la página
st.set_page_config(page_title="Churn Manager", layout="wide")

# Estilos personalizados
with open("frontend/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Autenticación
st.title("Churn Manager")
username = st.text_input("Usuario")
password = st.text_input("Contraseña", type="password")

if st.button("Iniciar sesión"):
    if authenticate_user(username, password):
        st.success("Inicio de sesión exitoso")
        
        # Cargar base de datos y modelo
        database = load_database()
        model = load_model()

        # Mostrar estadísticas
        st.header("Estadísticas")
        boxes_per_month = database['BoxesPerMonth'].mean()
        churns_last_month = database[database['Churn'] == 1].shape[0]
        st.metric("Promedio de cajas por mes", f"{boxes_per_month:.2f}")
        st.metric("Churns el último mes", churns_last_month)

        # Selección de cliente
        st.header("Predicción de Churn")
        client_id = st.text_input("Ingrese el ID del cliente")
        if st.button("Predecir"):
            client_data = get_client_data(client_id, database)
            if not client_data.empty:
                prediction = predict_churn(model, client_data)
                if prediction < 0.5:
                    st.success("Baja probabilidad de churn")
                elif prediction < 0.75:
                    st.warning("Probabilidad media de churn")
                else:
                    st.error("Alta probabilidad de churn")
                
                # Mostrar razones del churn
                api_key = os.getenv("GEMINI_API_KEY")
                reasons = get_churn_reasons(api_key, client_data)
                st.text(reasons)
            else:
                st.error("Cliente no encontrado")
    else:
        st.error("Usuario o contraseña incorrectos")

# Agregar una sección para cargar y procesar un archivo
st.header("Cargar archivo para predicción")
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

if uploaded_file is not None:
    # Guardar el archivo subido temporalmente
    file_path = "sales_churn_test.csv"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Procesar los datos y predecir
    try:
        processed_data = preprocess_data(file_path)
        predictions = predict_churn_for_file(model, processed_data)

        # Mostrar los resultados en el frontend
        st.success("Predicciones realizadas con éxito")
        processed_data['Churn Probability'] = predictions
        st.dataframe(processed_data)
    except Exception as e:
        st.error(f"Error al procesar el archivo: {e}")