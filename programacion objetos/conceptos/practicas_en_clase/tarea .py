class Estudiante:
  #Método constructor para inicializar los atributo
  def __init__(self, cedula,nombre,apellido,asignatura):
  #Crear los atributos de la clase
    self.cedula=cedula
    self.nombre=nombre
    self.apellido=apellido
    self.asignatura=asignatura
    self.nota=[]
  #Método Analizador para ingresar notas
  def ingresar_notas(self):
    #Validar la cantidad de notas
    while True:
      try:
        cantidad=int(input("Ingrese la cantidad de notas (mayor a 3): "))
        #Verificar que la cantidad de notas sea mayor a 3
        if cantidad>3:
          #break permite salir del ciclo repetitivo
          break
        else:
          print("La cantidad de notas debe ser mayor a 3")
      except ValueError:
        print("Error: Valor inválido")
    #Bucle para solicitar las notas del alumno
    for i in range(cantidad):
      while True:
        try:
          nota=float(input("Ingrese la nota del estudiante (del 0 al 100)"))
          #Verificar si la nota ingresada está en un rango de 0 a 100
          if nota>=0 and nota<=100:
            #Se almacena en la lista nota
            self.nota.append(nota)
            break
          else:
            print("La nota debe estar en el rango de 0 a 100")
        except ValueError:
          print("Error: Valor inválido")
  #Crear un método para calcular el promedio de las notas
  def calcular_promedio(self):
    if not self.nota:
      return 0
    return sum(self.nota)/len(self.nota)
  #Crear un método para conocer el estado del estudiante
  def estado_estudiante(self):
    #Se guarda el valor del promedio
    promedio=self.calcular_promedio()
    #Determinar el estado del estudiante
    if promedio>=69.5:
      return "Aprobado"
    elif promedio>=39.5:
      return "Suspenso"
    else:
      return "Reprobado"
  #Método para mostrar la información del estudiante
  def mostrar_informacion(self):
    promedio=self.calcular_promedio()
    estado=self.estado_estudiante()
    print("***Información estudiante ****")
    print(f"Estudiante: {self.nombre} {self.apellido}")
    print(f"Cedula: {self.cedula}")
    print(f"Asignatura: {self.asignatura}")
    print(f"Promedio: {promedio}")
    print(f"Estado: {estado}")

def menu():
  #Creo una lista para almacenar los objetos
  estudiantes=[]
  while True:
    print("\n***Menú Principal***")
    #Mostrar la información del Menú
    print("1. Registrar estudiante")
    print("2. Consultar promedio y estado del estudiante")
    print("3. Salir")
    try:
      opcion=int(input("Ingrese la opción deseada: "))
    except ValueError:
      print("Error: Valor inválido")
      continue
    if opcion==1:
      #Solicitamos la información del estudiante
      cedula=input("Ingrese la cédula del estudiante: ")
      nombre=input("Ingrese el nombre del estudiante: ")
      apellido=input("Ingrese el apellido del estudiante: ")
      asignatura=input("Ingrese la asignatura del estudiante: ")
      #Crear un objeto de la clase estudiante
      objeto_estudiante=Estudiante(cedula,nombre,apellido,asignatura)
      objeto_estudiante.ingresar_notas()
      #Creando una lista de objetos
      estudiantes.append(objeto_estudiante)
    elif opcion==2:
      if not estudiantes:
        print("No hay estudiantes registrados")
      else:
        #Mostrar la información de los estudiantes
        #Bucle para presentar todos los estudiantes
        for objeto_estudiante in estudiantes:
          objeto_estudiante.mostrar_informacion()
    elif opcion==3:
      print("Gracias por usar el programa")
      break
    else:
      print("Opción inválida")


menu()