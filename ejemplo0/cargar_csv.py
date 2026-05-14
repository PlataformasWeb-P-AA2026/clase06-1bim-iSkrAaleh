import csv
import os
from base_datos import conn

cursor = conn.cursor()

ruta_csv = os.path.join('data', 'info.csv')

try:

    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        lector_csv = csv.DictReader(archivo)
        
        print(f"Leyendo archivo desde: {ruta_csv}...")
        
        for fila in lector_csv:
        
            nombre = fila['nombre']
            apellido = fila['apellido']
            cedula = fila['cedula']
            edad = int(fila['edad'])
            
    
            cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) 
                            VALUES (?, ?, ?, ?);"""
            
            cursor.execute(cadena_sql, (nombre, apellido, cedula, edad))
            print(f"Cargado: {nombre} {apellido}")

    conn.commit()
    print("-" * 30)
    print("¡Proceso completado! Los datos del CSV ahora están en la tabla 'Autor'.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo en {ruta_csv}")
    print("Asegúrate de que la carpeta 'data' existe y contiene el archivo 'datos.csv'.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

cursor.close()