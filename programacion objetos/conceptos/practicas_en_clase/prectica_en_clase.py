# Crear una clase llamada Persona
class Persona:
    # Constructor para inicializar los atributos
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Método para presentar información
    def presentar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")


def demo():
    # Crear un objeto (persona1) e instanciarlo
    persona1 = Persona("Alejandro", 26)
    persona1.presentar()


if __name__ == "__main__":
    demo()

