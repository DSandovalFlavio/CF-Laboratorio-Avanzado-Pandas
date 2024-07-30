Ejercicios sobre manipulación de columnas de tipo string con Pandas, utilizando el conjunto de datos que proporcionaste, junto con sus soluciones:

**Ejercicio 1:** Convertir la columna `city` a mayúsculas.

```python
df['city'] = df['city'].str.upper()
```

**Ejercicio 2:** Reemplazar todas las instancias de "United States" en la columna `country` con "USA".

```python
df['country'] = df['country'].str.replace('United States', 'USA')
```

**Ejercicio 3:** Verificar si la columna `address` contiene la palabra "Way" (sin importar mayúsculas o minúsculas).

```python
df['contains_way'] = df['address'].str.lower().str.contains('way')
```

**Ejercicio 4:** Extraer el número de la calle de la columna `address` (asumiendo que el número siempre está al inicio).

```python
df['street_number'] = df['address'].str.extract('^(\d+)')
```

**Ejercicio 5:** Calcular la longitud de las cadenas de texto en la columna `address`.

```python
df['address_length'] = df['address'].str.len()
```

**Ejercicio 6:** Crear una nueva columna `full_address` que concatene `city`, `country` y `address`, separadas por comas.

```python
df['full_address'] = df['city'] + ', ' + df['country'] + ', ' + df['address']
```

**Ejercicio 7:** Dividir la columna `address` en dos columnas: `street_name` y `street_type`, utilizando el último espacio en blanco como delimitador.

```python
df[['street_name', 'street_type']] = df['address'].str.rsplit(n=1, expand=True)
```

**Ejercicio 8:** Encontrar todas las ciudades únicas que aparecen en la columna `city`.

```python
unique_cities = df['city'].unique()
print(unique_cities)
```

**Ejercicio 9:** Eliminar todos los espacios en blanco al principio y al final de las cadenas de texto en la columna `address`.

```python
df['address'] = df['address'].str.strip()
```

