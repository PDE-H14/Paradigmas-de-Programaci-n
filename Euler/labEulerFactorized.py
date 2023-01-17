#----------------------------------#
# Porfirio Damián Escamilla Huerta #
#----------------------------------#

import math

#--------------------------------#
# e^x como polinomio factorizado #
#--------------------------------#

x = 1

n = 1000000

def e_to_power_x_factorized(x,precision):
  i = n
  e = 0
  flag = False
  if x < 0:
      x = -x
      flag = True
  while i>0:
    e = 1 + ((x*e)/i)
    i-=1
  if flag:
      return 1/e
  else:
      return e

    
print("e generado por el algoritmo de la clase", e_to_power_x_factorized(x,n))
print("e de math.exp", math.exp(x))

