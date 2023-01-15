#-----------------------#
#   Broadcast con MPI   #
# distribución de datos #
#-----------------------#

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

#-----------------------------------------#
# El proceso 0 tiene datos y los otros no #
#-----------------------------------------#

if rank  == 0:
	data = {'key1': [7,2.72,2+3],
'key2': ('abc', 'xyz')}
elif rank == 1:
	data = {'llave': 'no llave'}
else:
	data = None

#----------------------------------------------------#
# Enviar diccionario a todos los procesos desde root #
#----------------------------------------------------#

data = comm.bcast(data, root=1) # La raíz es el que manda la información al resto.
print(data)
