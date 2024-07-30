#%%
# Importo librerias
# Tratamiento de datos
import pandas as pd
import numpy as np
# Gestion de los warnings
import warnings
warnings.filterwarnings("ignore")
#%%
# Funcion para convertir a csv a DataFrame
def csv_to_dataframe(file):
    return pd.read_csv(file, index_col=0)
#%%
#Funcion para explorar el DataFrame
def dataframe_exploration(df,df_name):
    print("*" * 50,"\n")
    print(f"--- DATAFRAME EXPLORATION: {df_name} ---\n")
    print("*" * 50,"\n") 
    # Estructura del dataframe y tipos de datos
    print(f"El DataFrame tiene {df.shape[0]} filas y {df.shape[1]} columnas.\n")
    print(f"Muestra de filas aleatorias:")
    print(df.sample(5))  
    print(f"\nTipos de datos por columna:")
    print(pd.DataFrame(df.dtypes, columns = ["tipo_dato"]))    
    print(f"\nInformacion del DataFrame:")
    print(df.info())
    print("_" * 50,"\n")
    # Valores duplicados
    duplicated_values = df.duplicated().sum()
    duplicated_percentage = round(duplicated_values / df.shape[0] * 100, 2)
    print(f"Numero de duplicados en el conjunto de datos son: {duplicated_values}, un {duplicated_percentage}%.\n")
    print("_" * 50,"\n")
    # Valores nulos
    print("Valores nulos por columna:")
    null_values = df.isnull().sum()
    null_percentage = null_values / df.shape[0] * 100
    df_nulos = pd.DataFrame(null_percentage, columns = ["%_nulos"])
    print(df_nulos[df_nulos["%_nulos"] > 0])
    print("_" * 50,"\n")    
    # Columnas numericas con nulos
    nulls_col_num = df[df.columns[df.isnull().any()]].select_dtypes(include=np.number).columns
    print(f"Las columnas numéricas que tienen nulos son:\n{nulls_col_num}\n")
    print(f"El porcentaje de nulos que tiene cada columna numerica es:\n{df[nulls_col_num].isnull().sum() / df.shape[0]}\n")
    print("_" * 50, "\n")
    # Columnas categoricas con nulos
    nulls_col_cat = df[df.columns[df.isnull().any()]].select_dtypes(include="O").columns
    print(f"Las columnas categóricas que tienen nulos son:\n{nulls_col_cat}\n")
    print(f"El porcentaje de nulos que tiene cada columna categórica es:\n{df[nulls_col_cat].isnull().sum() / df.shape[0]}\n")
    # Distribucion categorias
    for col in nulls_col_cat:
        print("_" * 20)
        print(f"Distribución de las categorías para la columna categorica {col.upper()}:")
        print(df[col].value_counts() / df.shape[0])
    print("_" * 50, "\n")   
    # Estadisticas basicas para columnas numericas
    col_num = df.select_dtypes(include=["number"])
    if not col_num.empty:
        print("Estadisticas basicas de columnas numericas:")
        df_num_est = pd.DataFrame(col_num.describe().T)
        print(df_num_est)
    else:
        print("\nNo hay columnas numericas en el DataFrame.")
    # Mostrar estadisticas basicas para columnas categoricas
    col_cat = df.select_dtypes(include=["object", "category"])
    if not col_cat.empty:
        print("\nEstadisticas basicas de columnas categoricas:")
        df_cat_est = pd.DataFrame(col_cat.describe().T)
        print(df_cat_est)
    else:
        print("\nNo hay columnas categoricas en el DataFrame.\n")     
    return df   
# %%
# Limpieza y transformacion
def clean_data(df):
    print("_" * 50,"\n")
    # Eliminar duplicados si los hay
    if df.duplicated().any():
        print(f"Hay {df.duplicated().sum()} registros duplicados encontrados y eliminados.")
        df = df.drop_duplicates(keep='first')
    else:
        print("No se encontraron duplicados.")
    # Eliminar columnas con más del 80% de registros nulos
    cols_null_percentage = df.isnull().mean(axis=0)
    cols_to_remove = cols_null_percentage[cols_null_percentage > 0.8].index
    if not cols_to_remove.empty:
        df = df.drop(columns=cols_to_remove)
        print(f"Columnas eliminadas con más del 80% de valores nulos: {list(cols_to_remove)}")
    else:
        print("No se eliminaron columnas por valores nulos.")      
    # Eliminar filas con más del 80% de sus campos nulos
    row_null_percentage = df.isnull().mean(axis=1)
    rows_to_remove = row_null_percentage[row_null_percentage > 0.8].index
    if not rows_to_remove.empty:
        df = df.drop(index=rows_to_remove)
        removed_rows = len(rows_to_remove)
        print(f"Número total de registros eliminados con más del 80% de sus campos nulos: {removed_rows}")
    else:
        print("No se eliminaron registros por valores nulos.")
    # Eliminar columnas con un solo valor unico
    cols_one_value = [col for col in df.columns if df[col].nunique() == 1]
    if cols_one_value:
        df = df.drop(columns=cols_one_value)
        print(f"Columnas eliminadas con solo un valor unico: {cols_one_value}")
    else:
        print("No se encontraron columnas con solo un valor unico.")       
    # Redondear columnas tipo float a dos decimales si no se pueden convertir a enteros
    cols_float = df.select_dtypes(include=[float]).columns
    if cols_float.any():
        print(f"Columnas tipo float redondeadas a dos decimales o convertidas a enteros: {list(cols_float)}")
        for col in cols_float:
            df[col] = df[col].apply(lambda x: round(x, 2) if x % 1 != 0 else int(x))
    else:
        print("No se encontraron columnas tipo float.\n")       
    return df
