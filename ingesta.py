import mysql.connector
import pandas as pd
import boto3

try:
    conexion = mysql.connector.connect(
        host="18.215.162.117", 
        user="root",
        password="utec",
        database="bd_api_employees"
    )
    print("Conexión a MySQL exitosa.")
except mysql.connector.Error as err:
    print(f"Error de conexión MySQL: {err}")
    exit(1)

try:
    consulta = "SELECT * FROM productos;"
    df = pd.read_sql(consulta, conexion)
    df.to_csv("data.csv", index=False)
    print("Datos guardados en data.csv.")
except Exception as e:
    print(f"Error al ejecutar la consulta o guardar el archivo CSV: {e}")
    exit(1)

try:
    s3 = boto3.client('s3')
    bucket = "tfg-output-02"
    s3.upload_file("data.csv", bucket, "data.csv")
    print("Archivo subido a S3 correctamente.")
except Exception as e:
    print(f"Error al subir el archivo a S3: {e}")
    exit(1)

print("Ingesta completada con éxito.")
