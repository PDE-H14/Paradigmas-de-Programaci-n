#-------------------------------------#
# Para ejecutar/correr en  # procesos #
#-------------------------------------#
#  mpiexec -n # python3 file_name.py  #
#  mpirun -n # python3 file_name.py   #
#-------------------------------------#

from mpi4py import MPI

class Mensaje:
	def __init__(self, rank):
		# iterador
		self.x = range(rank*10)
		# String
		self.p = "Vengo del proceso " + str(rank)


#--------------------#
# Programa principal #
# -------------------#
if __name__ == "__main__":

	#-----------------------------#
	# Crear un objeto comunicador #
	#-----------------------------#

	comm = MPI.COMM_WORLD

	#--------------------------#
	# Número total de procesos #
	#--------------------------#
	size = comm.Get_size()

	#--------------------------------------#
	# Número identificador de este proceso #
	#--------------------------------------#

	rank  = comm.Get_rank()

	s = Mensaje(rank)

	#-------------------------------------------------#
	# Que te mande el anterior y si es cero al último #
	#-------------------------------------------------#

	fuente = rank-1 if rank!=0 else size-1

	#-------------------------------------------------------------#
	# Mandalo al siguiente y si eres el último mandalo al primero #
	#-------------------------------------------------------------#

	destino = rank+1 if rank!= size-1 else 0

	#----------------------------------------------------------#
	# send y recv son operaciones bloqueadas y generan que el  # 
	# código se atore esperando que alguien reciba un mensaje  #
	# esto se resuelve enviando con los pares y recibiendo con #
	#                    con los impares.                      #
	#----------------------------------------------------------#

	# Si soy par
	if rank%2 == 0:
		# Enviar mensaje al destino
		comm.send(s, dest = destino)
		# Recibir de source y lo pone en m
		m = comm.recv(source = fuente)
	else:
		# Recibir primero y mandar mensaje después
		m = comm.recv(source = fuente)
		comm.send(s, dest =  destino)
	print("Proceso", rank, "de", size, "el resultado es:", len(m.x), ",", m.p)