# %%
# Imputacion con mediana para columnas numericas
def impute_with_median (df,cols):
    print("_" * 50,"\n")
    for col in cols:
        mediana = df[col].median()
        df[col].fillna(mediana, inplace=True)
        df[col] = df[col].round(2)
    # Comprobar los nulos para cada columna específica
    print("Después del reemplazo usando 'fillna' con la mediana quedan los siguientes nulos")
    print(df[cols].isnull().sum())
    return df
#%%
# Imputacion con Undefined para columnas categoricas
def cat_undefined (df,cols):
    print("_" * 50,"\n")
    for col in cols:
        # Reemplazar los nulos por el valor Undefined para cada una de las columnas de la lista
        df[col] = df[col].fillna("Undefined")  
    # Comprobar si quedan nulos en las columnas categóricas. 
    print("Después del reemplazo usando 'fillna' con 'Undefined' quedan los siguientes nulos")
    print(df[cols].isnull().sum())
    return df
#%%
print("_" * 50,"\n")
# Funcion para conversion de mes a numero
def convert_month_to_number(x):
    # Definir el diccionario de conversion dentro de la funcion
    month_dict = {
        'January': 1, 'February': 2, 'March': 3, 'April': 4, 
        'May': 5, 'June': 6, 'July': 7, 'August': 8, 
        'September': 9, 'October': 10, 'November': 11, 'December': 12
    }
    if isinstance(x, int):
        return x
    if x.isdigit():
        return int(x)
    return month_dict.get(x, None)
#%%
# Convertir dato a tipo DateTime
def convert_to_datetime(df, col):
    print("_" * 50,"\n")
    # Intentar convertir la columna al tipo datetime
    df[col] = pd.to_datetime(df[col], errors='coerce')
    # Identificar y mostrar los registros que se convirtieron en nulos
    problematic_rows = df[df[col].isnull()]
    print(f"Se encontraron {len(problematic_rows)} registros problemáticos que se convirtieron en nulos en la columna {col}:")
    print(problematic_rows)
    # Mostrar el tipo de la columna después de la conversión
    print(f"La columna {col} se ha convertido a tipo: {df[col].dtype}")
    return df
#%%
# Crear columna con anio y mes
def create_datetime_column(df, year_col, month_col, new_col):
    print("_" * 50,"\n")
    # Asignar una columna 'day' con el valor 1
    df = df.assign(day=1)
    # Crear una nueva columna de tipo datetime con las columnas de año y mes
    df[new_col] = pd.to_datetime(df[[year_col, month_col, 'day']].rename(columns={
        year_col: 'year', month_col: 'month'
    }))
    # Eliminar la columna 'day'
    df = df.drop(columns=['day'])
    # Verificar el tipo de la nueva columna
    print(f"Se ha creado una nueva columna '{new_col}' con el año '{year_col}' y el mes '{month_col}' de tipo: {df[new_col].dtype}")
    return df

#%%
#Funcion para crear columna ADR por niveles
def categorize_adr_column(df):
    # Calcular la media y la desviación estándar de ADR, ignorando los valores nulos
    adr_mean = df['adr'].mean()
    adr_std = df['adr'].std()

    # Definir umbrales para las categorías
    low_threshold = adr_mean - adr_std
    high_threshold = adr_mean + adr_std

    # Función para categorizar ADR
    def categorize_adr(adr):
        if pd.isna(adr):
            return 'Desconocido'
        elif adr < low_threshold:
            return 'Bajo'
        elif adr > high_threshold:
            return 'Alto'
        else:
            return 'Medio'

    # Crear una nueva columna con los niveles
    df['ADR_Nivel'] = df['adr'].apply(categorize_adr)
    
    return df
# %%
