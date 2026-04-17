# objeto es la intancia de una clase ##
from clases import Persona
from clases import Automovil
from clases import Laptop



persona1 = Persona("Jorge", 30)
persona2 = Persona("Ana", 25)

print(persona1.saludar())  # Hola, me llamo Jorge y tengo 30 años.
print(persona2.saludar())  # Hola, me llamo Ana y tengo 25 años.

Automovil1 = Automovil("Toyota", "Rojo")
print(Automovil1.acelerar())  # El automovil Toyota está acelerando.

Laptop1 =Laptop("dell", "xps 13")
