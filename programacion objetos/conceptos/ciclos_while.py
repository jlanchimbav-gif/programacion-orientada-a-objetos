## ciclos o bucles while ##
## Es una estructira de control que permite repetir un bloque de codigo mientras se cumpla una condicion ##
## la condicion se evalua antes de ejecutar el codigo es decir la condicion es verdadera##

## ejemplo con clase persona##

from clases import Persona


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.habilidad_aprendida = False

    def practicar(self):
        intentos = 0
        # Bucle while: sigue practicando hasta aprender
        while not self.habilidad_aprendida:
            intentos += 1
            print(f"{self.nombre} está practicando... intento {intentos}")
            
            if intentos >= 5:  # condición para salir del bucle
                self.habilidad_aprendida = True
                print(f"{self.nombre} ha aprendido la habilidad después de {intentos} intentos.")

# 🚀 Uso de la clase
persona1 = Persona("Jorge", 30)
persona1.practicar()

## ejemplo con clase Automovil ##

from clases import Automovil
class Automovil:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        # Bucle while: acelera paso a paso hasta alcanzar la velocidad máxima
        while self.velocidad_actual < self.velocidad_maxima:
            self.velocidad_actual += incremento
            if self.velocidad_actual > self.velocidad_maxima:
                self.velocidad_actual = self.velocidad_maxima
            print(f"{self.marca} {self.modelo} va a {self.velocidad_actual} km/h")
        print(f"{self.marca} {self.modelo} alcanzó su velocidad máxima de {self.velocidad_maxima} km/h.")

# 🚗 Uso de la clase
auto = Automovil("Toyota", "Corolla", 180)
auto.acelerar(40)

## Ejemplo con clase laptop ##

from clases import Laptop
class Laptop:
    def __init__(self, marca, modelo, capacidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.capacidad_maxima = capacidad_maxima
        self.capacidad_actual = 0

    def cargar(self, incremento):
        if incremento <= 0:
            print("El incremento de carga debe ser mayor que 0.")
            return

        # Bucle while: carga la laptop hasta alcanzar la capacidad máxima
        while self.capacidad_actual < self.capacidad_maxima:
            self.capacidad_actual += incremento
            if self.capacidad_actual > self.capacidad_maxima:
                self.capacidad_actual = self.capacidad_maxima
            print(f"{self.marca} {self.modelo} cargando... {self.capacidad_actual}%")

        print(f"{self.marca} {self.modelo} llegó al {self.capacidad_maxima}% de batería.")

# Uso de la clase
laptop1 = Laptop("HP", "15-f0010ns", 100)
laptop1.cargar(25)