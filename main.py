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



# TRANSFORMACION1: Crear dimension de libros (dim_libros)
# Combinar libros + autor + editorial

dim_libros = df_libros.merge(df_autor, on='idautor', how='left')
dim_libros = dim_libros.merge(df_editorial, left_on='ideditorial', right_on='idedit', how='left')

# Seleccionar y renombrar columnas segun estructura OLAP
dim_libros = dim_libros[['idlibro', 'nom_libro', 'idautor', 'nom_autor', 'ideditorial', 'nom_edit']]
dim_libros.rename(columns={'nom_edit':'nom_editorial'}, inplace=True)

print("Dimension libros creada:")
print(dim_libros.head())
print("Registros:", len(dim_libros))



# TRANSFORMACION 2: Crear dimension de salidas (dim_salidas)

dim_salidas = df_salidas_det[['idsalida', 'total_cant']].copy()

print("Dimension salidas creada: ")
print(dim_salidas)
print("Rgistros:", len(dim_salidas))



# TRANSFORMACION 3: Crear dimension de tiempos (dim_tiempos)
# Extraer year, month, day de la fecha

dim_tiempos = df_salidas_det[['fecha_sal']].copy()
dim_tiempos.rename(columns={'fecha_sal':'idtiempo'}, inplace=True)

#Convertir a datetime si no no lo es
dim_tiempos['idtiempo'] = pd.to_datetime(dim_tiempos['idtiempo'])

#Extraer componentes de fecha
dim_tiempos['year_sal'] = dim_tiempos['idtiempo'].dt.year
dim_tiempos['month_sal'] = dim_tiempos['idtiempo'].dt.month
dim_tiempos['day_sal'] = dim_tiempos['idtiempo'].dt.day

print("Dimension tiempos creada:")
print(dim_tiempos)
print("Registros: ", len(dim_tiempos))




