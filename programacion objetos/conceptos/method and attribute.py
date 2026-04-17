## metodo y atributo ##
## metodo es una funcion que pertenece al objeto ##
## atributo es una variable que pertenece al objeto ##
from clases import Persona
from clases import Automovil
from clases import Laptop


class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre= nombre
        self.apellido= apellido
        self.edad= edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} {self.apellido} y tengo {self.edad} años."

    def cumplir_anios(self):
        self.edad += 1
        return f"Feliz cumpleaños! Ahora tengo {self.edad} años."

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
    persona1=Persona("Jorge", "lanchimbe", 26)
    print(persona1.saludar())
    print(persona1.cumplir_anios())
    print(persona1)
    
# class automovil
class Automovil:
    def __init__(self,marca,color):
        self.marca= marca
        self.color= color

    def acelerar(self):
        return f"El automovil {self.marca} está acelerando."

    def __str__(self):
        return f"Automovil(marca={self.marca}, color={self.color})"
    
    Automovil1=Automovil("Toyota", "Rojo")
    print(Automovil1.acelerar())
    print(Automovil1)

# class Laptop
class Laptop:
    def __init__(self,marca,modelo,memoria):
        self.marca=marca
        self.modelo=modelo
        self.memoria=memoria

    def encender(self):
        return f"La laptop {self.marca} {self.modelo} está encendida."

    def __str__(self):
        return f"Laptop(marca={self.marca}, modelo={self.modelo}, memoria={self.memoria})"
    
    Laptop1=Laptop("Dell", "XPS 13" , "512GB")
    print(Laptop1.encender())
    print(Laptop1)
