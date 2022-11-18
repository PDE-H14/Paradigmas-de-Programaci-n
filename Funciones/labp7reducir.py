#------------------------------------------#
# Uso de reducciones (colapsar resultados) #
#------------------------------------------#


from functools import reduce

#-------------------------------------------------#
# Multiplicacion de todos los numeros en la lista #
#-------------------------------------------------#


bigdata = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

#-------------#
# Funcion x*y #
#-------------#


def multiplicar(x, y): return x*y


print(reduce(multiplicar, bigdata))

#----------------------------------------------------------#
# Reduce le aplica la funcion por pares a los resultados y #
#   el siguiente elemento comenzando con os dos primeros   #
#                         elementos                        #
#----------------------------------------------------------#
