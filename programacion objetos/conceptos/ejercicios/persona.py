import re                                                                                # libreria de expresiones regulares 

class Validador:                                                                         # contine metodos estaticos para validar informacion +                                                                
    @staticmethod                                                                        # rise exceptions para tratar errores
    def nombre_valido(nombre: str) -> bool:
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if nombre.isdigit():
            raise ValueError("El nombre no puede ser números")
        return True

    @staticmethod                                                        # contiene los metodos para validar la edad + el tretamiento de errores
    def edad_valida(edad: str) -> bool:
        if not edad.isdigit():
            raise ValueError("La edad debe ser un número entero positivo")
        edad = int(edad)
        if edad <= 0:
            raise ValueError("La edad no puede ser cero o negativa")
        return True

    @staticmethod                                                               # metodo para validar email 
    def email_valido(email: str) -> bool: 
        patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"                 #Este paton reconoce los simbolos,letras y numeros del email ingresado
        if not re.match(patron, email):                                         # y valida el patron del gmail
            raise ValueError("Formato de email inválido. Ejemplo válido: usuario@gmail.com")
        return True


class Persona:                                                      # creacion de clase, sus metodos y atributos 
    def __init__(self, nombre: str, edad: int, email: str):
        self.nombre = nombre
        self.edad = edad
        self.email = email

    def __str__(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"      #funciones para presentar la información 

    def es_mayor_edad(self) -> str:
        if self.edad >= 18:
            return " Soy mayor de edad"                  #funcion para validar edad return devuelve el mesaje de error
        return " Soy menor de edad"

    def cambiar_email(self, nuevo_email: str):         # funcion para cambiar email
        self.email = nuevo_email


def pedir_dato(mensaje: str, validador) -> str:
    """Función genérica para pedir datos con validación y manejo de excepciones"""
    while True:
        dato = input(mensaje)
        try:
            if validador(dato):
                return dato
        except ValueError as e:
            print(f"❌ {e}")


if __name__ == "__main__":
    # Entrada con validaciones robustas
    nombre = pedir_dato("Ingresa tu nombre: ", Validador.nombre_valido)
    edad = int(pedir_dato("Ingresa tu edad: ", Validador.edad_valida))
    email = pedir_dato("Ingresa tu email: ", Validador.email_valido)

    persona = Persona(nombre, edad, email)

    # Presentación
    print(persona)
    print(persona.es_mayor_edad())

    # Cambio de email con validación
    nuevo_email = pedir_dato("Ingresa tu nuevo email: ", Validador.email_valido)
    persona.cambiar_email(nuevo_email)
    print(f"📧 Email actualizado a: {persona.email}")


    



