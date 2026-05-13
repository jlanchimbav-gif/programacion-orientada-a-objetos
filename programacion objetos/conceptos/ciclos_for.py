import time

## ciclos for ##
## for es una estructura de control que se utiliza para iterar sobre una secuencia de elementos.
## la secuencia de elementos puede ser una lista, una tupla, un diccionario, un set, etc.

# ejemplo con clase persona


class Persona:
    def __init__(self, nombre, edad, habilidad="programar"):
        self.nombre = nombre
        self.edad = edad
        self.habilidad = habilidad
        self.habilidad_aprendida = False

    def practicar(self):
        intentos = 0
        # Bucle for: sigue practicando hasta aprender
        for _ in range(10):
            intentos += 1
            print(f"Intento {intentos}: {self.nombre} está practicando...")
            if intentos >= 5:
                self.habilidad_aprendida = True
                print(f"{self.nombre} ha aprendido a {self.habilidad}!")
                break
            time.sleep(1)
        if not self.habilidad_aprendida:
            print(f"{self.nombre} no ha aprendido a {self.habilidad}.")
        return self.habilidad_aprendida


persona = Persona("Juan", 20)
persona.practicar()

# ejemplo con clase automovil


class Automovil:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        # Bucle for: acelera paso a paso hasta alcanzar la velocidad máxima
        for _ in range(incremento):
            self.velocidad_actual += 1
            print(f"{self.marca} {self.modelo} acelerando... Velocidad actual: {self.velocidad_actual} km/h")
            if self.velocidad_actual >= self.velocidad_maxima:
                print(f"{self.marca} {self.modelo} ha alcanzado la velocidad máxima de {self.velocidad_maxima} km/h")
                break
            time.sleep(1)
        if self.velocidad_actual < self.velocidad_maxima:
            print(f"{self.marca} {self.modelo} no ha alcanzado la velocidad máxima de {self.velocidad_maxima} km/h")
        return self.velocidad_actual

    def frenar(self, decremento):
        # Bucle for: frena paso a paso hasta alcanzar la velocidad 0
        for _ in range(decremento):
            if self.velocidad_actual <= 0:
                print(f"{self.marca} {self.modelo} ya está detenido (0 km/h).")
                break
            self.velocidad_actual -= 1
            print(f"{self.marca} {self.modelo} frenando... Velocidad actual: {self.velocidad_actual} km/h")
            if self.velocidad_actual <= 0:
                print(f"{self.marca} {self.modelo} se ha detenido por completo.")
                break
            time.sleep(1)
        if self.velocidad_actual > 0:
            print(f"{self.marca} {self.modelo} no ha llegado a 0 km/h (sigue a {self.velocidad_actual} km/h).")
        return self.velocidad_actual


auto = Automovil("Toyota", "Corolla", 8)
auto.acelerar(12)
auto.frenar(12)


# ejemplo con clase laptop


class Laptop:
    def __init__(self, marca, modelo, capacidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.capacidad_maxima = capacidad_maxima
        self.capacidad_actual = 0

    def cargar(self, incremento):
        # Bucle for: carga paso a paso hasta alcanzar la capacidad máxima
        for _ in range(incremento):
            self.capacidad_actual += 1
            print(f"{self.marca} {self.modelo} cargando... Capacidad actual: {self.capacidad_actual} GB")
            if self.capacidad_actual >= self.capacidad_maxima:
                print(f"{self.marca} {self.modelo} ha alcanzado la capacidad máxima de {self.capacidad_maxima} GB")
                break
            time.sleep(1)
        if self.capacidad_actual < self.capacidad_maxima:
            print(f"{self.marca} {self.modelo} no ha alcanzado la capacidad máxima de {self.capacidad_maxima} GB")
        return self.capacidad_actual

    def descargar(self, decremento):
        # Bucle for: descarga paso a paso hasta alcanzar la capacidad 0
        for _ in range(decremento):
            if self.capacidad_actual <= 0:
                print(f"{self.marca} {self.modelo} ya está a 0 GB.")
                break
            self.capacidad_actual -= 1
            print(f"{self.marca} {self.modelo} descargando... Capacidad actual: {self.capacidad_actual} GB")
            if self.capacidad_actual <= 0:
                print(f"{self.marca} {self.modelo} ha alcanzado la capacidad 0 GB")
                break
            time.sleep(1)
        if self.capacidad_actual > 0:
            print(f"{self.marca} {self.modelo} no ha alcanzado la capacidad 0 GB")
        return self.capacidad_actual


laptop = Laptop("Dell", "XPS 13", 8)
laptop.cargar(12)
laptop.descargar(12)
