from numba import jit
import numpy as np
import time

@jit(nopython = True)
def rapido(a):
	t = 0.0
	for i in range(a.shape[0]):
		t += np.tanh(a[i,i])
	return a+t

def lento(a):
	t = 0.0
	# Para cada región
	for i in range(a.shape[0]):
		t += np.tanh(a[i,i])
	return a + t

x = np.arange(10000).reshape(100,100)

# La primera llamada incluye el tiempo de compilación

start = time.time()
rapido(x)
end  = time.time()
print("Tiempo incluyendo compilación = %s" % (end - start))

# La segunda llamada es para obtener el tiempo de ejecución

start = time.time()
rapido(x)
end= time.time()
print("Tiempo de ejecución usando numba = %s" % (end - start))

# Función sin optimización
start = time.time()
lento(x)
end = time.time()
print("Tiempo de ejecución en python puro = %s" % (end - start))