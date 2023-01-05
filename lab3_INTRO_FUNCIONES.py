
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

def salu2(nombre):
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
	print("¡Qué onda ese", nombre,"!", "Type", type(nombre))
saludos("Julián")
a = 123
print(type(a)) 
saludos(a)

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
	    #Último nombre
            if (i == len(nombres)-1):
                print(nombres[i])
            else:
                # Cualquier otro nombre
                print(nombres[i], end= ", ")
            i += 1

muchos_saludos("Bosco", "Angel", "David", "Tamara", "Mili", "Edwin", "Lev", "Luis", "Abigail")

def greet(firstName, lastName):
    print("Hello", firstName, lastName)

#----------------------------------------------#
# Llamar la función con argumentos en desorden #
#----------------------------------------------#

greet(lastName = "Jobs", firstName = "Steve") # Se pueden especificar las variables en desorden

#-----------------------------------#
# Función con argumentos escondidos #
#-----------------------------------#

def greet(**person):

    #-----------------------------------------------------#
    # Persona tiene caracteristicas: firstName y lastName #
    #-----------------------------------------------------#

    print("Hello", person["firstName"], person["lastName"])

greet(firstName = "Manolo", lastName = "conchas")
greet(lastName = "Conchas", firstName = "Manolo")
greet(firstName = "Manolo", lastName = "Conchas", age = 55) # Se pueden pasar mas parametros de los necesarios

#---------------------------------#
# Función con valores por defecto #
#---------------------------------#

def greet(name = "Guest"):
    print("Hello, ", name)

greet() # Utiliza el valor por defecto
greet("Steve")

#-----------------------#
# Función con resultado #
#-----------------------#

def suma(a,b):
    return a+b

print(suma(2,3))

#---------------------------------------------------------------#
# Programación funcional. Se pueden usar funciones de funciones #
#---------------------------------------------------------------#

total = suma(5, suma(10,20))
print(total)

#--------------------------------------------------#
#                  Cálculo llamado                 #
# nombre de la función = lambda vaiables : función #
#--------------------------------------------------#

x_to_2 = lambda x : x * x
a1 = x_to_2(5)
print(a1)

#----------------------------#
# Lambda de varias variables #
#----------------------------#

suma = lambda x1, x2, x3: x1 + x2 + x3
print(suma(1,2,3))

sumas = lambda *x: x[0]+x[1]+x[2]+x[3]
print(sumas(1,2,3,4))

#-----------------------------------------#
#        Uso de una función anónima       #
# El argumento va afuera entre paréntesis #
#-----------------------------------------#

print((lambda x : x * x)(6)) # Función anónima

#-----------------------------#
# Función con variable global #
#      ¡EVITE EL EXCESO!      #
#-----------------------------#

name = "Steve"
def greet():
    global name # Para utilizar una variable global (que viene del bloque)
    name = "Bill"
    print("Hello ", name)

greet()
