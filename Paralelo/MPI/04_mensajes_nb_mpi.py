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
		self.x = [i for i in range(rank*10)]
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

	src = rank-1 if rank!=0 else size-1

	#-------------------------------------------------------------#
	# Mandalo al siguiente y si eres el último mandalo al primero #
	#-------------------------------------------------------------#

	dst = rank+1 if rank!= size-1 else 0

	#---------------------#
	# Envío no bloqueante #
	#---------------------#

	comm.isend(s, dest = dst)

	#----------------------------------#
	# Recibir no bloqueante con espera # 
	#      req: request (petición)     #
	#----------------------------------#

	req = comm.irecv(source = src)
	a = req.wait()

	print("Proceso", rank, "de", size, "el resultado es:", len(a.x), ",", a.p)
