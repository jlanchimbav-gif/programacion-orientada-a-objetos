class Estudiante:
    def __init__(self, nombre, apellido, cedula, n1, n2, n3, n4, ex1, ex2):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.ex1 = ex1
        self.ex2 = ex2

    def calcular_nota_final(self):
        return (self.n1 + self.n2 + self.n3 + self.n4 + self.ex1 + self.ex2) / 6

    def presentar_informacion(self):
        nota_final = self.calcular_nota_final()
        print(f"Nombre: {self.nombre} Apellido: {self.apellido} Cédula: {self.cedula} Nota Final: {nota_final:.2f}")

    def __str__(self):
        nota_final = self.calcular_nota_final()
        return f"Estudiante(nombre={self.nombre}, apellido={self.apellido}, cedula={self.cedula}, nota_final={nota_final:.2f})"
