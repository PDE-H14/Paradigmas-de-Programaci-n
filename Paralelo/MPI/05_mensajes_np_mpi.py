#--------------------------------------------#
# El comando ejecuta el código en # procesos #
#--------------------------------------------#
#      mpiexec -n # python3 file_name.py     #
#       mpirun -n #python3 file_name.py      #
#--------------------------------------------#

from mpi4py import MPI
import numpy as np

class Mensaje:
    def __init__(self, rank):
        # Arreglo de numpy optimizdo
        self.x = np.array([float(x+rank) for x in range(10)])
        self.p = "Vengo del proceso" + str(rank)

# main
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    s = Mensaje(rank)
    src = rank-1 if rank!=0 else size-1
    dest = rank+1 if rank!=size-1 else 0

    # Arreglo para enviar
    m = s.x

    #------------------------------------#
    #  Isend Irecv son para comunicación #
    # no bloqueante de arreglos de numpy #
    #------------------------------------#
    comm.Isend(m, dest)

    #----------------------------------#
    #   Arreglo vacío para escribir    #
    # con dimensión 10 y tipo de datos #
    #     float64 (doble precisión)    #
    #----------------------------------#

    a = np.zeros(10,np.float64)
    req = comm.Irecv(a,src)
    req.wait()

    print("Yo soy el proceso", rank, "de", size, ", el resultado es", a)
