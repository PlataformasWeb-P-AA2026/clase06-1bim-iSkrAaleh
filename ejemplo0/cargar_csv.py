import csv
import os
from base_datos import conn

# 1. Preparar el cursor
cursor = conn.cursor()

# 2. Definir la ruta del archivo dentro de la carpeta 'data'
# Usamos os.path.join para que funcione bien en Windows, Mac o Linux
ruta_csv = os.path.join('data', 'info.csv')

try:
    # 3. Abrir el archivo CSV
    with open(ruta_csv, mode='r', encoding='utf-8') as archivo:
        # DictReader lee la primera fila como nombres de columnas
        lector_csv = csv.DictReader(archivo)
        
        print(f"Leyendo archivo desde: {ruta_csv}...")
        
        for fila in lector_csv:
            # Extraer variables del CSV
            nombre = fila['nombre']
            apellido = fila['apellido']
            cedula = fila['cedula']
            edad = int(fila['edad'])
            
            # Crear la sentencia SQL (siguiendo tu formato de los otros archivos)
            # Usamos ? para mayor seguridad contra errores de sintaxis
            cadena_sql = """INSERT INTO Autor (nombre, apellido, cedula, edad) 
                            VALUES (?, ?, ?, ?);"""
            
            # Ejecutar el SQL con los datos de la fila actual
            cursor.execute(cadena_sql, (nombre, apellido, cedula, edad))
            print(f"Cargado: {nombre} {apellido}")

    # 4. Confirmar cambios en la base de datos
    conn.commit()
    print("-" * 30)
    print("¡Proceso completado! Los datos del CSV ahora están en la tabla 'Autor'.")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo en {ruta_csv}")
    print("Asegúrate de que la carpeta 'data' existe y contiene el archivo 'datos.csv'.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

# 5. Cerrar el cursor
cursor.close()