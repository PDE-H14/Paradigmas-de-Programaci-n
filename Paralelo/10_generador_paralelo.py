from multiprocessing import Process
import modulo_generador as mg
import os

N:int = 10

procesos = []
cpus = os.cpu_count()
print("Número de procesadores=", cpus)
for i in range(cpus):
    procesos.append(Process(target = mg.generador, args=(N,)))

# Comienza los procesos en paralelo
for proceso in procesos:
    proceso.start()

# Espera a que todos los procesos terminen
for proceso in procesos:
    proceso.join()