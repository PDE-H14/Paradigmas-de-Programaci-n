from aplicacion.banco.cliente_bancario import ClienteBancario

#--------------------------------------------#
#  try: intenta ejecutar las instrucciones   #
# except: atrapar el error en una variable e #
#     e se puede convertir a string          #
#--------------------------------------------#

#------------------------------------------#
# Error por sacar más dinero del que tiene #
#------------------------------------------#

try:
	cliente = ClienteBancario("Jaime Andrade", "Hernandez Sánchez", 28, 0.0)
	cliente.guardarDinero(300)
	print(Cliente.imprimirInfo())
	print(Cliente)
	cliente.retirarDinero(400)
	print(Cliente.imprimirInfo())
	print(Cliente)

