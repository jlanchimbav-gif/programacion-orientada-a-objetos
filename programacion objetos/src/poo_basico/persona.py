from __future__ import annotations


class Persona:
    """Entidad simple para practicar encapsulación."""

    def __init__(self, nombre: str) -> None:
        self._nombre = nombre.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    def presentarse(self) -> str:
        return f"Me llamo {self._nombre}."

