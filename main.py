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
    df_test = pd.read_sql_query("SELECT * FROM autor LIMIT 7", engine_oltp)

    print("Conexión OLTP funciona correctamente")
    print("\nDatos de prueba de la tabla autor:")
    print(df_test)
except Exception as e:
    print("Error al conectar con OLTP:", e)
