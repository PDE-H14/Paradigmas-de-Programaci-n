from ampi4py import MPI
import numpy as np 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 10

#------------------------------------------#
#      Arreglo de ceros de tamaño n        #
# sumando con un escalar (en cada entrada) #
#------------------------------------------#

sendarray = np.zeros(n, dtype='i')+rank

recvarray = None

if rank == 0:
	#----------------------------------------#
	#   Matriz vacía de tamaño procesos * n  #
	# dtype es el tipo de dato (i) es entero #
	#----------------------------------------#
	recvarray = np.empty([size, n], dtype='i')
