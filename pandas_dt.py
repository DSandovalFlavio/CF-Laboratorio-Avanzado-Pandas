# %%
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/DSandovalFlavio/CF-Laboratorio-Avanzado-Pandas/main/data/walmartsales.csv')
# %%
df.info()
# %%
df['fecha'] = pd.to_datetime(df['fecha'], format='%Y-%m-%d') # Formato estándar
df['fecha'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')  
# %%
df['año'] = df['fecha'].dt.year
df['mes_nombre'] = df['fecha'].dt.month_name()