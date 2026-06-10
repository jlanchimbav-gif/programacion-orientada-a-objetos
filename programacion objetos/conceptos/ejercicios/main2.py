from Producto import Producto

def main():
    # Ejemplo de productos
    prod1 = Producto("Laptop", 2, 600)
    prod1.mostrar_detalle()

    print("--------------------")

    prod2 = Producto("Mouse", 10, 25)
    prod2.mostrar_detalle()

    print("--------------------")

    prod3 = Producto("Monitor", 1, 1200)
    prod3.mostrar_detalle()

if __name__ == "__main__":
    main()
