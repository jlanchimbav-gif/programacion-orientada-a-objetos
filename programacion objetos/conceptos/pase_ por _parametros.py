## pase por parametros ##
## es una funcion que recibe parametros 
## y los utiliza para realizar una tarea especifica ##

def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Jorge"))

# pase por parametros con valores por defecto 

def saludar(nombre,mensaje="hola"):
    return f"{mensaje}, {nombre}!"

#class Automovil
class Automovil:
    def __init__(self, marca, modelo, año):
        # Atributos que reciben parámetros al crear el objeto
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.encendido = False

    # Método para encender el automóvil
    def encender(self):
        self.encendido = True
        return f"El {self.marca} {self.modelo} está encendido."

    # Método para apagar el automóvil
    def apagar(self):
        self.encendido = False
        return f"El {self.marca} {self.modelo} está apagado."

    # Método para mostrar información
    def info(self):
        estado = "encendido" if self.encendido else "apagado"
        return f"{self.marca} {self.modelo} ({self.año}) - Estado: {estado}"


