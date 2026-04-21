## swicth ##
## en lenguage python equivale a case/match ##
## es una instruccion  o orden que se le da a un objeto ##
## reemplaza al metodo if/else ##

# class auto 
class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.estado = "apagado"

    def accion(self, comando):
        # Usamos match-case como un switch
        match comando:
            case "encender":
                self.estado = "encendido"
                return f"El {self.marca} {self.modelo} está encendido."
            case "apagar":
                self.estado = "apagado"
                return f"El {self.marca} {self.modelo} está apagado."
            case "tocar_claxon":
                return f"{self.marca} {self.modelo} hace ¡piiiip!"
            case _:
                return "Comando no reconocido."

    def info(self):
        return f"{self.marca} {self.modelo} - Estado: {self.estado}"

# para aceleracion y freno 
class Auto:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.estado = "apagado"

    def accion(self, comando, valor=0):
        # match-case funciona como un switch
        match comando:
            case "encender":
                self.estado = "encendido"
                return f"El {self.marca} {self.modelo} está encendido."
            case "apagar":
                self.estado = "apagado"
                self.velocidad_actual = 0
                return f"El {self.marca} {self.modelo} está apagado."
            case "acelerar":
                if self.estado == "encendido":
                    self.velocidad_actual += valor
                    if self.velocidad_actual > self.velocidad_maxima:
                        self.velocidad_actual = self.velocidad_maxima
                        return f"¡Has alcanzado la velocidad máxima de {self.velocidad_maxima} km/h!"
                    else:
                        return f"El automóvil aceleró a {self.velocidad_actual} km/h."
                else:
                    return "No puedes acelerar un auto apagado."
            case "frenar":
                if self.estado == "encendido":
                    self.velocidad_actual -= valor
                    if self.velocidad_actual < 0:
                        self.velocidad_actual = 0
                    return f"El automóvil frenó a {self.velocidad_actual} km/h."
                else:
                    return "No puedes frenar un auto apagado."
            case _:
                return "Comando no reconocido."

    def info(self):
        return f"{self.marca} {self.modelo} - Estado: {self.estado}, Velocidad: {self.velocidad_actual} km/h"
