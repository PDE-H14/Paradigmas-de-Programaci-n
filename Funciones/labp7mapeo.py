#-------------------#
# Funcion pura x**2 #
#-------------------#

def alcuadrado(x):
    return x*x

#-------------------#
# Funcion pura x**3 #
#-------------------#


def alcubo(x):
    return x*x*x
    
#---------------------------#
# Mapeo de una funcion pura #
#---------------------------#


def mapeo(func, lista_numeros):
    resultado = []
    for i in lista_numeros:
        resultado.append(func(i))
    return resultado


cuadrados = mapeo(alcuadrado, [2.1, 2.2, 2.3,
                  2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.0j])
cubos = mapeo(alcubo, [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 2.0j])
print(cuadrados)
print(cubos)

#-------------------------------#
# Funciones dentro de funciones #
#-------------------------------#


def Mayusculas(texto: str):
    return texto.upper()


def minusculas(texto: str):
    return texto.lower()


def saludar(func, nombre: str):
    saludo = func("Hola, Como estas? "+nombre)
    print(saludo)

#-------------#
# Con strings #
#-------------#


saludar(Mayusculas, "Damian")
saludar(minusculas, "Porfirio")

#------------------------------------------#
# Funciones abstractas dentro de funciones #
#       Su resultado es otra funcion       #
#------------------------------------------#


def divisor(x):
    def dividendo(y):
        return y/x
    return dividendo

#----------------------------------#
# Primero generamos la funcion y/2 #
#----------------------------------#


division = divisor(2)

#-----------------------------#
# La usamos para calcular 3/2 #
#-----------------------------#

print(division(3))

#-------------------------------------#
# Uso de la funcion map con una lista #
#-------------------------------------#

#------------------------------------#
# Lista de ciudades y su temperatura #
#------------------------------------#

temps = [("Berlin", 29), ("Cairo", 36), ("Buenos Aires", 19), ("Los Angeles", 26), ("Tokyo",
                                                                                    27), ("Nueva York", 28), ("Londres", 22), ("Pekin", 32), ("Mexico Tenochtitlan", 23)]


def C_a_F(datos): return (datos[0], (9/5)*datos[1]+32)


print(list(map(C_a_F, temps)))
