class Persona:                                                   # metodos y atributos 
    def __init__(self, nombre, edad, email):
        self.nombre = nombre
        self.edad = edad
        self.email = email if self.email_valido(email) else ""

    @staticmethod                                                 # metodo estatico para validar gmail
    def email_valido(email):
        for caracter in email:
            if caracter.isdigit():
                print("El correo no puede contener números")
                return False
        return True

    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

    def es_mayor_edad(self):
        if self.edad <= 0:
            print("La edad no puede ser cero o negativa")
        elif self.edad >= 18:
            print("Soy mayor de edad")
        else:
            print("Soy menor de edad")

    def cambiar_email(self, nuevo_email):
        if self.email_valido(nuevo_email):
            self.email = nuevo_email


if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    edad = int(input("Ingresa tu edad: "))
    email = input("Ingresa tu email: ")
    while not Persona.email_valido(email):
        email = input("Ingresa tu email (sin números): ")

    persona = Persona(nombre, edad, email)

    persona.presentarse()
    persona.es_mayor_edad()

    nuevo_email = input("Ingresa tu nuevo email: ")
    while not Persona.email_valido(nuevo_email):
        nuevo_email = input("Ingresa tu nuevo email (sin números): ")
    persona.cambiar_email(nuevo_email)
    print(f"Email actualizado a: {persona.email}")
