# 📊 Sistema de Análisis de Datos de Ventas

## 📌 Descripción del Proyecto

Este programa permite analizar las ventas diarias de una empresa con múltiples sucursales durante un mes. Utiliza arreglos multidimensionales y funciones modulares para procesar la información y generar estadísticas útiles para la toma de decisiones.

El sistema simula el comportamiento de ventas de **10 sucursales durante 30 días**, permitiendo calcular totales, identificar la mejor sucursal, detectar patrones y generar un pronóstico de ventas.

---

## 🎯 Objetivos del Programa

El programa fue desarrollado para:

* Almacenar datos de ventas en una estructura bidimensional
* Calcular el total de ventas por sucursal y por día
* Identificar la sucursal con mejor desempeño
* Detectar patrones en las ventas
* Generar un pronóstico simple para el siguiente mes

---

## 🧠 Tecnologías Utilizadas

* Lenguaje: **Python**
* Estructuras de datos: **Arreglos multidimensionales (listas anidadas)**
* Programación modular mediante funciones

---

## 🏗️ Estructura del Programa

El sistema está organizado en funciones independientes, cada una con una tarea específica:

| Función                | Descripción                                  |
| ---------------------- | -------------------------------------------- |
| `generar_ventas()`     | Genera datos de ventas simulados             |
| `total_por_sucursal()` | Calcula el total de ventas por cada sucursal |
| `total_por_dia()`      | Calcula el total de ventas por día           |
| `mejor_sucursal()`     | Identifica la sucursal con mayores ventas    |
| `analizar_patrones()`  | Detecta los días con mayor y menor ventas    |
| `pronostico()`         | Estima las ventas del próximo mes            |

---

## 🧮 Estructura de Datos

Se utiliza una matriz para almacenar las ventas:

```
ventas[sucursal][dia]
```

Ejemplo:

```
ventas[0][0] → Ventas de la sucursal 1 en el día 1
ventas[3][10] → Ventas de la sucursal 4 en el día 11
```

---

## 🚀 Cómo Ejecutar el Programa

1. Asegúrate de tener Python instalado.
2. Guarda el archivo como:

```
analisis_ventas.py
```

3. Ejecuta el programa desde la terminal:

```
python analisis_ventas.py
```

---

## 📈 Funcionalidades Principales

### 1. Registro de ventas

El sistema genera automáticamente ventas diarias aleatorias entre 100 y 1000 para simular datos reales.

### 2. Cálculo de totales

Se calculan:

* Totales por sucursal
* Totales por día

### 3. Identificación de la mejor sucursal

El sistema detecta cuál sucursal obtuvo el mayor volumen de ventas durante el mes.

### 4. Detección de patrones

Se identifican:

* Día con mayores ventas
* Día con menores ventas

### 5. Pronóstico de ventas

Se realiza una estimación del siguiente mes usando el promedio diario de ventas.

---

## 📊 Ejemplo de Salida

```
Total por sucursal: [14500, 15230, 13980, ...]
Total por día: [4200, 3900, 5100, ...]

Mejor sucursal: 2 con ventas: 15230
Día con más ventas: 7
Día con menos ventas: 3

Pronóstico de ventas para el próximo mes: 145320.50
```

---

## 📂 Posibles Mejoras Futuras

* Lectura de datos desde archivos CSV o Excel
* Visualización gráfica de ventas
* Análisis por días de la semana
* Implementación de una interfaz gráfica

---

## 👨‍💻 Autor

Proyecto desarrollado con fines académicos para practicar:

* Arreglos bidimensionales
* Funciones modulares
* Análisis básico de datos en Python

---

## 📜 Licencia

Este proyecto puede ser utilizado libremente con fines educativos.
