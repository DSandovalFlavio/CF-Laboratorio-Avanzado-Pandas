Ejercicios sobre manipulación de columnas de tipo datetime con Pandas, junto con sus soluciones, utilizando el conjunto de datos que proporcionaste:

**Ejercicio 1:** Extrae el año, mes y día de la columna `Date` y crea nuevas columnas para cada componente.

```python
df['Año'] = df['Date'].dt.year
df['Mes'] = df['Date'].dt.month
df['Día'] = df['Date'].dt.day
```

**Ejercicio 2:** Calcula la cantidad de días transcurridos desde la fecha actual hasta cada fecha en la columna `Date`.

```python
df['Dias_Transcurridos'] = (pd.Timestamp.now() - df['Date']).dt.days
```

**Ejercicio 3:** Encuentra la fecha más reciente y la fecha más antigua en el conjunto de datos.

```python
fecha_mas_reciente = df['Date'].max()
fecha_mas_antigua = df['Date'].min()
print("Fecha más reciente:", fecha_mas_reciente)
print("Fecha más antigua:", fecha_mas_antigua)
```

**Ejercicio 4:** Filtra todas las filas de los meses de Enero y Febrero.

```python
df_filtrado = df[(df['Date'].dt.month == 1) | (df['Date'].dt.month == 2)]
```

**Ejercicio 5:** Filtra todas las filas de los días Viernes.

```python
df_filtrado = df[(df['Date'].dt.dayofweek == 4)]  # 0: Lunes, 1: Martes... 4: Viernes
```

**Ejercicio 6:** Convierte la columna `Date` al formato "año-mes" (por ejemplo, "2010-02").

```python
df['Año-Mes'] = df['Date'].dt.strftime('%Y-%m')
```

**Ejercicio 7:** Calcula la diferencia en días entre la fecha máxima y la fecha mínima.

```python
diferencia_dias = (df['Date'].max() - df['Date'].min()).days
print("Diferencia en días:", diferencia_dias)
```

**Ejercicio 8:** Encuentra el día de la semana (por ejemplo, lunes, martes) para cada fecha en la columna `Date`.

```python
df['Dia_Semana'] = df['Date'].dt.day_name()
```
