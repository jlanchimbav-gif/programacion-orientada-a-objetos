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

    def imprimirDatos(self):
        print(f"Estudiante: {self.nombre} {self.apellido}")
        print(f"Cédula: {self.cedula}")
        print(f"Notas: {self.n1}, {self.n2}, {self.n3}, {self.n4}")
        print(f"Exámenes: {self.ex1}, {self.ex2}")

    def mostrarResultado(self):
        nota = self.calcular_nota_final()
        self.resultado = "Aprobado" if nota >= 7 else "Reprobado"
        print(f"Nota final: {nota:.2f}")
        print(f"Resultado: {self.resultado}")
