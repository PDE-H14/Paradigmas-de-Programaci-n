#----------------------------------#
# Porfirio Damián Escamilla Huerta #
#----------------------------------#

import math

class Triángulo():
    def __init__(self, a:float, b:float, c:float, alpha:float, theta:float, gamma:float):
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c
        self.alpha = alpha
        self.theta = theta
        self.gamma = gamma
    def perímetro(self):
        perímetro = self.ladoA + self.ladoB + self.ladoC
        return perímetro
    def es_triángulo(self):
        if self.ladoA + self.ladoB > self.ladoC and self.ladoA + self.ladoC > self.ladoB and self.ladoB + self.ladoC > self.ladoA:
            return True
        else:
            return False

triángulo1 = Triángulo(1.2, 2.3, 3.4, 30, 90, 60)

print(triángulo1.perímetro())
print(triángulo1.es_triángulo())
print(type(triángulo1.perímetro()))

class Triángulo_equilátero(Triángulo):
    def __init__(self, lado=1):
        super().__init__(lado, lado, lado, 60, 60, 60)
    def área(self):
        área = self.lado/2 * self.lado*(3**1/2)/2
        return área

triángulo2 = Triángulo_equilátero(3)
print(triángulo2.perímetro())