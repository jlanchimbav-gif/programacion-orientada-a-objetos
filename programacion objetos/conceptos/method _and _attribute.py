## metodo y atributo ##
## metodo es una funcion que pertenece al objeto ##
## atributo es una variable que pertenece al objeto ##
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludar(self):
        return f"Hola, me llamo {self.nombre} {self.apellido} y tengo {self.edad} años."

    def cumplir_anios(self):
        self.edad += 1
        return f"Feliz cumpleaños! Ahora tengo {self.edad} años."

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
# class automovil
class Automovil:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def acelerar(self):
        return f"El automovil {self.marca} está acelerando."

    def __str__(self):
        return f"Automovil(marca={self.marca}, color={self.color})"

# class Laptop
class Laptop:
    def __init__(self, marca, modelo, memoria):
        self.marca = marca
        self.modelo = modelo
        self.memoria = memoria

    def encender(self):
        return f"La laptop {self.marca} {self.modelo} está encendida."

    def __str__(self):
        return f"Laptop(marca={self.marca}, modelo={self.modelo}, memoria={self.memoria})"


def demo():
    persona1 = Persona("Jorge", "Lanchimbe", 26)
    print(persona1.saludar())
    print(persona1.cumplir_anios())
    print(persona1)

    automovil1 = Automovil("Toyota", "Rojo")
    print(automovil1.acelerar())
    print(automovil1)

    laptop1 = Laptop("Dell", "XPS 13", "512GB")
    print(laptop1.encender())
    print(laptop1)


if __name__ == "__main__":
    demo()
