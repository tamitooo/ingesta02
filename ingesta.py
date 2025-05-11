import mysql.connector
import pandas as pd
import boto3

conexion = mysql.connector.connect(
    host="mysql_c", 
    user="root",
    password="utec",
    database="bd_api_employees"
)

consulta = "SELECT * FROM productos;"
df = pd.read_sql(consulta, conexion)
df.to_csv("data.csv", index=False)

s3 = boto3.client('s3')
bucket = "tfg-output-02"
s3.upload_file("data.csv", bucket, "data.csv")

print("✅ Ingesta completada con éxito.")
