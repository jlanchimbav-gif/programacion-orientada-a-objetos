class Pizza:
    PRECIOS = {
        "pequeña": 6.50,
        "mediana": 12.35,
        "grande": 22.50
    }
    PRECIO_INGREDIENTE = 1.50
    IVA = 0.12

    def __init__(self, tamaño: str, cantidad: int, ingredientes_extra: int):
        tamaño = tamaño.lower()
        if tamaño not in Pizza.PRECIOS:
            raise ValueError("Tamaño inválido. Use: pequeña, mediana o grande.")
        if cantidad < 1 or cantidad > 25:
            raise ValueError("La cantidad debe estar entre 1 y 25.")
        if ingredientes_extra < 0 or ingredientes_extra > 5:
            raise ValueError("Los ingredientes extra deben estar entre 0 y 5.")

        self.tamaño = tamaño
        self.cantidad = cantidad
        self.ingredientes_extra = ingredientes_extra
        self.precio_base = Pizza.PRECIOS[tamaño]

    def calcular_precio_ingredientes(self):
        return self.ingredientes_extra * Pizza.PRECIO_INGREDIENTE * self.cantidad

    def calcular_precio_sin_iva(self):
        return (self.precio_base * self.cantidad) + self.calcular_precio_ingredientes()

    def calcular_precio_con_iva(self):
        return self.calcular_precio_sin_iva() * (1 + Pizza.IVA)

    def mostrar_detalle(self):
        print(f"Tamaño: {self.tamaño}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Ingredientes extra: {self.ingredientes_extra}")
        print(f"Precio sin IVA: ${self.calcular_precio_sin_iva():.2f}")
        print(f"Valor ingredientes: ${self.calcular_precio_ingredientes():.2f}")
        print(f"Precio final con IVA: ${self.calcular_precio_con_iva():.2f}")
