import pandas as pd

# Cargar la base de datos
def load_database():
    return pd.read_csv('sales_churn_train.csv')

# Obtener datos de un cliente por ID
def get_client_data(client_id, database):
    client_data = database[database['ClientID'] == client_id]
    return client_data