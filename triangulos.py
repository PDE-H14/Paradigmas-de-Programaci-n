#----------------------------------#
# Porfirio Damián Escamilla Huerta #
#----------------------------------#

import math


class Triángulo():
    def __init__(self, a: float, b: float, c: float, alpha: float, theta: float, gamma: float):
        """__init__

        El constructor del objeto triángulo inicializa sus variables.

        Parametros:
            a (float): Lado a de un triángulo
            b (float): Lado b de un triángulo
            c (float): Lado c de un triángulo
            alpha (float): Ángulo alpha de un triángulo
            theta (float): Ángulo theta de un triángulo
            gamma (float): Ángulo gamma de un triángulo
        """
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c
        self.alpha = alpha
        self.theta = theta
        self.gamma = gamma

    def perímetro(self):
        """perímetro

        Calculoa el perímetro.

        Retorna:
            float: perímetro
        """
        perímetro = self.ladoA + self.ladoB + self.ladoC
        return perímetro

    def es_triángulo_lados(self):
        """es_triángulo_lados

        Evalua si los valores ingresados pueden formar un tríangulo según sus lados.

        Retorna:
            bool: Si es o no un triángulo
        """
        if self.ladoA + self.ladoB > self.ladoC and self.ladoA + self.ladoC > self.ladoB and self.ladoB + self.ladoC > self.ladoA:
            return True
        else:
            return False

    def es_triángulo_ángulos(self):
        """es_triángulo_ángulos

        Evalua si los valores ingresados pueden formar un tríangulo según sus ángulos.

        Retorna:
            bool: Si es o no un triángulo
        """
        if self.alpha + self.gamma + self.theta == 180:
            return True
        else:
            return False


triángulo1 = Triángulo(1.2, 2.3, 3.4, 30, 90, 60)

print("¿Es un triángulo según sus lados?", triángulo1.es_triángulo_lados())
print("¿Es un triángulo según sus ángulos?", triángulo1.es_triángulo_ángulos())
print("Método perímetro", triángulo1.perímetro())
print(type(triángulo1.perímetro()))


class Triángulo_equilátero(Triángulo):
    def __init__(self, a: float = 0):
        """__init__

        Args:
            a (float, optional): Longitud de los lados.
        """
        super().__init__(a, a, a, 60, 60, 60)

    def área(self):
        área = (self.ladoA**2)*(3**1/2)/4
        return área


triángulo2 = Triángulo_equilátero(1)
print("Método heredada (perímetro)", triángulo2.perímetro())
print("Método propia (área)", triángulo2.área())


class Triángulo_rectángulo(Triángulo):
    
    def área(self):
        área = (self.ladoA*self.ladoB)/2
        return área
