from producto import Producto

inventario = {}

def registrar_producto(id_prod, nombre, categoria, precio, stock):
    # Validar que el ID no exista previamente
    if buscar_producto(id_prod):
        print("Error: El ID ya se encuentra registrado.")
        return False
    nuevo = Producto(id_prod, nombre, categoria, precio, stock)
    inventario.append(nuevo)
    return True

def buscar_producto(id_producto):
    for producto in inventario:
        if producto.id == id_producto:
            return producto
    return None

def procesar_venta(id_producto, cantidad):
    producto = buscar_producto(id_producto)
    if not producto:
        print("Error: Producto no encontrado.")
        return
    
    if producto.stock == 0:
        print("VENTA BLOQUEADA: Producto agotado.")
        return
    if cantidad > producto.stock:
        print("VENTA BLOQUEADA: Stock insuficiente.")
        return

    producto.stock -= cantidad
    producto.ventas_totales += cantidad
    print("Venta realizada correctamente.")

    if producto.stock < 5:
        print("ALERTA: ¡Generar Alerta de Reabastecimiento! Stock menor a 5 unidades.")

def cancelar_venta(id_producto, cantidad):
    producto = buscar_producto(id_producto)
    if not producto:
        print("Error: Producto no encontrado.")
        return
    
    if cantidad > producto.ventas_totales:
        print("Error: No puedes cancelar más unidades de las vendidas históricamente.")
        return

    producto.stock += cantidad
    producto.ventas_totales -= cantidad
    print("Venta cancelada. El stock ha sido restaurado.")

# Algoritmo De Ordenamiento Manual
def ordenar_inventario(criterio, reverso=False):
    n = len(inventario)
    lista_copia = list(inventario) # Copia para no alterar el orden original si no se desea
    
    for i in range(n):
        for j in range(0, n - i - 1):
            # Obtener el valor del atributo dinámicamente según el criterio
            val1 = getattr(lista_copia[j], criterio)
            val2 = getattr(lista_copia[j+1], criterio)
            
            condicion = val1 > val2 if not reverso else val1 < val2
            if condicion:
                lista_copia[j], lista_copia[j+1] = lista_copia[j+1], lista_copia[j]
                
    return lista_copia

def obtener_mas_vendido():
    if not inventario:
        return None
    # Búsqueda manual del mayor para cumplir con algoritmos básicos
    mas_vendido = inventario[0]
    for p in inventario:
        if p.ventas_totales > mas_vendido.ventas_totales:
            mas_vendido = p
    return obtener_mas_vendido