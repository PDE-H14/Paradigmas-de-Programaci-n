#----------------------------------#
# Porfirio Damián Escamilla Huerta #
#----------------------------------#

#-------------------#
# Clase computadora #
#-------------------#

class Computadora:
	marca: str = None
	capacidad: int = 0
	ram: int = 0

	#-------------#
	# Constructor #
	#-------------#

	def __init__(self, marca: str, capacidad: int, ram: int):
		print(f"$ Accediendo al constructor de la pc: {marca}")
		self.marca = marca
		self.capacidad = capacidad 
		self.ram = ram
	
	#----------------------#
	# Impresión del objeto #
	#----------------------#

	def __str__(self):
		computadora: str = f"Marca: {self.marca}\nCapacidad: {self.capacidad}GB\nRAM: {self.ram}GB"
		return computadora
	
	def imprimirInfoPC(self):
		print(f"$ Esta es una computadora marca {self.marca} con almacenamiento de {self.capacidad} y memoria de {self.ram}")
	
	#------------#
	# Destructor #
	#------------#
	
	def __del__(self):
		print(f"$ Se eliminó la computadora: {self.marca} ")


#----------------#
# Objeto Persona #
#----------------#

class Persona:
	nombres: str = None
	apellidos: str = None
	edad: int = 0
	dirección: str = None
	computadora: Computadora = None

	#------------------------#
	# Constructor de Persona #
	#------------------------#

	def __init__(self, nombres:str, apellidos:str, edad:int, dirección:str, marca:str, capacidad:int, ram:int):
		self.nombres = nombres
		self.apellidos = apellidos
		self.edad = edad
		self.dirección = dirección
		self.computadora = Computadora(marca, capacidad, ram)
		print(f"$ Accedimos al consructor de la persona: {nombres}, {apellidos}, {edad}, {dirección}")

	def __str__(self):
		computadora: str = f"Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años de edad, vivo en {self.dirección}\n{self.computadora}"
		return computadora
	
	def imprimirInfoPersona(self) -> None:
		print(f"Mi nombre es {self.nombres} {self.apellidos}, tengo {self.edad} años de edad, vivo en {self.dirección}\n{self.computadora}")

	def __del__(self):
		print(f"$ Se eliminó el objeto: {self.nombres} {self.apellidos}")

#-------------------------#
# Función 1 es l programa #
#-------------------------#

def función1():
	persona = Persona("Manolo", "Estrada", 29, "Ecatepec", "hp", 500, 4)
	print(persona)
	persona.imprimirInfoPersona()
	persona2 = Persona("Mololongo", "Jamón", 34, "París", "Mac", 1000, 6)
	print(persona2)
	persona2.imprimirInfoPersona()

#--------------------#
# Llamar a función 1 #
#--------------------#

función1()