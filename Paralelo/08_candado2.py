#---------------------------------------------------------------#
# Ejemplo de comunicación bloqueada a misma variable compartida #
#---------------------------------------------------------------#
from multiprocessing import Process, Value, Lock
import time

def sumale100conCandado(numeros, candado):
    for i in range(100):
        time.sleep(0.01)
        # Usando candado
        with candado:
            # Hacer la operación
            numeros.value += 1

def sumale100sinCandado(numeros):
    for i in range(100):
        time.sleep(0.01)
        # Hacer la operación
        numeros.value += 1

if __name__ == '__main__':
    # Candado para evitar que dos procesos de empalmen
    candado = Lock()
    # Número común a los procesos, 'i' de dobles,  comienza siendo 0
    numero_compartido = Value('i', 0)
    print("Al principio vale =", numero_compartido.value)
    p1 = Process(target=sumale100conCandado, args = (numero_compartido, candado))
    p2 = Process(target=sumale100conCandado, args = (numero_compartido, candado))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Al final vale =", numero_compartido.value)
    print("Operación +100 con candado. Al principio vale =", numero_compartido.value)
    p1 = Process(target=sumale100sinCandado, args = (numero_compartido, ))
    p2 = Process(target=sumale100sinCandado, args = (numero_compartido, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Operación +100 sin candado. Al final vale =", numero_compartido.value)