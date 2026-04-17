from __future__ import annotations

import runpy
import sys
from pathlib import Path

try:
    # Ejecución recomendada: python -m src.poo_basico.app
    from src.poo_basico.persona import Persona
    from src.poo_basico.saludo import Saludo
except ModuleNotFoundError:
    # Ejecución directa: python src/poo_basico/app.py
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[1]))
    from poo_basico.persona import Persona
    from poo_basico.saludo import Saludo


def ejecutar_conceptos() -> None:
    base_dir = Path(__file__).resolve().parents[2]
    conceptos_dir = base_dir / "conceptos"
    archivos_conceptos = sorted(conceptos_dir.glob("*.py"))

    rutas_necesarias = (str(base_dir), str(conceptos_dir))
    for ruta in rutas_necesarias:
        if ruta not in sys.path:
            sys.path.insert(0, ruta)

    print("\n=== Ejecutando ejemplos de conceptos ===")
    for archivo in archivos_conceptos:
        print(f"\n--- {archivo.name} ---")
        try:
            runpy.run_path(str(archivo), run_name="__main__")
        except Exception as exc:
            print(f"No se pudo ejecutar {archivo.name}: {exc}")


def main() -> None:
    persona = Persona("Jaguar EW")
    print(persona.presentarse())

    Saludo("Hola desde POO!").mostrar()
    ejecutar_conceptos()


if __name__ == "__main__":
    main()

