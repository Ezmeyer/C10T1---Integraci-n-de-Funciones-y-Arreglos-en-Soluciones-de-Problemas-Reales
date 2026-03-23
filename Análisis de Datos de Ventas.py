import random

# -----------------------------
# 1. Generar datos de ventas
# -----------------------------
def generar_ventas(sucursales, dias):
    ventas = []
    for i in range(sucursales):
        fila = []
        for j in range(dias):
            fila.append(random.randint(100, 1000))
        ventas.append(fila)
    return ventas


# -----------------------------
# 2. Total por sucursal
# -----------------------------
def total_por_sucursal(ventas):
    totales = []
    for fila in ventas:
        totales.append(sum(fila))
    return totales


# -----------------------------
# 3. Total por día
# -----------------------------
def total_por_dia(ventas):
    dias = len(ventas[0])
    totales = []
    
    for d in range(dias):
        suma = 0
        for s in range(len(ventas)):
            suma += ventas[s][d]
        totales.append(suma)
        
    return totales


# -----------------------------
# 4. Mejor sucursal
# -----------------------------
def mejor_sucursal(totales):
    mayor = max(totales)
    indice = totales.index(mayor)
    return indice, mayor


# -----------------------------
# 5. Análisis de patrones
# -----------------------------
def analizar_patrones(totales_dia):
    mejor_dia = totales_dia.index(max(totales_dia))
    peor_dia = totales_dia.index(min(totales_dia))
    
    return mejor_dia, peor_dia


# -----------------------------
# 6. Pronóstico simple
# Promedio diario proyectado
# -----------------------------
def pronostico(ventas):
    total = 0
    dias = 0
    
    for fila in ventas:
        total += sum(fila)
        dias += len(fila)
    
    promedio = total / dias
    return promedio * 30


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------
SUCURSALES = 10
DIAS = 30

ventas = generar_ventas(SUCURSALES, DIAS)

totales_sucursal = total_por_sucursal(ventas)
totales_dia = total_por_dia(ventas)

mejor, valor = mejor_sucursal(totales_sucursal)
mejor_dia, peor_dia = analizar_patrones(totales_dia)

pronostico_mes = pronostico(ventas)

# -----------------------------
# RESULTADOS
# -----------------------------
print("Total por sucursal:", totales_sucursal)
print("Total por día:", totales_dia)

print("\nMejor sucursal:", mejor + 1, "con ventas:", valor)

print("Día con más ventas:", mejor_dia + 1)
print("Día con menos ventas:", peor_dia + 1)

print("Pronóstico de ventas para el próximo mes:", round(pronostico_mes, 2))