#testing 

from persona import Persona, Validador
import pytest

def test_nombre_valido():
    assert Validador.nombre_valido("Jorge") is True
    with pytest.raises(ValueError):
        Validador.nombre_valido("1234")

def test_edad_valida():
    assert Validador.edad_valida("20") is True
    with pytest.raises(ValueError):
        Validador.edad_valida("-5")

def test_email_valido():
    assert Validador.email_valido("jorge@gmail.com") is True
    with pytest.raises(ValueError):
        Validador.email_valido("jorge@123.com")

def test_persona_mayor_edad():
    persona = Persona("Jorge", 20, "jorge@gmail.com")
    assert persona.es_mayor_edad() == " Soy mayor de edad"

def test_cambiar_email():
    persona = Persona("Jorge", 20, "jorge@gmail.com")
    persona.cambiar_email("nuevo@gmail.com")
    assert persona.email == "nuevo@gmail.com"
