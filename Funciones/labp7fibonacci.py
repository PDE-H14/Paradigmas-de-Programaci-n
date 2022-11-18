#-----------------------------#
# Recursividad y memorizacion #
#-----------------------------#

#----------------------------------------------#
# Importamos herramientas para la memirizacion #
#----------------------------------------------#

from functools import lru_cache


def fibonacci_lento(n):
    if n == 1 or n == 2:
        return 1
    if n > 2:
        return fibonacci_lento(n-1) + fibonacci_lento(n-2)


for i in range(1, 36):
    print(str(i)+":"+str(fibonacci_lento(i)))
#-----------------------------------------------------#
# Optimizacion 1: Uso de conjuntos para guardar valores #
#-----------------------------------------------------#

fibonaccis = {}


def fibonacci(n):

    #-----------------------------------------#
    # Revisa si ya  existe y regresa el valor #
    #-----------------------------------------#

    if n in fibonaccis:
        return fibonaccis[n]
    if n == 1:
        valor = 1
    elif n == 2:
        valor = 1
    elif n > 2:
        valor = fibonacci(n-1) + fibonacci(n-2)

    #----------#
    # Guardalo #
    #----------#

    fibonaccis[n] = valor
    return valor


for i in range(1, 10001):
    print(str(i)+":"+str(fibonacci(i)))
#---------------------------------------#
# Optimizacion 2: Uso de decoradores para memorizacion  #
# maxsize: es cuantos anteriores guarde #
#---------------------------------------#


@lru_cache(maxsize=3)
def nfibonacci(n: int):
    if type(n) != int:
        raise TypeError("n debe ser un entero positivo.")
    if n < 1:
        raise TypeError("n debe ser un entero positivo.")
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return nfibonacci(n-1) + nfibonacci(n-2)


for i in range(1, 10001):
    print(str(i)+":"+str(nfibonacci(i)))
