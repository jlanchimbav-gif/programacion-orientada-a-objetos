## Es un mecanismo para compartir atributos y métodos entre clases. ##
## Las subclases heredan los atributos y métodos de las superclases. ##

#class auto
# Clase base
class Auto:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        self.velocidad_actual += incremento
        if self.velocidad_actual > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
        return f"{self.marca} {self.modelo} aceleró a {self.velocidad_actual} km/h."

    def frenar(self, decremento):
        self.velocidad_actual -= decremento
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0
        return f"{self.marca} {self.modelo} frenó a {self.velocidad_actual} km/h."

    def info(self):
        return f"{self.marca} {self.modelo} - Velocidad máxima: {self.velocidad_maxima} km/h"


# Clase derivada (hereda de Auto)
class Moto(Auto):
    def __init__(self, marca, modelo, velocidad_maxima, tipo):
        # Reutilizamos el constructor de Auto
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo = tipo  # atributo adicional

    # Sobrescribimos el método info para añadir más detalles
    def info(self):
        return f"{self.marca} {self.modelo} ({self.tipo}) - Velocidad máxima: {self.velocidad_maxima} km/h"
