import pandas as pd
from sqlalchemy import create_engine

print("Librerías importadas de manera correcta")

try:
    # Conexión a OLTP (base de datos origen)
    engine_oltp = create_engine('postgresql+pg8000://postgres:1234@localhost:5432/oltp')


    # Conexión a OLAP (base de datos destino)
    engine_olap = create_engine('postgresql+pg8000://postgres:1234@localhost:5433/olap')

    print("Conexiones creadas de manera exitosa")
    print("OLTP:", engine_oltp)
    # print("OLAP:", engine_olap)

except Exception as e:
    print("Error en la conexión:", e)

# Probar las conexiones leyendo datos desde la base de datos
try:
    #df_test = pd.read_sql_query("SELECT * FROM autor LIMIT 7", engine_oltp)

    print("Conexión OLTP funciona correctamente")
    print("\nDatos de prueba de la tabla autor:")
    print(df_test)
except Exception as e:
    print("Error al conectar con OLTP:", e)

print("Extrayendo datos del OLTP...")

#Leer la tabla autor
df_autor = pd.read_sql_query("SELECT * FROM autor", engine_oltp)
print("Tabla autor: ", df_autor.shape)


#Leer la tabla editorial
df_editorial = pd.read_sql_query("SELECT * FROM editorial", engine_oltp)
print("Tabla editorial:", df_editorial.shape)

#Leer tabla libros
df_libros = pd.read_sql_query("SELECT * FROM libros", engine_oltp)
print("Tabla libros", df_libros.shape)

#Leer tabla de salida
df_salidas_det = pd.read_sql_query("SELECT * FROM salida", engine_oltp)
print("Tabla salidas_det:", df_salidas_det.shape)

print("\nExtraccion completada!")


