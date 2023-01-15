#Con la primer prueba, este parece ser más rápido que el de hilos
from multiprocessing import Process
import os
import numpy as np
import time

def calc():
    for i in range(0,4000000):
        np.sqrt(i)

procesos = []

cpus = os.cpu_count()

print("Núcleos en tu cpu: ", cpus)

for i in range(cpus):
    print("registrando el proceso %d" % i)
    procesos.append(Process(target=calc))

start = time.time()

for thread in procesos:
    thread.start()

for thread in procesos:
    thread.join()

end = time.time()
print("Se tardó:",end-start)