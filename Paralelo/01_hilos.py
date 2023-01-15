from threading import Thread
import os
import numpy as np
import time

def calc():
    for i in range(0,4000000):
        np.sqrt(i)

threads = []

cpus = os.cpu_count()

print("Núcleos en tu cpu: ", cpus)

for i in range(cpus):
    print("registrando el hilo %d" % i)
    threads.append(Thread(target=calc))

start = time.time()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.time()
print("Se tardó:",end-start)