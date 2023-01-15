from mpi4py import MPI
import numpy as np 

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

n = 40
x = range(n)
m = int(np.ceil(float(n)/size))
x_chunk = list(x[rank*m:(rank+1)*m])
r_chunk = list(map(np.sqrt, x_chunk))

#-----------------------------------#
# Una sola lista de todos los datos #
#-----------------------------------#

r = comm.allreduce(r_chunk)

#--------------------------------#
# Una matriz con todos los datos #
#--------------------------------#

rr = comm.allgather(r_chunk)

#--------------------------------#
# Una matriz con todos los datos #
#--------------------------------#

rrr = comm.gather(r_chunk, root=1)


if rank == 0:
	print("r:",r,"\nrr:",rr,"\nrrr:",rrr)
if rank == 1:
    print(rank,"->", rrr)