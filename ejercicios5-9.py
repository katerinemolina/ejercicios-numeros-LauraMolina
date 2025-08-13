# Este programa permite al usuario registrar números del 0 al 9
# y ver algunas estadísticas sobre ellos.

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
    print("3. Ver cuántas veces apareció cada número")
    print("4. Calcular la media de las apariciones")
    print("5. Ver el número más frecuente")
    print("6. Ver el número menos frecuente")
    print("7. Ver la diferencia entre números pares e impares")
    print("8. Ver el total de números ingresados")
    print("9. Salir del programa")

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
        print() # Imprime una línea vacía para el formato.

    elif opcion == '3':
        # Opción 3: Ver apariciones
        print("\nApariciones de cada número:")
        for i in range(10):
            print(f"Número {i}: {frecuencias[i]} veces")

    elif opcion == '4':
        # Opción 4: Ver la media
        total_apariciones = 0
        for i in range(10):
            total_apariciones = total_apariciones + frecuencias[i]
        
        if total_apariciones > 0:
            media = total_apariciones / 10
            print(f"La media de las apariciones es: {media:.2f}")
        else:
            print("Todavía no se han registrado números para calcular la media.")

    elif opcion == '5':
        # Opción 5: El número más frecuente
        if sum(frecuencias) == 0:
            print("Todavía no se han registrado números.")
        else:
            max_frecuencia = -1
            for frecuencia in frecuencias:
                if frecuencia > max_frecuencia:
                    max_frecuencia = frecuencia
            
            numeros_mas_frecuentes = []
            for i in range(10):
                if frecuencias[i] == max_frecuencia:
                    numeros_mas_frecuentes.append(i)
            
            # Aquí imprimimos los resultados.
            numeros_str = [str(n) for n in numeros_mas_frecuentes]
            print(f"El/los número(s) más frecuente(s) es/son: {', '.join(numeros_str)} con {max_frecuencia} apariciones.")

    elif opcion == '6':
        # Opción 6: El número menos frecuente
        if sum(frecuencias) == 0:
            print("Todavía no se han registrado números.")
        else:
            # Buscamos la frecuencia mínima, pero solo de los números que ya fueron elegidos.
            min_frecuencia = -1
            for frecuencia in frecuencias:
                if frecuencia > 0:
                    if min_frecuencia == -1 or frecuencia < min_frecuencia:
                        min_frecuencia = frecuencia
            
            if min_frecuencia == -1: # Si no se encontró ninguna frecuencia mayor a 0
                print("Todavía no se han registrado números.")
            else:
                numeros_menos_frecuentes = []
                for i in range(10):
                    if frecuencias[i] == min_frecuencia:
                        numeros_menos_frecuentes.append(i)
                
                numeros_str = [str(n) for n in numeros_menos_frecuentes]
                print(f"El/los número(s) menos frecuente(s) es/son: {', '.join(numeros_str)} con {min_frecuencia} apariciones.")

    elif opcion == '7':
        # Opción 7: Diferencia entre pares e impares
        apariciones_pares = 0
        apariciones_impares = 0
        
        for i in range(10):
            if i % 2 == 0: # Si el número es par
                apariciones_pares = apariciones_pares + frecuencias[i]
            else: # Si el número es impar
                apariciones_impares = apariciones_impares + frecuencias[i]
        
        diferencia = abs(apariciones_pares - apariciones_impares)
        print(f"Total de apariciones de números pares: {apariciones_pares}")
        print(f"Total de apariciones de números impares: {apariciones_impares}")
        print(f"Diferencia: {diferencia}")

    elif opcion == '8':
        # Opción 8: Total de apariciones
        total_apariciones = 0
        for i in range(10):
            total_apariciones = total_apariciones + frecuencias[i]
        print(f"El total de apariciones de todos los números es: {total_apariciones}")

    elif opcion == '9':
        # Opción 9: Salir del programa
        print("Saliendo del programa. ¡Hasta luego!")
        break  # Esto rompe el bucle 'while True' y termina el programa.

    else:
        # Si el usuario elige una opción que no existe
        print("Opción no válida. Por favor, elige una opción del 1 al 9.")