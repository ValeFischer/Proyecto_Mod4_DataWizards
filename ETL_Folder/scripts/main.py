#%%
import support as sup
import numpy as np
#%%
#Importacion DataFrame
df = sup.csv_to_dataframe("../data/input_data/finanzas-hotel-bookings.csv")
#%%
#Exploracion
sup.dataframe_exploration(df, "Finanzas Hotel Bookings")
#%%
#Limpieza y transformacion
df_cleaned = sup.clean_data(df)
#Duplicado para imputacion
df_imputed = df_cleaned.copy()
#%%
#Imputacion numerica
nulls_col_num = df_imputed[df_imputed.columns[df_imputed.isnull().any()]].select_dtypes(include = np.number).columns
df_imputed = sup.impute_with_median(df_imputed, nulls_col_num)
#%%
#Imputacion categorica
cols_undefined = ['country', 'market_segment', 'distribution_channel', 'reserved_room_type', 'customer_type']
df_imputed = sup.cat_undefined(df_imputed,cols_undefined)
# %%
#Conversion de mes a numero
df_imputed['arrival_date_month'] = df_imputed['arrival_date_month'].apply(sup.convert_month_to_number)
#%%
#Conversion de fecha a tipo datetime
df_imputed = sup.convert_to_datetime(df_imputed,'reservation_status_date')
#%%
#Creacion de columna tipo datetime con mes y anio
df_imputed = sup.create_datetime_column(df_imputed, 'arrival_date_year', 'arrival_date_month', 'arrival_date_year_month')
#%%
#Agregar columna ADR_Nivel a partir de columna [adr]
df_imputed = sup.categorize_adr_column(df_imputed)

#%%
#Exportacion CSV
print("_" * 50,"\n")
ruta = "../data/output_data/reservas_limpio_final.csv"
df_imputed.to_csv(ruta,index=False)
print(f"CSV exportado correctamente en {ruta}.")

# %%
