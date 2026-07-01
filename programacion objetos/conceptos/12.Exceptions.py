## Raise Exceptions##
## son errores que ocurren durante la ejecucion del programa ##
## se utilizan para manejar errores y evitar que el programa se detenga ##

# ejemplo de exception

try:
    edad = int(input("Ingrese su edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
except ValueError as e:
    print(f"Error: {e}")



#TRY Y CATCH ejemplo 1##
try:
    edad = int(input("Ingrese su edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
except ValueError as e:
    print(f"Error: {e}")

## finally ejemplo ##
try:
    edad = int(input("Ingrese su edad: "))
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
except ValueError as e:
    print(f"Error: {e}")
finally:
    print("Fin del programa")






