#Crear la clase Vehículo
class Vehiculo:
  #Crear el método constructor para inicializar mis atributos (marca,modelo,año)
  def __init__(self,marca,modelo,anio):
    #Creo mis atributos
    self.marca=marca
    self.modelo=modelo
    self.anio=anio
  #Creo un método para mostrar información
  def mostrar_info(self):
    print("Información del vehículo")
    print(f"Marca: {self.marca} Modelo: {self.modelo} Año: {self.anio}")
  #Creo un método para acelerar
  def acelerar(self):
    print("El vehículo está acelerando")

#Crear la clase hija llamada Coche
class Coche(Vehiculo):
  #Creo el método constructor de la clase Coche
  def __init__(self,marca,modelo,anio,numero_puerta):
    #LLamar al método constructor de la clase padre Vehículo
    super().__init__(marca,modelo,anio)
    #Creo el atributo propio de la clase Coche
    self.numero_puerta=numero_puerta
  #Crear el método para presentar información del Coche
  def mostrar_info(self):
    #LLamar al método mostrar_info de la clase padre Vehículo
    super().mostrar_info()
    print(f"Número de puertas: {self.numero_puerta}")
  #Crear el método abrir puertas
  def abrir_puerta(self):
    print(f"El coche {self.marca} {self.modelo} esta abriendo las puertas")

#Crear la clase hija Motocicleta
class Motocicleta(Vehiculo):
  #Creo el método constructor de la clase Motocicleta
  def __init__(self,marca,modelo,anio,tipo_motor):
    #LLamar al método constructor de la clase padre Vehículo
    super().__init__(marca,modelo,anio)
    #Creo el atributo propio de la clase
    self.tipo_motor=tipo_motor
  #Crear el método para presentar información de la Motocicleta
  def mostrar_info(self):
    #LLamar al método mostrar_info de la clase padre Vehículo
    super().mostrar_info()
    print(f"Tipo de motor: {self.tipo_motor}")
  #Crear el metodo hacer caballito
  def hacer_caballito(self):
    print(f"La motocicleta {self.marca} {self.modelo} está haciendo el caballito")

#Solicitar la información al usuario de Coche
marca=input("Ingrese la marca del vehículo: ")
modelo=input("Ingrese el modelo del vehículo: ")
anio=int(input("Ingrese el año del vehículo: "))
numero_puertas=int(input("Ingrese el número de puertas del coche: "))

#Creo el objeto e instancio de la clase coche
coche=Coche(marca,modelo,anio,numero_puertas)
coche.mostrar_info()
coche.acelerar()
coche.abrir_puerta()

#Solicitar la información al usuario de motocicleta
marca=input("Ingrese la marca de la motocicleta: ")
modelo=input("Ingrese el modelo de la motocicleta: ")
anio=int(input("Ingrese el año de la motocicleta: "))
tipo_motor=input("Ingrese el tipo de motor de la motocicleta: ")
#Creo el objeto e instacio de la clase Motocicleta
motocicleta=Motocicleta(marca,modelo,anio,tipo_motor)
motocicleta.mostrar_info()
motocicleta.acelerar()
motocicleta.hacer_caballito()

            


