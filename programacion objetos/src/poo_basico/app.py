from __future__ import annotations

try:
    # Ejecución recomendada: python -m src.poo_basico.app
    from src.poo_basico.persona import Persona
    from src.poo_basico.saludo import Saludo
except ModuleNotFoundError:
    # Ejecución directa: python src/poo_basico/app.py
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parents[1]))
    from poo_basico.persona import Persona
    from poo_basico.saludo import Saludo


def main() -> None:
    persona = Persona("Jaguar EW")
    print(persona.presentarse())

    Saludo("Hola desde POO!").mostrar()


if __name__ == "__main__":
    main()

