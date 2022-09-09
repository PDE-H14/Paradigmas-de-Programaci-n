#----------------------------------#
# Porfirio Damián Escamilla Huerta #
#----------------------------------#

#--------------------------------------#
# PROGRAMACIÓN ORIENTADA A OBJETOS POO #
#--------------------------------------#

#--------------------------------#
# Una clase para un objeto vacío #
# no está tan vacío, necesita la #
#      palabra pass = pasar      #
#--------------------------------#

class ObjetoVacio:
    pass

#-------------------------#
# Nada es un objeto vacío #
#-------------------------#

nada = ObjetoVacio()
print(type(nada))

#-----------------#
# La clase llanta #
#-----------------#

class Llanta:

	#----------------------------------------#
	# La variable cuenta es de toda la clase #
	#----------------------------------------#

	cuenta = 0

	#-----------------------------------#
	# Función constructora de identidad #
	# __init__ es una función reservada #
	# comienza con uno mismo: self pero #
	# puede ser otro nombre (mi) pará-  #
	#   metros de entrada = default.    #
	#-----------------------------------#
	
	def __init__(mi, radio=50, ancho=30, presion=1.5):
		# variable de la estructura completa llanta
		Llanta.cuenta += 1
		# variables exclusivas de cada objeto
		mi.radio = radio
		mi.ancho = ancho
		mi.presion = presion

#------------------------#
# Objetos (instanciados) #
#------------------------#

llanta1 = Llanta(50,30,1.5)
llanta2 = Llanta(presion=1.2)
llanta3 = Llanta()
llanta4 = Llanta(40,30,1.6)

#-------------------------------------#
# Objetos que contienen otros objetos #
#-------------------------------------#

class Coche:
	def __init__(mi,ll1,ll2,ll3,ll4):
		mi.llanta1 = ll1
		mi.llanta2 = ll2
		mi.llanta3 = ll3
		mi.llanta4 = ll4

miCoche = Coche(llanta1, llanta2, llanta3, llanta4)

print("OBJETOS: LLANTAS Y COCHES")
print("Total de llantas:", Llanta.cuenta) # Variable global de la clase
print("Presión de la llanta 4:", llanta4.presion) # Presión de la llanta 4
print("Radio de la llanta 4:", miCoche.llanta4.radio)
print("Radio de la llanta 3:", llanta3.radio)
print("Presión de la llanta 1 de mi coche:", miCoche.llanta1.presion)

#-----------------#
# Encapsulamiento #
#-----------------#

#---------------------------------------------------------------------#
# Uso de la función de python property para poner y obtener atributos #
#---------------------------------------------------------------------#

class Estudiante:
	def __init__(mi):
		mi.__nombre = ""
	def ponerme_nombre(mi, nombre):
		print("Se llamó a la función 'ponerme_nombre'")
		mi.__nombre = nombre
	def obtener_nombre(mi):
		print("Se llamó a la función 'obtener_nombre'")
		return mi.__nombre
	nombre = property(obtener_nombre, ponerme_nombre)

#---------------------------------------#
# Crear un objeto estudiante sin nombre #
#---------------------------------------#

estudiante = Estudiante()

#----------------------------------------------------------------------#
# Ponerle nombre usando la propiedad nombre y el método ponerme_nombre #
#           (sin tener que llamar explícitamente la función)           #
#----------------------------------------------------------------------#

estudiante.nombre = "Diego"

#-------------------------------------------------------------#
#     Obtener el nombre con el método obtener_nombre.         #
# Nombre es una variable encapsulada (no visible desde fuera) # 
#  (sin llamar explícitamente a la función obtener_nombre)    #
#-------------------------------------------------------------#

print(estudiante.nombre)

# Esto no funciona

#print(estudiante.__nombre)

#--------------------#
# Herencia de clases #
#--------------------#

class Cuadrilatero:
	def __init__(mi, a, b, c, d):
		mi.lado1 = a
		mi.lado2 = b
		mi.lado3 = c
		mi.lado4 = d
	def perimetro(mi):
		p = mi.lado1 + mi.lado2 + mi.lado3 + mi.lado4
		print("Perímetro =", p)
		return p

#------------------------------------#
#         Su hijo rectángulo         #
# Rectángulo es hijo de Cuadrilátero #
#      Rectángulo(Cuadrilátero)      #
#------------------------------------#

class Rectangulo(Cuadrilatero):
	def __init__(self, a, b):
		#-------------------------#
		# Constructor de su madre #
		#-------------------------#
		super().__init__(a,b,a,b)

#--------------------#
# Su nieto Cuadrado  #
# Hijo de Rectángulo #
#--------------------#
class Cuadrado(Rectangulo):
	def __init__(self,a):
		super().__init__(a,a)

	def area(self):
		area = self.lado1**2
		return area

	#def perimetro(self):
	#	p = 4.0*self.lado1
	#	print("Perímetro =", p)
	#	return p

#-------------------#
# Crear un cuadrado #
#-------------------#

cuadrado1 = Cuadrado(5)

#------------------------------------------------------#
# Llamar al método perímetro de su abuelo Cuadrilátero #
#------------------------------------------------------#

perimetro1 = cuadrado1.perimetro()

#--------------------------------#
# Llamar a su propio método área #
#--------------------------------#

area1 = cuadrado1.area()

print("Perímetro =", perimetro1)
print("Área =", area1)

#-----------------------------------------------------------------#
# Sobre-escribir un método de su  madre o abuela o tatarabuela... #
#          Es volver a definir una función ya existente           #
#-----------------------------------------------------------------#
