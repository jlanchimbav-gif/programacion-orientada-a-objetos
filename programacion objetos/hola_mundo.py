"""Hola mundo con programación orientada a objetos."""


class Saludo:
    """Representa un mensaje de saludo."""

    def __init__(self, mensaje: str = "Hola mundo") -> None:
        self._mensaje = mensaje

    def mostrar(self) -> None:
        """Muestra el mensaje por consola."""
        print(self._mensaje)


if __name__ == "__main__":
    saludo = Saludo()
    saludo.mostrar()
