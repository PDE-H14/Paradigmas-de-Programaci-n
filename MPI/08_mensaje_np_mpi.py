#--------------------------------------------#
# El comando ejecuta el código en # procesos #
#--------------------------------------------#
#      mpiexec -n # python3 file_name.py     #
#       mpirun -n #python3 file_name.py      #
#--------------------------------------------#

from mpi4py import MPI
import numpy as np

# main
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    # Arreglo con un solo elemento
    zeroArray = np.zeros(1)

    #-------------------------------------------#
    # Se indica el tipo de datos explicitamente #
    #-------------------------------------------#

    #--------------------------#
    # Ejemplo ! usando enteros #
    #--------------------------#

    if rank == 1:
        data = np.empty(10,dtype='int')
        comm.Recv([data, MPI.INT], source=0, tag=77)
        print(data)

    if rank == 0:
        #-------------------------------#
        # Arreglo de enteros del 0 al 9 #
        #-------------------------------#
        data = np.arange(10, dtype='i')
        #------------------------------------------------#
        # Envío bloqueante especificando el tipo de dato #
        #------------------------------------------------#
        comm.Send([data, MPI.INT], dest=1, tag=77)

    #----------------------------------------------------------#
    #  También se puede sin decir el tipo de dato pero deben   #
    # coincidir el tipo de arreglos a los extremos del mensaje #
    #----------------------------------------------------------#

    #----------------------------#
    # Ejemplo 2 usando flotantes #
    #----------------------------#

    if rank == 1:
        data = np.arange(10, dtype=np.float64)
        comm.Recv([data, MPI.INT], source=0, tag=13)
        print(data)

    if rank == 0:
        data = np.arange(10, dtype=np.float64)
        comm.Send([data, MPI.INT], dest=1, tag=13)

