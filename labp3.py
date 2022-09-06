#----------------------------------#
# Porfirio Damián Escamilla Huerta #
#----------------------------------#

#---------------#
# Condicionales #
#---------------#

precio = 50

#-------------
# Si esto...
#-------------

if precio < 50:
    print("El precio es menor que 50")

#--------------------------
# Si no... si esto otro...
#--------------------------

elif precio > 50:
    print("El precio es mayor a 50")

#---------------------------
# Si nada de lo anterior...
#---------------------------

else:
    print("El precio es 50")

precio = 50
cantidad = 5
total = precio * cantidad

#------------------------#
# Condicionales anidados #
#------------------------#

if total > 100:
    if total > 500:
        print("Total es mayor que 500")
    else:
        if total < 500 and total > 400:
            print("Total es menor que 500 y mayor que 400")
        elif total < 500 and total > 300:
            print ("Total es mayor que 300 y menor que 500")
        else:
            print("Total entre 100 y 300")

#-------------------------------#
# Condicional de igualdad es == #
#-------------------------------#

elif total == 100:
    print("Total es 100")
else:
    print("Total menor que 100")

#----------------------------------------------#
# Contador mientras la condición sea verdadera #
#----------------------------------------------#

num = 0

while num < 5:
    num += 1 # Es lo mismo que num = num + 1
    print("num =", num)

num = 0

while num < 5:
    num = num + 1
    print("num =", num)
    if num == 3:
        break

num = 0

while num < 5:
    num += 1
    if num > 3:
        continue # Evita lo que sigue, continuar con las iteraciones
    print("num =", num)

#--------------------#
# Bucle sobre listas #
#--------------------#

nums = [10, 20, 30, 40, 50]
for i in nums:
    print(i)

#-----------------------#
# Bucle sobre un string #
#-----------------------#

for char in "Hello":
    print(char)

#---------------------------#
# Bucle sobe un diccionario #
#     items = elementos     #
#---------------------------#

numNames = {1:"One", 2:"Two", 3:"Three"}
for pair in numNames.items():
    print(pair)

#-------------------------#
# Bucle sobre diccionario #
#       key = llave       #
#      value = valor      #
#-------------------------#

for k,v in numNames.items():
    print("key =", k, ", value =",v)
	
#----------------------------------#
# Porfirio Damián Escamilla Huerta #
#----------------------------------#

#-----------------#
# Primera función #
#-----------------#

def saludo():
	#------------------------------------#
	# Documentación rápida de la función #
	#------------------------------------#
	"""Esta función saluda"""
	print("¡Quiúboles, ¿cómo estás?!")
	
#-----------------------#
# Llamado de la función #
#-----------------------#
saludo()

#------------------------------#
# Se ejecuta pero no se asigna #
#------------------------------#
salida = saludo()

#------------------#
# Esto no funciona #
#------------------#

print(salida)

#-----------------------#
# Mostrar documentación #
#-----------------------#

#help(saludo)

#-----------------------#
# Función con argumento #
#-----------------------#

def salu2(numbre):
	"""Esta función te saluda por tu nombre"""
	print("¡Qué onda ese", nombre,"!")

salu2("Julián")
salu2("Ángel")

#-----------------------------------------#
#      Ahorrar trabajo del intérprete     #
# nombre:str la variable nombre es un str #
#-----------------------------------------#

def saludos(nombre:str):
	"""Esta función te saluda por tu nombre estrictamente"""
	print("¡Qué onda ese", nombre,"!")
saludos("Julián")
a = 123
print(type(a)) 

#------------------------------#
# Función con mchos argumentos #
#------------------------------#

def saludos_multiples(nombre1, nombre2, nombre3):
	"""Esta función te saluda a tres personas al mismo tiempo"""
	print("¡Hola", nombre1, ",", nombre2, "y", nombre3, "!")
saludos_multiples("Hugo","Paco","Luis")

#--------------------------------------------#
# Función con cualquier número de argumentos #
#--------------------------------------------#

def muchos_saludos(*nombres):
	"""Está función saluda a todos los que quieras"""
	i = 0
	#---------------------------------#
	# end= es para ponerlo de corrido #
	#---------------------------------#
	print("Hola ", end="")
	while len(nombres) > i:
	