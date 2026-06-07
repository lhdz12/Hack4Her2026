import pandas as pd
import joblib
import lightgbm as lgb

# Cargar el modelo entrenado
def load_model():
    # Cargar el modelo desde el archivo .pkl
    model = joblib.load("modelo_churn.pkl")
    return model

# Procesar los datos y calcular las características faltantes
def preprocess_data(file_path):
    # Cargar la base de datos
    data = pd.read_csv(file_path)

    # Ejemplo de cálculo de características faltantes
    # Asegúrate de ajustar esto según las características que tu modelo necesita
    if 'TotalCharges' in data.columns and 'MonthlyCharges' in data.columns:
        data['MissingCharges'] = data['TotalCharges'].isnull().astype(int)
        data['TotalCharges'] = data['TotalCharges'].fillna(data['MonthlyCharges'] * data['tenure'])

    # Normalización o transformación adicional si es necesario
    # Por ejemplo, si tu modelo requiere codificación de variables categóricas:
    if 'gender' in data.columns:
        data['gender'] = data['gender'].map({'Male': 0, 'Female': 1})

    # Seleccionar solo las columnas que el modelo necesita
    # Asegúrate de que estas columnas coincidan con las usadas en el entrenamiento
    features = [
        'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
        'PhoneService', 'InternetService', 'MonthlyCharges', 'TotalCharges'
    ]
    data = data[features]

    return data

# Predecir churn para los datos procesados
def predict_churn_for_file(model, processed_data):
    predictions = model.predict(processed_data)
    return predictions