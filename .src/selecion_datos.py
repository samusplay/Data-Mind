import pandas as pd
import os

def load_data(file_path):
    """Carga el acrhivo Csv si existe y maneja posibles errpres"""
    # Verificar si el archivo existe
    if os.path.exists(file_path):
        try:
            #intentar leer el archivo CSV
            retail_data=pd.read_csv(file_path)
            print(f"Archivo cargado exitosamente: {file_path}")
            # mostrar 5 primeras filas como muestra de los datos cargados
            print(retail_data.head())
            return retail_data
        except Exception as e:
            # En caso de error al leer el acrhivo,imprimir el error
            print(f"Error al leer el archivo: {e}")
            return None
    else:
        # Si el archivo no existe , mostrar un mensaje de error
        print(f"El archivo no existe en la ruta proporcionada:{file_path}")
        return None
       
file_path='.data/online_retail.csv'

retail_data=load_data(file_path)

if retail_data is not None:
    print("Datos Cargados correctamente")