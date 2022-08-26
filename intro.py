#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
# Porfirio Damián Escamilla Huerta #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#=====================#
# Operaciones básicas #
#=====================#

print(2+3)
print(2*3)
print(2/3)
print(2**10)
print(2**0.5) #raíz cuadrada
print(10%2)
print(10%0.1) #esclusivo de python

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

