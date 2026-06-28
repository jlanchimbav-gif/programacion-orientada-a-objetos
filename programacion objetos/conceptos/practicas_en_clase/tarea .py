class Estudiante:
  #Método constructor para inicializar los atributo
  def __init__(self, cedula,nombre,apellido,asignatura):
  #Crear los atributos de la clase
    self.cedula=cedula
    self.nombre=nombre
    self.apellido=apellido
    self.asignatura=asignatura
    self.nota=[]
# métodos para validar cada atributo al ingresarlo
  @staticmethod
  def validar_cedula(cedula):
    if not cedula.isdigit() or len(cedula) != 10:
      print("Error: La cédula debe tener 10 dígitos numéricos")
      return False
    return True

  @staticmethod
  def validar_nombre(nombre):
    if not nombre.strip():
      print("Error: El nombre no puede estar vacío")
      return False
    if not all(c.isalpha() or c.isspace() for c in nombre):
      print("Error: El nombre solo puede contener letras")
      return False
    if len(nombre.strip()) <= 1:
      print("Error: El nombre no puede ser una sola letra")
      return False
    return True

  @staticmethod
  def validar_apellido(apellido):
    if not apellido.strip():
      print("Error: El apellido no puede estar vacío")
      return False
    if not all(c.isalpha() or c.isspace() for c in apellido):
      print("Error: El apellido solo puede contener letras")
      return False
    return True

  @staticmethod
  def validar_asignatura(asignatura):
    if not asignatura.strip():
      print("Error: La asignatura no puede estar vacía")
      return False
    return True
#metodo para vadilar notas 
  @staticmethod
  def validar_cantidad_notas(cantidad):
    if cantidad <= 3:
      print("La cantidad de notas debe ser mayor a 3")
      return False
    return True

  @staticmethod
  def validar_nota(nota):
    if nota < 0 or nota > 100:
      print("La nota debe estar en el rango de 0 a 100")
      return False
    return True

  @staticmethod
  def recopilar_notas():
    notas_temp = []
    while True:
      try:
        cantidad=int(input("Ingrese la cantidad de notas (mayor a 3): "))
        if Estudiante.validar_cantidad_notas(cantidad):
          break
      except ValueError:
        print("Error: Valor inválido")
    for i in range(cantidad):
      while True:
        try:
          nota=float(input("Ingrese la nota del estudiante (del 0 al 100): "))
          if Estudiante.validar_nota(nota):
            notas_temp.append(nota)
            break
        except ValueError:
          print("Error: Valor inválido")
    return notas_temp

  #Método Analizador para ingresar notas
  def ingresar_notas(self):
    self.nota = Estudiante.recopilar_notas()
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
    if not self.nota:
      print(f"Error: {self.nombre} {self.apellido} no tiene notas registradas")
      return
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
      while True:
        cedula=input("Ingrese la cédula del estudiante: ")
        if Estudiante.validar_cedula(cedula):
          break
      while True:
        nombre=input("Ingrese el nombre del estudiante: ")
        if Estudiante.validar_nombre(nombre):
          break
      while True:
        apellido=input("Ingrese el apellido del estudiante: ")
        if Estudiante.validar_apellido(apellido):
          break
      while True:
        asignatura=input("Ingrese la asignatura del estudiante: ")
        if Estudiante.validar_asignatura(asignatura):
          break
      notas=Estudiante.recopilar_notas()
      objeto_estudiante=Estudiante(cedula,nombre,apellido,asignatura)
      objeto_estudiante.nota=notas
      estudiantes.append(objeto_estudiante)
      print("Estudiante registrado correctamente")
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