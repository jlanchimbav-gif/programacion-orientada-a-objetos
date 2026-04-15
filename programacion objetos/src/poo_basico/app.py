from __future__ import annotations

from src.poo_basico.persona import Persona
from src.poo_basico.saludo import Saludo


def main() -> None:
    persona = Persona("Ana")
    print(persona.presentarse())

    Saludo("Hola desde POO!").mostrar()


if __name__ == "__main__":
    main()

