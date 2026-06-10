#Crear una clase llamada Persona
class Persona:
  #Crear el método contructor para inicializar mis atributos
  def __init__(self,nom,apellido,cedula,nota_final):
    #Crear mis atributos
    self.nombre=nom
    self.apellido=apellido
    self.cedula=cedula
    self.nota_final=nota_final
  #Crear un método para presenta la información
  def presenta_informacion(self):
    print(f"Nombre: {self.nombre} Apellido: {self.apellido} Cédula: {self.cedula} Nota Final: {self.nota_final}")

#Ingreso de los datos
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
cedula=input("Ingrese su cédula: ")
nota_final=input("Ingrese su nota final: ")
#Crear el objeto y luego lo instancio a partir de la clase Persona
persona1=Persona(nombre,apellido,cedula,nota_final)
#Llamar al método presenta_información
persona1.presenta_informacion()
#Crear el segundo objeto
persona2 =Persona("Gabriel","Villegas","0986804432","88")
persona2.presenta_informacion()
persona2.nombre="Juan"
persona2.presenta_informacion()
