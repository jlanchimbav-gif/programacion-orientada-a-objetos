from __future__ import annotations


class Saludo:
    """Representa un saludo configurable."""

    def __init__(self, mensaje: str = "Hola mundo") -> None:
        self._mensaje = mensaje

    @property
    def mensaje(self) -> str:
        return self._mensaje

    def mostrar(self) -> None:
        print(self._mensaje)

