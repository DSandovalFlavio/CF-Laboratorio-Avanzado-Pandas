Ejercicios para practicar la interacción entre SQLite, SQLAlchemy y Pandas, junto con sus soluciones:

**Ejercicio 1:** Crear una base de datos SQLite llamada "ventas.db" y una tabla llamada "productos" con las columnas "id" (INTEGER PRIMARY KEY), "nombre" (TEXT), "precio" (REAL) y "cantidad" (INTEGER).

```python
import sqlite3
from sqlalchemy import create_engine

engine = create_engine('sqlite:///ventas.db')

with engine.connect() as conn:
    conn.execute('''
        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT,
            precio REAL,
            cantidad INTEGER
        )
    ''')
```

**Ejercicio 2:** Insertar algunos productos en la tabla "productos" utilizando SQLAlchemy.

```python
import pandas as pd

data = {'nombre': ['Producto A', 'Producto B', 'Producto C'],
        'precio': [10.5, 25.99, 5.75],
        'cantidad': [50, 30, 100]}
df = pd.DataFrame(data)

df.to_sql('productos', engine, if_exists='append', index=False)
```

**Ejercicio 3:** Leer todos los productos de la tabla "productos" en un DataFrame de Pandas.

```python
df_productos = pd.read_sql_table('productos', engine)
print(df_productos)
```

**Ejercicio 4:** Actualizar el precio del "Producto B" a 29.99 utilizando SQLAlchemy.

```python
with engine.connect() as conn:
    conn.execute("UPDATE productos SET precio = 29.99 WHERE nombre = 'Producto B'")
```

**Ejercicio 5:** Eliminar el "Producto C" de la tabla "productos" utilizando SQLAlchemy.

```python
with engine.connect() as conn:
    conn.execute("DELETE FROM productos WHERE nombre = 'Producto C'")
```

**Ejercicio 6:** Seleccionar los productos cuyo precio sea mayor a 15 utilizando Pandas y SQLAlchemy.

```python
df_productos_caros = pd.read_sql_query("SELECT * FROM productos WHERE precio > 15", engine)
print(df_productos_caros)
```

**Ejercicio 7:** Crear una nueva tabla llamada "ventas" con las columnas "id" (INTEGER PRIMARY KEY), "producto_id" (INTEGER), "fecha" (DATE) y "cantidad_vendida" (INTEGER), y establecer una clave foránea que relacione "producto_id" con la columna "id" de la tabla "productos".

```python
with engine.connect() as conn:
    conn.execute('''
        CREATE TABLE ventas (
            id INTEGER PRIMARY KEY,
            producto_id INTEGER,
            fecha DATE,
            cantidad_vendida INTEGER,
            FOREIGN KEY(producto_id) REFERENCES productos(id)
        )
    ''')
```

**Ejercicio 8:** Insertar algunas ventas en la tabla "ventas" utilizando Pandas y SQLAlchemy.

```python
data_ventas = {'producto_id': [1, 2, 1],
               'fecha': ['2023-07-20', '2023-07-22', '2023-07-25'],
               'cantidad_vendida': [5, 10, 8]}
df_ventas = pd.DataFrame(data_ventas)

df_ventas.to_sql('ventas', engine, if_exists='append', index=False)
```

**Ejercicio 9:** Realizar una consulta JOIN para obtener un DataFrame que muestre el nombre del producto, la fecha de venta y la cantidad vendida, utilizando Pandas y SQLAlchemy.

```python
df_ventas_detalle = pd.read_sql_query('''
    SELECT productos.nombre, ventas.fecha, ventas.cantidad_vendida
    FROM ventas
    JOIN productos ON ventas.producto_id = productos.id
''', engine)
print(df_ventas_detalle)
```

**Ejercicio 10:** Calcular el total de ventas por producto, utilizando Pandas y SQLAlchemy para agrupar y sumar las cantidades vendidas.

```python
df_ventas_totales = pd.read_sql_query('''
    SELECT productos.nombre, SUM(ventas.cantidad_vendida) as total_vendido
    FROM ventas
    JOIN productos ON ventas.producto_id = productos.id
    GROUP BY productos.nombre
''', engine)
print(df_ventas_totales)
```

¡Espero que estos ejercicios te sean de ayuda para dominar la interacción entre SQLite, SQLAlchemy y Pandas!
