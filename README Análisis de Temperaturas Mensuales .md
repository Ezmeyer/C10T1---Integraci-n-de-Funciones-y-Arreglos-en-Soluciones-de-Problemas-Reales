C10T1 - Integración de Funciones y Arreglos en Soluciones de Problemas Reales
# 📊 Análisis de Temperaturas Mensuales

Proyecto académico que demuestra la **integración de funciones y arreglos multidimensionales** para resolver un problema real: el análisis de temperaturas de varias ciudades a lo largo del año.

---

## 🎯 Objetivo

Desarrollar un programa que permita:

* Almacenar temperaturas mensuales de **5 ciudades durante 12 meses**
* Calcular el **promedio anual** de cada ciudad
* Identificar el **mes más caluroso y el más frío** por ciudad
* Determinar qué ciudad tuvo la **mayor variación de temperatura** en el año

Este proyecto fue desarrollado como parte del tema:

**Funciones y procedimientos – Integración de funciones y arreglos**

---

## 🧠 Conceptos aplicados

* Arreglos bidimensionales (matrices)
* Funciones modulares
* Paso de parámetros y valores de retorno
* Análisis de datos con estructuras iterativas
* Separación de responsabilidades en el código

---

## 🏗️ Estructura del programa

El programa utiliza una matriz para almacenar los datos:

```
temperaturas[ciudad][mes]
```

| Índice   | Representa    |
| -------- | ------------- |
| Filas    | Ciudades      |
| Columnas | Meses del año |

---

## ⚙️ Funciones implementadas

### `ingresar_temperaturas()`

Solicita al usuario las temperaturas de cada ciudad y las guarda en una matriz.

### `promedio_anual_ciudades(temps)`

Calcula el promedio anual de temperatura para cada ciudad.

### `meses_extremos(temps)`

Determina el mes más caluroso y el más frío para cada ciudad.

### `ciudad_mayor_variacion(temps)`

Identifica la ciudad con mayor diferencia entre su temperatura máxima y mínima.

### `mostrar_resultados(...)`

Muestra todos los resultados del análisis en pantalla.

---

## ▶️ Ejecución del programa

### Requisitos

* Python 3.x

### Ejecutar

```bash
python temperaturas.py
```

El programa solicitará ingresar las temperaturas mes por mes para cada ciudad.

---

## 📈 Ejemplo de salida

```
--- PROMEDIOS ANUALES ---
Ciudad 1: 21.5 °C
Ciudad 2: 19.8 °C

--- MESES EXTREMOS ---
Ciudad 1: Más caliente = Mes 8, Más frío = Mes 1

--- MAYOR VARIACION ---
Ciudad con mayor variación: Ciudad 3
Variación: 15.2 °C
```

---

## 🧩 Ventajas del uso de funciones y arreglos

### Mantenibilidad

* El código está dividido en funciones independientes
* Facilita la lectura, depuración y modificación

### Escalabilidad

* Es posible aumentar el número de ciudades sin reescribir el programa

```python
CIUDADES = 100
```

### Reutilización

* Las funciones pueden utilizarse en otros proyectos de análisis de datos

---

## ⚡ Rendimiento y uso de memoria

El algoritmo tiene una complejidad aproximada de:

```
O(ciudades × meses)
```

Esto lo hace eficiente incluso si se incrementa el número de ciudades.

El uso de memoria es bajo, ya que solo se almacenan valores numéricos en una matriz.

---

## 📁 Estructura del repositorio

```
📦 analisis-temperaturas
 ┣ 📜 temperaturas.py
 ┗ 📜 README.md
```

---

## 🧑‍💻 Autor

Proyecto desarrollado con fines educativos para demostrar el uso de funciones y arreglos en la resolución de problemas de programación.

---

## 📜 Licencia

Este proyecto puede utilizarse libremente con fines educativos.
