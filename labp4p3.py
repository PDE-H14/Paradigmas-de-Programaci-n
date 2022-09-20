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
		print(f"Accediendo al constructor de la pc: {marca}")
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
		print(f"Esta es una computadora marca {self.marca} con almacenamiento de {self.capacidad} y memoria de {self.ram}")
	
	#------------#
	# Destructor #
	#------------#
	
	def __del__(self):
		print(f"Se eliminó la computadora: {self.marca} ")

compu1 = Computadora("DELL", 500, 8)

print(compu1)
compu1.imprimirInfoPC()
