# ============================================
# SISTEMA DE INVENTARIO SIMPLE
# ============================================

MAX = 5  # puedes cambiar a 50


# -----------------------------
# Ingresar productos
# -----------------------------
def ingresar_productos():
    productos = []
    for i in range(MAX):
        print("\nProducto", i+1)
        codigo = input("Codigo: ")
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        productos.append([codigo, nombre, precio, stock])
    return productos


# -----------------------------
# Buscar por codigo
# -----------------------------
def buscar_codigo(productos, codigo):
    for p in productos:
        if p[0] == codigo:
            return p
    return None


# -----------------------------
# Realizar venta
# -----------------------------
def vender(productos, codigo, cantidad):
    producto = buscar_codigo(productos, codigo)
    if producto and producto[3] >= cantidad:
        producto[3] -= cantidad
        return True
    return False


# -----------------------------
# Mostrar productos con poco stock
# -----------------------------
def stock_bajo(productos):
    for p in productos:
        if p[3] < 5:
            print(p)


# -----------------------------
# Calcular valor total
# -----------------------------
def valor_total(productos):
    total = 0
    for p in productos:
        total += p[2] * p[3]
    return total


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------
productos = ingresar_productos()

codigo = input("\nBuscar producto por codigo: ")
print(buscar_codigo(productos, codigo))

codigo = input("\nCodigo a vender: ")
cantidad = int(input("Cantidad: "))
vender(productos, codigo, cantidad)

print("\nProductos con stock bajo:")
stock_bajo(productos)

print("\nValor total del inventario:", valor_total(productos))