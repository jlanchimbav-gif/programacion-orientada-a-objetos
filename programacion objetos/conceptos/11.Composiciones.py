# Composiciones #
## es un mecanismo para combinar objetos de diferentes clases ##

# ejemplo con clase persona##
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"

# ejemplo con clase automovil##
class Automovil:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self):
        self.velocidad_actual += 10
        return f"El automovil {self.marca} {self.modelo} está acelerando a {self.velocidad_actual} km/h."

    def __str__(self):
        return f"Automovil(marca={self.marca}, modelo={self.modelo}, velocidad_maxima={self.velocidad_maxima}, velocidad_actual={self.velocidad_actual})"

# ejemplo con clase laptop##
class Laptop:
    def __init__(self, marca, modelo, memoria):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria
        self.memoria_actual = 0
        self.memoria_actual += 10
        return f"La laptop {self.marca} {self.modelo} está encendida con {self.memoria_actual} GB de memoria."
    def __str__(self):
        return f"Laptop(marca={self.marca}, modelo={self.modelo}, memoria={self.memoria}, memoria_actual={self.memoria_actual})"

# ejemplo con clase composiciones##
def demo():
    persona1 = Persona("Jorge", 30)
    automovil1 = Automovil("Toyota", "Corolla", 180)
    laptop1 = Laptop("Dell", "XPS 13", 512)
    print(persona1.saludar())
    print(automovil1.acelerar())
    print(laptop1.encender())
    print(persona1)
    print(automovil1)