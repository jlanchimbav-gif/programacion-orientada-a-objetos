## condicionales if y else ##
# clase Automovil
from clases import Automovil
from clases import Laptop


class Automovil:
    def __init__(self, marca, modelo, año, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        # Usamos if y else para controlar la velocidad
        if self.velocidad_actual + incremento <= self.velocidad_maxima:
            self.velocidad_actual += incremento
            return f"El automóvil aceleró a {self.velocidad_actual} km/h."
        else:
            self.velocidad_actual = self.velocidad_maxima
            return f"¡Has alcanzado la velocidad máxima de {self.velocidad_maxima} km/h!"

    def frenar(self, decremento):
        if self.velocidad_actual - decremento >= 0:
            self.velocidad_actual -= decremento
            return f"El automóvil frenó a {self.velocidad_actual} km/h."
        else:
            self.velocidad_actual = 0
            return "El automóvil está detenido."

    def info(self):
        return f"{self.marca} {self.modelo} ({self.año}) - Velocidad actual: {self.velocidad_actual} km/h"

# class Laptop 
class Laptop:
    def __init__(self, marca, modelo, año, memoria_maxima):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.memoria_maxima = memoria_maxima
        self.memoria_actual = 512

    def memoria(self, incremento):
        # Usamos if y else para controlar la capacidad de menoria
        if self.memoria_actual + incremento <= self.memoria_maxima:
            self.memoria_actual += incremento
            return f"La Laptop icrementa su memoria {self.memoria_actual} GB."
        else:
            self.memoria_actual = self.memoria_maxima
            return f"¡Has alcanzado la capacidad máxima de {self.memoria_maxima} GB!"

    def capacidad (self, decremento):
        if self.memoria_actual - decremento >= 0:
            self.memoria_actual -= decremento
            return f"la Laptop tiene capacidad de memoria de  {self.memoria_actual} GB."
        else:
            self.memoria_actual = 512
            return "La Laptop no incremento su memoria."

    def info(self):
        return f"{self.marca} {self.modelo} ({self.año}) - memoria actual: {self.memoria_actual} GB"
