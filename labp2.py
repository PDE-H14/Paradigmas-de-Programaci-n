#----------------------------------#
# Porfirio Damián Escamilla Huerta #
#----------------------------------#

#---------------------#
# Conjuntos en python #
#---------------------#

even_nums = {2, 4, 6, 8, 10} # Conjunto de números pares
print("Conjunto de números pares:", even_nums)

#El bool no es parte del conjunto
emp = {1, 'Steve', 10.5, True} # Conjunto de diferentes objetos
print("Conjunto de diferentes objetos:", emp)

nums = {1, 2, 2, 3, 4, 4, 5, 5}
print("Conjunto de números:", nums)

#--------------------------------#
# Convertir secuencia a conjunto #
#      No lo genera en ordem     #
#--------------------------------#

s = set('Hello')
print("Palabra 'Hello' como conjunto:",s)
s = set((1, 2, 3, 4, 5)) # Tupla a conjunto
print("Tupla a conjunto:",s)

#-----------------------------------------------#
# De diccionario a conjunto: conjunto de llaves #
#-----------------------------------------------#

d = {1:"One", 2:"Two"}
s = set(d)
print("Diccionario a conjunto", s)

s.add(100)
print("100 añadido al conjunto",s)

s.update(nums)
print("conjunto S actualizado con NUMS:",s)

s.remove(100)
print("Remover elemento 100:",s)

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

su = s1|s2 # Unión
print("S_1 unión S_2:", su)

si = s1&s2 # Intersecciòn
print("S_1 intersección S_2:", si)

sr = s1-s2 # Diferencia de conjuntos
print("Diferencia de conjuntos (S_1\\S_2):",sr)

sp = s2-s1
print("Diferencia de conjuntos (S_2\\S_1):",sp)

ss = s1^s2 # Diferencia simétrica
print("diferencia simétrica:", ss)

#---------------------#
# Uso de diccionarios #
#---------------------#

capitals = {"USA":"Washington D.C.", "France":"París", "India":"New Delhi"}
print(capitals)

#--------------#
# llave: valor #
#--------------#

# Diccionario vacío
d = {}

# Llave entera, valor string
numNames = {1:"One", 2:"Two", 3:"Three"}

# Llave real, valor string
decNames = {1.5:"One and half", 2.5:"Two and half", 3.5:"Three and half"}

# Llave tupla, valor string
items = {("Parker", "Reynolds", "Camlin"):"pen", ("LG","Whirpool","Samsung"):"refrigerator"}

# Llave String valor entero
romanNums = {'I':1, 'II':2, 'III':3, 'IV':4, 'V':5}

print("Números romanos:", romanNums)
print("Número 'I' romano:", romanNums['I'])

print("Obtener la capital de 'India':",capitals.get("India"))
print("Obtener la capital de 'india':",capitals.get("india"))

# Reportar llave y valor
for k in capitals:
    print("Key=", k + ", Value=",capitals[k])

# Nuevo dato para el diccionario
capitals["Mexico"] = "CDMX"
print(capitals)

# Borrar dato del diccionario
del capitals["Mexico"]
print(capitals)

# Borrar todo el diccionario
del capitals

# Reportar llaves
print(romanNums.keys())

# Reportar valores
print(romanNums.values())

# Juicio de llave (está o no está la llave en el diccionario)
print ("I" in romanNums)
print("X" in romanNums)
print("XX" not in romanNums)

#----------------------------------#
# Porfirio Damián Escamilla Huerta #
#----------------------------------#

#---------------------------------------------#
#                    Listas                   #
# Las listas pueden ser de objetos diferentes #
#---------------------------------------------#

miPrimerLista =[] # Lista vacía
print("Lista vacía",miPrimerLista)

#------------------#
# Llenado de lista #
#------------------#

miPrimerLista = [1,"Javier",1.34,"Bosco","Angel","Abigail",True]
print("Lista definida:",miPrimerLista)

#------------------------------------------#
#           list: Hacer una lista          # 
# range(i, j): Secuencia desde i hasta j-1 #
#------------------------------------------#

nums = list(range(1,61))
print("Lista de un rango de números",nums)
for i in nums:
    print(i)

#--------------------------------------#
# Incluir nuevos elementos en la lista #
#--------------------------------------#

nums.append(61)
nums.append(62)
nums.append(61)
print("Lista con números agregados:",nums)

#------------------------------#
# Quitar elementos de la lista #
#------------------------------#

nums.remove(61)
print("Lista de números quitando el valor 61", nums) # Elimina la primer coincidencia

#------------------------------#
# Quitar elemento con índice i #
#------------------------------#

i = 61
del nums[i]
print("Lista de números sin el elemnto con pocisión 61",nums)

#-----------------#
# Borrar la lista #
#-----------------#

del nums

#--------------#
# Sumar listas #
#--------------#

L1 = [1, 2, 3]
L2 = [4, 5, 6]
print("Suma de listas:",L1+L2)

#----------------#
# Llenado a mano #
#----------------#

potencial = []

for i in range(0,10000):
    potencial.append(float(i))
print(potencial[100])

#--------------------------------#
# Generar una tupla con la lista #
#--------------------------------#

potencial = tuple(potencial)
print(potencial[100])
