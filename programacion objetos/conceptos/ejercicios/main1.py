from pizza import Pizza

def main():
    # Ejemplo de pedidos
    pedido1 = Pizza("mediana", 2, 3)
    pedido1.mostrar_detalle()

    print("--------------------")

    pedido2 = Pizza("grande", 1, 5)
    pedido2.mostrar_detalle()

if __name__ == "__main__":
    main()
