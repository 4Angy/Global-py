from clases import Detector, Radiacion, Virus, Sanador, ingresar_adn

def main():
    adn = ingresar_adn()

    detector = Detector(adn)
    radiacion = Radiacion("G")  # Puedes cambiar la base nitrogenada por la que desees
    virus = Virus("A")  # Igualmente puedes elegir otra base
    sanador = Sanador(detector)

    while True:
        print("\nSeleccione la opción que quiere ver:")
        print("--------------------")
        print("1. Detectar mutaciones.")
        print("2. Mutar con radiación.")
        print("3. Mutar con virus.")
        print("4. Sanar mutación.")
        print("5. Salir")

        opcion = input()

        if opcion == "1":
            mutaciones = detector.hayMutacion()
            if mutaciones["horizontalSi"]:
                print("Mutacion(es) en direccion horizontaldetectada(s).")
            if mutaciones["verticalSi"]:
                print("Mutacion(es) en direccion vertical detectada(s).")
            if mutaciones["diagonalSi"]:
                print("Mutacion(es) en direccion diagonal detectada(s).")
            if not (mutaciones["horizontalSi"] or mutaciones["verticalSi"] or mutaciones["diagonalSi"]):
                print("No se detectaron mutaciones.")

        elif opcion == "2":
            fila = int(input("Fila de la posición inicial (0-5): "))
            columna = int(input("Columna de la posición inicial (0-5): "))
            orientacion = input("Orientación de la mutación (H para horizontal, V para vertical): ")
            try:
                adn_mutado = radiacion.crear_mutante(adn, (fila, columna), orientacion)
                print("ADN después de la mutación con radiación:")
                for fila in adn_mutado:
                    print(fila)
            except Exception as e:
                print(e)

        elif opcion == "3":
            fila = int(input("Fila de la posición inicial (0-5): "))
            columna = int(input("Columna de la posición inicial (0-5): "))
            try:
                adn_mutado = virus.crear_mutante(adn, (fila, columna))
                print("ADN después de la mutación con virus:")
                for fila in adn_mutado:
                    print(fila)
            except Exception as e:
                print(e)

        elif opcion == "4":

            adn_sano, mensaje = sanador.sanar_mutantes(adn)
            adn = adn_sano
            print(mensaje)
            for fila in adn:
                print(fila)

        elif opcion == "5":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
