                                                           # con def  creamos una funcion con el nombre contador_palabras ##
def contador_palabras():
                                                           # 1 solicitamos al usuario una frase
    frase = input("Por favor, ingresa una frase: ")
                                                           # 2 Procesar la frase.
    import re                                              #Se convierte toda la frase a minúsculas para ignorar mayúsculas/minúsculas.
    palabras = re.findall(r'\b[\w-]+\b', frase.lower())    #Se usa re.findall con el patrón \b[\w-]+\b para extraer palabras,
                                                           #ignora las  comas y puntos .

                                            # 3 Contar ocurrencias de cada palabra
    contador = {}                           #Se crea un diccionario (contador) donde las claves son las palabras y los valores sus conteos. 
    for palabra in palabras:
        if palabra in contador:             #verifica que la frese no este vacia y que contenga al menos una palabra 
            contador[palabra] += 1          # Si no hay palabras en el diccionario, las funciones max() o min() lanzan una excepción porque intentan 
                                             #acceder a claves inexistente
        else:
            contador[palabra] = 1

    # Encontrar palabra más y menos frecuente
    if not contador:  # Evitar error si la frase está vacía
        print("La frase ingresada está vacía.")
        return

    max_palabra = max(contador, key=contador.get)            #max(contador, key=contador.get) encuentra la palabra con mayor frecuencia.
    min_palabra = min(contador, key=contador.get)            #min(contador, key=contador.get) encuentra la palabra con menor frecuencia 
                                                             #y si hay empate, elige la primera en orden alfabético.

    # Mostrar resumen
    print("\n--- Resumen de palabras ---")
    for palabra, cantidad in sorted(contador.items()):       
        print(f"{palabra}: {cantidad}")
                                                            #e imprime un resumen ordenado alfabéticamente y las palabras más a menos frecuentes.
    print(f"\nPalabra más frecuente: '{max_palabra}' (aparece {contador[max_palabra]} veces)")
    print(f"Palabra menos frecuente: '{min_palabra}' (aparece {contador[min_palabra]} veces)")

# Ejecutar la función
contador_palabras()
