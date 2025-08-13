# Creamos una lista para guardar la frecuencia de cada número.
# El índice 0 es para el número 0, el 1 para el 1, y así sucesivamente.
# Todos los contadores empiezan en cero.
frecuencias = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Creamos una lista para guardar los números que el usuario ha elegido.
# Es una lista simple para que sea más fácil de entender.
numeros_elegidos = []

# Este bucle principal hará que el programa se ejecute una y otra vez
# hasta que el usuario decida salir.
while True:
    print("\n--- MENÚ ---")
    print("1. Ingresar un número del 0 al 9")
    print("2. Ver qué números no han sido elegidos")
 
    opcion = input("Elige una opción: ")

    if opcion == '1':
        # Opción 1: Pedir un número al usuario
        while True:
            numero_valido = False
            try:
                numero_str = input("Introduce un número del 0 al 9: ")
                numero = int(numero_str)

                if 0 <= numero <= 9:
                    # Si el número es válido, lo registramos.
                    frecuencias[numero] = frecuencias[numero] + 1
                    # Verificamos si el número ya está en nuestra lista de elegidos.
                    if numero not in numeros_elegidos:
                        # Si no está, lo agregamos.
                        numeros_elegidos.append(numero)
                    
                    print(f"Número {numero} registrado. Frecuencia actual: {frecuencias[numero]}")
                    numero_valido = True
                else:
                    print("Error: El número debe estar entre 0 y 9.")
            except ValueError:
                print("Error: Por favor, introduce un número válido.")
            
            # Si el número fue válido, salimos de este bucle interno.
            if numero_valido:
                break

    elif opcion == '2':
        # Opción 2: Ver números no elegidos
        print("Números que aún no han sido elegidos:")
        todos_los_numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        alguno_no_elegido = False
        
        for numero_posible in todos_los_numeros:
            if numero_posible not in numeros_elegidos:
                print(numero_posible, end=' ')
                alguno_no_elegido = True
        
        if not alguno_no_elegido:
            print("Todos los números del 0 al 9 han sido elegidos al menos una vez.")
        print() # Imprime una línea vacía para el formato.