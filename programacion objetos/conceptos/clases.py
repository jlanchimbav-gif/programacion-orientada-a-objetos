## clase es un molde para crear objetos ##
## ejemplo con varios objetos ##

# clase persona
from pyexpat import model


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre   # atributo de instancia
        self.edad = edad       # atributo de instancia

    def saludar(self):
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años."

# clase automovil
class Automovil:
    def __init__(self, marca, color):
        self.marca = marca  
        self.color = color       

    def acelerar(self):
        return f"El automovil {self.marca} está acelerando."
    
    # clase laptop
class Laptop:
    def __init__(self, marca, color):
        self.marca = marca  
        self.modelo = color      

    def encender(self):
        return f"La laptop {self.marca} {self.modelo} está encendida."