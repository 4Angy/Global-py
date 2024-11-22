import random

class Detector:
    def __init__(self, matriz_adn):
        self.matriz_adn = matriz_adn

    def hayMutacion(self):
        return {
            "horizontalSi": self._detectar_horizontal(),
            "verticalSi": self._detectar_vertical(),
            "diagonalSi": self._detectar_diagonal()
        }

    def _detectar_horizontal(self):
        for fila in self.matriz_adn:
            if self._contiene_secuencia_repetida(fila):
                return True
        return False

    def _detectar_vertical(self):
        for col in zip(*self.matriz_adn): 
            if self._contiene_secuencia_repetida(col):
                return True
        return False

    def _detectar_diagonal(self):
        n = len(self.matriz_adn)
        diagonales = []

        for d in range(-n + 1, n):
            diagonal = [self.matriz_adn[i][i - d] for i in range(max(0, d), min(n, n + d))]
            diagonales.append(diagonal)

        for d in range(-n + 1, n):
            diagonal = [self.matriz_adn[i][n - 1 - (i - d)] for i in range(max(0, d), min(n, n + d))]
            diagonales.append(diagonal)

        for diagonal in diagonales:
            if self._contiene_secuencia_repetida(diagonal):
                return True
        return False

    def _contiene_secuencia_repetida(self, secuencia):
        if len(secuencia) < 4:
            return False
        for i in range(len(secuencia) - 3):
            if secuencia[i] == secuencia[i + 1] == secuencia[i + 2] == secuencia[i + 3]:
                return True
        return False


class Mutador:
    def __init__(self, base_nitrogenada):
        self.base_nitrogenada = base_nitrogenada

    def crear_mutante(self):
        pass


class Radiacion(Mutador):
    def crear_mutante(self, matriz, posicion_inicial, orientacion_de_la_mutacion):
        try:
            fila, columna = posicion_inicial
            orientacion_de_la_mutacion = orientacion_de_la_mutacion.upper()

            if orientacion_de_la_mutacion == "H":
                if columna + 3 < len(matriz[0]):

                    for i in range(4):
                        matriz[fila][columna + i] = self.base_nitrogenada
                else:
                    raise IndexError("La mutación horizontal excede los límites de la matriz.")
            
            elif orientacion_de_la_mutacion == "V":
                if fila + 3 < len(matriz):

                    for i in range(4):
                        matriz[fila + i][columna] = self.base_nitrogenada
                else:
                    raise IndexError("La mutación vertical excede los límites de la matriz.")
            
            else:
                raise ValueError("Orientación no válida. Use 'H' o 'V'.")
            
            return matriz
        except IndexError as e:
            raise IndexError(f"Error al mutar: {e}")
        except Exception as e:
            raise RuntimeError(f"Error al crear el mutante: {str(e)}")


class Virus(Mutador):
    def crear_mutante(self, matriz, posicion_inicial):
        try:
            fila, columna = posicion_inicial
            for i in range(4):
                matriz[fila + i][columna + i] = self.base_nitrogenada
            return matriz
        except IndexError:
            raise IndexError("La posición inicial o la orientación excede los límites de la matriz.")
        except Exception as e:
            raise RuntimeError(f"Error al crear el mutante: {str(e)}")


class Sanador:
    def __init__(self, detector):
        self.detector = detector

    def sanar_mutantes(self, matriz_adn):
        mutaciones = self.detector.hayMutacion()
        
        if not (mutaciones["horizontalSi"] or mutaciones["verticalSi"] or mutaciones["diagonalSi"]):
            return matriz_adn, "No hay mutaciones, el ADN está limpio."

        nuevo_adn = self.generar_adn_sano()
        return nuevo_adn, "El ADN fue sanado y se generó uno nuevo sin mutaciones."

    def generar_adn_sano(self):
        bases = ['A', 'T', 'C', 'G']
        tamaño = 6 
        return [[random.choice(bases) for _ in range(tamaño)] for _ in range(tamaño)]


def ingresar_adn():
    adn = []
    print("Ingrese la secuencia de ADN, 6 letras por fila (A, G, T, C).")
    for i in range(6):
        while True:
            fila = input(f"Ingrese la fila {i+1}: ").upper()
            if len(fila) == 6 and all(base in 'AGTC' for base in fila):
                adn.append(list(fila))
                break
            else:
                print("Entrada inválida. Asegúrese de ingresar 6 letras (A, G, T, C) por fila.")
    return adn
