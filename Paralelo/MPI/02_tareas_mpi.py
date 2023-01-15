#-------------------------------------#
# Para ejecutar/correr en  # procesos #
#-------------------------------------#
#  mpiexec -n # python3 file_name.py  #
#  mpirun -n # python3 file_name.py   #
#-------------------------------------#

from mpi4py import MPI

#-----------------------------#
# Crear un objeto comunicador #
#-----------------------------#

comm = MPI.COMM_WORLD

#--------------------------#
# Número total de procesos #
#--------------------------#

size = comm.Get_size()

#--------------------------------------------------#
# Número identificador de este proceso (quien soy) #
#--------------------------------------------------#

rank = comm.Get_rank()

#----------------------------------#
# Si soy el proceso cero hago esto #
#----------------------------------#
if rank == 0:
	print("Yo soy el proceso", rank) # 0
#------------------------------#
# Si soy el uno  hago esto ... #
#------------------------------#
elif rank == 1:
	print("Yo soy el proceso", rank) # 1
#------------------#
# En otro caso ... #
#------------------#
else:
	print("No soy ninguno de los dos primeros porcesos") # 2,3

print("Reportandose el proceso", rank, "de", size)
