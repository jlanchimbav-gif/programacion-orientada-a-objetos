def escanear_matriz():
    # Solicitar filas y columnas con validación
    while True:
        try:
            filas = int(input("Ingrese el número de filas (1-20): "))
            columnas = int(input("Ingrese el número de columnas (1-20): "))
            
            if 1 <= filas <= 20 and 1 <= columnas <= 20:
                break
            else:
                print("⚠️ Error: filas y columnas deben estar entre 1 y 20.")
        except ValueError:
            print("⚠️ Error: ingrese solo números enteros positivos.")

    # Crear matriz con valores secuenciales
    matriz = []
    contador = 1
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(contador)
            contador += 1
        matriz.append(fila)

    # Mostrar encabezado de columnas
    print("\n📋 Escaneo de la matriz:")
    print("     ", end="")
    for j in range(columnas):
        print(f"C{j+1:3}", end=" ")
    print()

    # Mostrar filas con índices
    for i in range(filas):
        print(f"F{i+1:3}", end=" ")
        for valor in matriz[i]:
            print(f"{valor:3}", end=" ")
        print()


# Ejecutar el programa
escanear_matriz()




 


