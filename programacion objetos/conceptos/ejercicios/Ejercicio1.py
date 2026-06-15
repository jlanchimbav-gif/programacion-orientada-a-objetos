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


def pedir_nota(mensaje, minimo, maximo):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"La nota debe estar entre {minimo} y {maximo}.")
        except ValueError:
            print("Ingrese un número válido.")


def main():
    print("--- Registro de estudiante ---")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    cedula = input("Ingrese la cédula: ")

    n1 = pedir_nota("Ingrese la nota 1 (0-15): ", 0, 15)
    n2 = pedir_nota("Ingrese la nota 2 (0-15): ", 0, 15)
    n3 = pedir_nota("Ingrese la nota 3 (0-15): ", 0, 15)
    n4 = pedir_nota("Ingrese la nota 4 (0-15): ", 0, 15)
    ex1 = pedir_nota("Ingrese la nota del examen 1 (0-20): ", 0, 20)
    ex2 = pedir_nota("Ingrese la nota del examen 2 (0-20): ", 0, 20)

    estudiante = Estudiante(nombre, apellido, cedula, n1, n2, n3, n4, ex1, ex2)

    print("\n--- Datos del estudiante ---")
    estudiante.imprimirDatos()
    print("\n--- Resultado ---")
    estudiante.mostrarResultado()


if __name__ == "__main__":
    main()
