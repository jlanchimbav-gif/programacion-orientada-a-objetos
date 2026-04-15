# Programaci?n orientada a objetos (POO) ? base

Estructura m?nima para practicar POO en Python.

## Estructura

- `hola_mundo.py`: ejemplo r?pido.
- `src/poo_basico/`: ?paquete? con clases.
- `tests/`: tests con `unittest` (sin dependencias).

## C?mo ejecutar

Desde la carpeta `programacion objetos`:

```powershell
python -m src.poo_basico.app
python hola_mundo.py
python -m unittest discover -s tests -v
```

> Si `python hola_mundo.py` no encuentra `poo_basico`, ejecuta usando:
>
> ```powershell
> $env:PYTHONPATH="src"
> python hola_mundo.py
> ```

