#----------------------------------#
# Porfirio Damián Escamilla Huerta #
#----------------------------------#

x = 1

n = 1000 

#-------------------#
# Función factorial #
#-------------------#

def factorial(k):
	r = 1
	for i in range(k):
		r *= (i+1) 
	return r

#---------------------#
# Función e^x con x=1 #
#---------------------#

def e_to_x_power(x,precision):
	e = 0
	for i in range(precision):
		e += (x**i)/(factorial(i))
	return e

print(e_to_x_power(x,n))


