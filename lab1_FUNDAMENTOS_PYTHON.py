#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Porfirio Damián Escamilla Huerta #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#=====================#
# Operaciones básicas #
#=====================#

print(2+3)
print(2*3)
print(2/3)
print(7//3)
print(2**10)
print(2**0.5) #raíz cuadrada
print(10%2)
print(10%0.2) #esclusivo de python

#==========================================#
# Para saber el tipo de objeto se usa type #
#==========================================#

t=0
print(type(t)) #entero
t=3.6
print(type(t)) #real (flotante)
t=True
print(type(t)) #booleano (bool)

#=====================#
# Mensajes a pantalla #
#=====================#

print("Este es un comando de python. ", "Este es otro enunciado. ", t)
print('id: ', 1)
print('First name: ', 'Steve')
print('Last name: ', 'Jobs')
print("Vamos a sumar esto "+"con esto otro (concatenar)")

#===============================================#
# Continuar una instruccion en varios renglones #
#===============================================#

if 100 > 99 and \
   200 <= 300 and \
   True != False:
	print("Hello world!") 

#======================================#
#Comandos diferentes en la misma linea #
#======================================#

print("Hola "); print("tú!")  #Se considera mala práctica

#================================================#
# Usando paréntesis redondos, corchetes o llaves #
#    se puede escribir en varios renglones.      #
#================================================#

list = [1, 2, 3, 4,
	5, 6, 7, 8,
	9, 10, 11, 12]
matrix = [[1,0,0],[0,1,0],[0,0,1]]

print(list)
print(matrix)

#================================================#
# Identación estricta para procesos dependientes #
#           de : (colon, dos puntos)             #
#================================================#

if 10>5:
	print("Diez es mayor que cinco. ")
	print("Otra identación. ")
for i in list:
	print('i')
	print("ok. ")
if 10>5:
	print("Verdadero. ")
	if 10<20:
		print("Verdadero. ")
elif 5>3: #Comienza segundo condicional
	print("Esto no se imprimirá. ")
else:
	print("Aquí nunca llegará. ")

#===========#
# Funciones #
#===========#

def say_hello(name):
	print("Hello ", name)
	print("Welcome to Python tutorials :)")
say_hello("Porfirio")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Porfirio Damián Escamilla Huerta #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#======================================================#
# Input permite obtener datos del usuarion en prompter #
#======================================================#

nombre = input("Dame tu nombre: ")
print("Hola, ¿Cómo estás ", nombre, " ?")

#========================================#
# Los enteros son de precisión ilimitada #
#========================================#

y = 500000000000000000000000000000000000000000000000000
print(y)

#==============================================================#
# Se pueden delimitar números con guión bajo, pero no con coma #
#==============================================================#

y = 5_000_000
print(y)

#==================================================#
# La función int cambia strings y floats a enteros #
#==================================================#

numero = int(input("Dame tu edad: "))
type(numero)

#===================================================#
# La notación cientifica de flotantes utiliza e o E #
#                 1.2 x 10^{-9}                     #
#===================================================#

y = 1.2E-09
print(y)

#======================================================#
# La función float convierte strings y enteros a float #
#======================================================#

y = float("14.3")
print(y)

#====================================================#
# Los complejos se escriben con la raíz de menos uno #
#      j siempre con un número como prefijo          #
#             no acepta la j suelta                  #
#====================================================#

z = 1+1j

# Suma +
# Resta -
# Multiplicación *
# División /
# Módulo %
# Exponente **
# // Función piso
# Funciones para transformar números int() float() complex()
# Operaciones abs() round() pow()

print(round(3.14159,4))

#==========================#
# Strings de varias lineas #
#==========================#

parrafo="""
En el bosque de la china,
  La chinita se perdió
        """
print(parrafo)

#===============================================#
# La función len() obtiene el tamaño del string #
#===============================================#

n=len(parrafo)
print(n)

#===========================================================#
# Las letras en un string ocupan lugares como en un arreglo #
#  (también de atras para delante comienza en -1 el último) #
#===========================================================#

palabra = "Hola"
print(palabra[0])
print(palabra[-4])

