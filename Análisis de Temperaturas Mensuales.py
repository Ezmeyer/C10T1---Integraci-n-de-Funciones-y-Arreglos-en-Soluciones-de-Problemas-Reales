# ============================================
# PROGRAMA: ANALISIS DE TEMPERATURAS MENSUALES
# ============================================

CIUDADES = 5
MESES = 12


# -------------------------------------------------
# FUNCION: ingresar_temperaturas
# Descripción:
# Solicita al usuario las temperaturas de cada
# ciudad para los 12 meses y las almacena en una
# matriz bidimensional.
# Parámetros:
#   ninguno
# Retorna:
#   matriz de temperaturas
# -------------------------------------------------
def ingresar_temperaturas():
    temperaturas = []

    for i in range(CIUDADES):
        ciudad = []
        print(f"\nIngrese temperaturas para la ciudad {i+1}")

        for j in range(MESES):
            temp = float(input(f"Mes {j+1}: "))
            ciudad.append(temp)

        temperaturas.append(ciudad)

    return temperaturas


# -------------------------------------------------
# FUNCION: promedio_anual_ciudades
# Descripción:
# Calcula el promedio anual de temperatura de cada
# ciudad.
# Parámetros:
#   temps -> matriz de temperaturas
# Retorna:
#   lista con promedios por ciudad
# -------------------------------------------------
def promedio_anual_ciudades(temps):
    promedios = []

    for ciudad in temps:
        promedio = sum(ciudad) / MESES
        promedios.append(promedio)

    return promedios


# -------------------------------------------------
# FUNCION: meses_extremos
# Descripción:
# Encuentra el mes más caluroso y el más frío
# para cada ciudad.
# Parámetros:
#   temps -> matriz de temperaturas
# Retorna:
#   lista de tuplas (mes_caliente, mes_frio)
# -------------------------------------------------
def meses_extremos(temps):
    resultados = []

    for ciudad in temps:
        max_temp = max(ciudad)
        min_temp = min(ciudad)

        mes_caliente = ciudad.index(max_temp) + 1
        mes_frio = ciudad.index(min_temp) + 1

        resultados.append((mes_caliente, mes_frio))

    return resultados


# -------------------------------------------------
# FUNCION: ciudad_mayor_variacion
# Descripción:
# Determina qué ciudad tuvo la mayor diferencia
# entre su temperatura máxima y mínima.
# Parámetros:
#   temps -> matriz de temperaturas
# Retorna:
#   índice de la ciudad con mayor variación
# -------------------------------------------------
def ciudad_mayor_variacion(temps):
    mayor_variacion = -1
    ciudad_variacion = -1

    for i in range(len(temps)):
        variacion = max(temps[i]) - min(temps[i])

        if variacion > mayor_variacion:
            mayor_variacion = variacion
            ciudad_variacion = i

    return ciudad_variacion, mayor_variacion


# -------------------------------------------------
# FUNCION: mostrar_resultados
# Descripción:
# Muestra en pantalla todos los análisis realizados.
# Parámetros:
#   promedios, extremos, variacion
# -------------------------------------------------
def mostrar_resultados(promedios, extremos, variacion):
    print("\n--- PROMEDIOS ANUALES ---")
    for i, prom in enumerate(promedios):
        print(f"Ciudad {i+1}: {prom:.2f} °C")

    print("\n--- MESES EXTREMOS ---")
    for i, (caliente, frio) in enumerate(extremos):
        print(f"Ciudad {i+1}: Más caliente = Mes {caliente}, Más frío = Mes {frio}")

    print("\n--- MAYOR VARIACION ---")
    print(f"Ciudad con mayor variación: {variacion[0]+1}")
    print(f"Variación: {variacion[1]:.2f} °C")


# ---------------------------
# PROGRAMA PRINCIPAL
# ---------------------------
temperaturas = ingresar_temperaturas()

promedios = promedio_anual_ciudades(temperaturas)
extremos = meses_extremos(temperaturas)
variacion = ciudad_mayor_variacion(temperaturas)

mostrar_resultados(promedios, extremos, variacion)