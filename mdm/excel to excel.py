import pandas as pd

# Cargar los archivos de Excel
excel1 = pd.read_excel('C:\Desarrollo\Scripts-varios\datos_extraidos.xlsx')
excel2 = pd.read_excel('C:\Desarrollo\Scripts-varios\MS Security Baseline Windows 11 v24H2.xlsx', sheet_name=None)

# Obtener la información de la columna 1 de Excel 1
nombres_a_buscar = excel1.iloc[:, 0]

# Crear un dataframe vacío para almacenar los resultados
resultados = pd.DataFrame()

# Recorrer los nombres a buscar y obtener la información correspondiente en todas las pestañas de Excel 2
for nombre in nombres_a_buscar:
    print(f"Buscando {nombre}...")
    for sheet_name, sheet_data in excel2.items():
        print(f"  Pestaña: {sheet_name}")
        fila = sheet_data[sheet_data.iloc[:, 0] == nombre]
        if not fila.empty:
            print(f"  Encontrada coincidencia en {sheet_name}!")
            resultados = pd.concat([resultados, fila])
    print(f"Resultados: {resultados.shape[0]} filas")

# Guardar los resultados en un nuevo archivo de Excel
resultados.to_excel('output.xlsx', index=False)