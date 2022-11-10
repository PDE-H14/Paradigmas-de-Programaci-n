#-----------------------#
# Clase ClienteBancario #
#-----------------------#
class ClienteBancario:
    __nombres: str = None
    __apellidos: str = None
    __edad: int = 0
    __balanceDeCuenta: float = 0.0

    def __init__(self, nombres:str, apellidos:str, edad:int = 0, balanceDeCuenta:float = 0.0) -> None:
        self.__validarEdad(edad)
        self.__validarCantidad(balanceDeCuenta)
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__edad = edad
        self.__balanceDeCuenta = balanceDeCuenta

    def getNombreCompleto(self) -> str:
        return self.__nombres+" "+self.__apellidos

    def __mandarEmail(self, titulo:str, texto:str) -> None:
        print("Mandar email: "+ titulo+" con texto: "+texto)

    def __enviarBalanceAlBanco(self, cantidd:float)->None:
        print("Enviando cantidad: "+str(cantidad)+" al banco...")

    #--------------------------------------------#
    # Método privado con dos guiones bajos       #
    # Si la edad es menor que 18 genera un error #
    #--------------------------------------------#

    def __validarEdad(self, edad:int)->None:
        if edad < 18:
            raise Exception("Es menor de edad.")

    def __str__(self)->str:
        return "Nombre: "+self.getNombreCompleto()+", Edad: "+str(self.__edad)+" Balance: "+str(self.__balanceDeCuenta)