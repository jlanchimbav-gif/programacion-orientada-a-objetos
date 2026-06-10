class Producto:
    IVA = 0.12

    def __init__(self, nombre: str, cantidad: int, precio: float):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0.")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0.")

        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def calcular_total(self):
        return self.cantidad * self.precio

    def calcular_total_con_iva(self):
        return self.calcular_total() * (1 + Producto.IVA)

    def categorizar_producto(self):
        total = self.calcular_total()
        if total > 1000:
            return "Top A", 0.22
        elif 500 <= total <= 1000:
            return "Top B", 0.16
        else:
            return "Top C", 0.06

    def calcular_descuento(self):
        categoria, descuento = self.categorizar_producto()
        return self.calcular_total_con_iva() * (1 - descuento)

    def mostrar_detalle(self):
        categoria, descuento = self.categorizar_producto()
        print(f"Producto: {self.nombre}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Precio unitario: ${self.precio:.2f}")
        print(f"Subtotal: ${self.calcular_total():.2f}")
        print(f"Subtotal con IVA: ${self.calcular_total_con_iva():.2f}")
        print(f"Categoría: {categoria} (Descuento {int(descuento*100)}%)")
        print(f"Precio final con descuento: ${self.calcular_descuento():.2f}")
