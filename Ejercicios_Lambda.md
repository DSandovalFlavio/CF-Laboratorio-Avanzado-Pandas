Ejercicios enfocados en el uso de `apply()` y `lambda` en Pandas, junto con sus soluciones:

**Ejercicio 1:** Crear una nueva columna `price_discount` que aplique un descuento del 10% a los precios mayores a 100 en la columna `price`.

```python
df['price_discount'] = df['price'].apply(lambda x: x * 0.9 if x > 100 else x)
```

**Ejercicio 2:** Convertir la columna `address` a minúsculas y eliminar espacios en blanco al inicio y al final.

```python
df['address'] = df['address'].apply(lambda x: x.lower().strip())
```

**Ejercicio 3:** Crear una nueva columna `is_expensive` que indique si las venta es mayor a 500.

```python
df['is_expensive'] = df['Weekly_Sales'].apply(lambda x: x > 500)
```

**Ejercicio 4:** Calcular el cuadrado de los valores en la columna `Weekly_Sales`.

```python
df['Weekly_Sales_squared'] = df['Weekly_Sales'].apply(lambda x: x**2)
```

**Ejercicio 5:** Crear una nueva columna `price_per_unit` que divida el precio entre la cantidad para cada producto.

```python
df['price_per_unit'] = df.apply(lambda row: row['price'] / row['quantity'], axis=1)
```

**Ejercicio 6:** Crear una función que clasifique los productos en "barato", "moderado" o "caro" según su precio, y aplicarla a la columna `price` para crear una nueva columna `price_category`.

```python
def classify_price(price):
    if price < 100:
        return 'barato'
    elif price < 500:
        return 'moderado'
    else:
        return 'caro'

df['price_category'] = df['price'].apply(classify_price)
```

**Ejercicio 7:** Crear una nueva columna `description_length` que calcule la longitud de la descripción de cada producto.

```python
df['description_length'] = df['description'].apply(len)
```