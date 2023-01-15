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

    if rank == 1:
        randNum = zeroArray = np.random.random_sample(1)
        print("Proceso", rank, "generó", randNum[0])
        comm.Isend(randNum, dest=0)
        req = comm.Irecv(randNum, source=0)
        req.Wait()
        print("Proceso", rank, "recibió el número", randNum[0])

    if rank == 0:
        randNum = zeroArray = np.random.random_sample(1)
        print("Proceso", rank, "generó", randNum[0]) #Este randNum lo genera el uno
        comm.Isend(randNum, dest=1)
        req = comm.Irecv(randNum, source=1) # Aquí guarda el ranNum que envia el cero
        req.Wait()
        print("Proceso", rank, "recibió el número", randNum[0])
