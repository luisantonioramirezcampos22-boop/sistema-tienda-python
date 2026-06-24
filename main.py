import inventario as inv

def menu():
    while True:
        print("\nSistema De Tienda Integral")
        print("1. Registrar producto")
        print("2. Actualizar stock existente")
        print("3. Procesar venta de productos")
        print("4. Cancelar una venta (Revertir stock)")
        print("5. Mostrar catálogo completo")
        print("6. Mostrar productos agotados")
        print("7. Identificar producto más vendido")
        print("8. Ordenar productos")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            try:
                id_p = input("ID: ")
                nom = input("Nombre: ")
                cat = input("Categoría: ")
                pre = float(input("Precio: "))
                stk = int(input("Stock inicial: "))
                if inv.registrar_producto(id_p, nom, cat, pre, stk):
                    print("Producto registrado exitosamente.")
            except ValueError:
                print("Error: Tipo de dato inválido.")
                
        elif opcion == "2":
            id_p = input("ID del producto: ")
            p = inv.buscar_producto(id_p)
            if p:
                try:
                    cant = int(input(f"Stock actual es {p.stock}. Cantidad a añadir: "))
                    if cant > 0:
                        p.stock += cant
                        print("Stock actualizado.")
                    else:
                        print("Cantidad debe ser positiva.")
                except ValueError:
                    print("Entrada inválida.")
            else:
                print("Producto no encontrado.")
                
        elif opcion == "3":
            id_p = input("ID del producto a vender: ")
            try:
                cant = int(input("Cantidad a vender: "))
                if cant > 0:
                    inv.procesar_venta(id_p, cant)
                else:
                    print("Cantidad debe ser mayor a cero.")
            except ValueError:
                print("Entrada inválida.")
                
        elif opcion == "4":
            id_p = input("ID del producto de la venta a cancelar: ")
            try:
                cant = int(input("Cantidad de unidades a revertir: "))
                if cant > 0:
                    inv.cancelar_venta(id_p, cant)
                else:
                    print("Cantidad debe ser mayor a cero.")
            except ValueError:
                print("Entrada inválida.")
                
        elif opcion == "5":
            if not inv.inventario:
                print("El catálogo está vacío.") 
            else:
                for p in inv.inventario.values():
                    p.mostrar_datos()
                
        elif opcion == "6":
            agotados = [p for p in inv.inventario.values() if p.stock == 0]
            if not agotados:
                print("No hay productos agotados con stock en 0.")
            for p in agotados:
                p.mostrar_datos()
                
        elif opcion == "7":
            mv = inv.obtener_mas_vendido()
            if mv:
                print("\nProducto Más Vendido")
                mv.mostrar_datos()
            else:
                print("No hay productos en el sistema.")
                
        elif opcion == "8":
            print("\nCriterios de ordenamiento:")
            print("1. Precio Ascendente")
            print("2. Precio Descendente")
            print("3. Cantidad en Stock")
            print("4. Número de Ventas")
            crit = input("Seleccione criterio: ")
            
            res = []
            if crit == "1": res = inv.ordenar_inventario("precio", reverso=False)
            elif crit == "2": res = inv.ordenar_inventario("precio", reverso=True)
            elif crit == "3": res = inv.ordenar_inventario("stock")
            elif crit == "4": res = inv.ordenar_inventario("ventas_totales", reverso=True)
            else: print("Opción inválida.")
            
            for p in res:
                p.mostrar_datos()
                
        elif opcion == "9":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida de menú.")

if __name__ == "__main__":
    menu()
 
