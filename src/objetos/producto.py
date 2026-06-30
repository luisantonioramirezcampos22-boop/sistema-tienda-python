class Producto:
    def __init__(self, id_producto, nombre, categoria, precio, stock):
        self.id = id_producto
        self.nombre = nombre
        self.categoria = categoria
        self.precio = float(precio)
        self.stock = int(stock)
        self.ventas_totales = 0

    def mostrar_datos(self):
        print(f"\nID: {self.id} | {self.nombre} | Cat: {self.categoria}")
        print(f"Precio: ${self.precio:.2f} | Stock: {self.stock} | Ventas: {self.ventas_totales}")
        print("-" * 40)
        
