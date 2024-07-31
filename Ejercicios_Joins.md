Ejercicios para practicar `merge`, `pivot_table` y `melt` en Pandas, junto con sus soluciones:

**Ejercicio 1:** Une los DataFrames `df_clientes` y `df_pedidos` por la columna `id_cliente`, utilizando un `left join` para mantener todos los clientes, incluso si no tienen pedidos.

```python
df_combinado = pd.merge(df_clientes, df_pedidos, on='id_cliente', how='left')
```

**Ejercicio 2:** Une los DataFrames `df_productos` y `df_ventas` por las columnas `id_producto` y `product_id` respectivamente, utilizando un `inner join` para mostrar solo los productos que se han vendido.

```python
df_combinado = pd.merge(df_productos, df_ventas, left_on='id_producto', right_on='product_id', how='inner')
```

**Ejercicio 3:** Crea una tabla dinámica (pivot table) que muestre la suma de `ventas` por `mes` y `categoria_producto` a partir del DataFrame `df_ventas`.

```python
pivot_table = df_ventas.pivot_table(index='mes', columns='categoria_producto', values='ventas', aggfunc='sum')
```

**Ejercicio 4:** Crea una tabla dinámica que muestre el promedio de `calificacion` por `producto` y `pais` a partir del DataFrame `df_reviews`.

```python
pivot_table = df_reviews.pivot_table(index='producto', columns='pais', values='calificacion', aggfunc='mean')
```

**Ejercicio 5:** Transforma el DataFrame `df_ventas_anchas`, que tiene una columna por cada mes y los valores de ventas en las filas, a un formato largo (long format) utilizando `melt`.

```python
df_ventas_largo = df_ventas_anchas.melt(id_vars='id_producto', var_name='mes', value_name='ventas')
```

**Ejercicio 6:** Transforma el DataFrame `df_temperaturas`, que tiene una columna para cada ciudad y los valores de temperatura en las filas, a un formato largo utilizando `melt`.

```python
df_temperaturas_largo = df_temperaturas.melt(id_vars='fecha', var_name='ciudad', value_name='temperatura')
```

**Ejercicio 7:** Une los DataFrames `df_empleados` y `df_salarios` por la columna `id_empleado`, y luego crea una tabla dinámica que muestre el salario promedio por `departamento` y `año`.

```python
df_combinado = pd.merge(df_empleados, df_salarios, on='id_empleado')
pivot_table = df_combinado.pivot_table(index='departamento', columns='año', values='salario', aggfunc='mean')
```