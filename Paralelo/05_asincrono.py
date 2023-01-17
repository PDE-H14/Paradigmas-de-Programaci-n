import multiprocessing as mp
import numpy as np 
import time

def my_function(i, param1, param2, param3):
	 # calcula un polinomio
	 result = param1**3+param2**2+param3
	 # se hace tonto 2 segundos 
	 time.sleep(2)
	 return (i, result)

def get_result(result):
	# Se inscriben en la lista global
	# (mal estilo de programación)
	global results
	results.append(result)

#--------------------#
# Programa principal #
#--------------------#

if __name__ == '__main__':
	#--------------------------------#
	# Matriz 10x3 de números al azar #
	#--------------------------------#
	params = np.random.random((10,3))*100
	results = []
	start = time.time()

	#Un grupo de procesos (Pool)
	pool = mp.Pool(mp.cpu_count())

	# loop  de primera dimensión del arreglo
	for i in range(0, params.shape[0]):
		#Correr asincrónicamente my_function con argumentos y cuando termine correr get_result
		pool.apply_async(my_function, args=(i, params[i,0], params[i,1], params[i,2]), callback = get_result)

	# Cerrar el grupo 
	pool.close()
	# Esperar que termine el grupo
	pool.join()

	print("Tiempo en paralelo = ", time.time()-start)
	print(results)
