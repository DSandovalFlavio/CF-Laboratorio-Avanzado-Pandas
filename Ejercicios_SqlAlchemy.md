Ejercicios para practicar la interacción entre SQLite, SQLAlchemy y Pandas, junto con sus soluciones:


**Ejercicio 1:** Insertar algunos productos en la tabla "productos" utilizando SQLAlchemy.

```python
import pandas as pd

data = {'nombre': ['Producto A', 'Producto B', 'Producto C'],
        'precio': [10.5, 25.99, 5.75],
        'cantidad': [50, 30, 100]}
df = pd.DataFrame(data)

df.to_sql('productos', engine, if_exists='append', index=False)
```

**Ejercicio 2:** Leer todos los productos de la tabla "productos" en un DataFrame de Pandas.

```python
df_productos = pd.read_sql_table('productos', engine)
print(df_productos)
```

**Ejercicio 3:** Seleccionar los productos cuyo precio sea mayor a 15 utilizando Pandas y SQLAlchemy.

```python
df_productos_caros = pd.read_sql_query("SELECT * FROM productos WHERE precio > 15", engine)
print(df_productos_caros)
```

**Ejercicio 4:** Insertar algunas ventas en la tabla "ventas" utilizando Pandas y SQLAlchemy.

```python
data_ventas = {'producto_id': [1, 2, 1],
               'fecha': ['2023-07-20', '2023-07-22', '2023-07-25'],
               'cantidad_vendida': [5, 10, 8]}
df_ventas = pd.DataFrame(data_ventas)

df_ventas.to_sql('ventas', engine, if_exists='append', index=False)
```

**Ejercicio 5:** Realizar una consulta JOIN para obtener un DataFrame que muestre el nombre del producto, la fecha de venta y la cantidad vendida, utilizando Pandas y SQLAlchemy.

```python
df_ventas_detalle = pd.read_sql_query('''
    SELECT productos.nombre, ventas.fecha, ventas.cantidad_vendida
    FROM ventas
    JOIN productos ON ventas.producto_id = productos.id
''', engine)
print(df_ventas_detalle)
```

**Ejercicio 6:** Calcular el total de ventas por producto, utilizando Pandas y SQLAlchemy para agrupar y sumar las cantidades vendidas.

```python
df_ventas_totales = pd.read_sql_query('''
    SELECT productos.nombre, SUM(ventas.cantidad_vendida) as total_vendido
    FROM ventas
    JOIN productos ON ventas.producto_id = productos.id
    GROUP BY productos.nombre
''', engine)
print(df_ventas_totales)
```
