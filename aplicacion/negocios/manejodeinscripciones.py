from aplicacion.repositorio.repositoriodeusuarios import RepositorioDeUsuarios
from aplicacion.modelos.usuario import Usuario

#----------------------#
#  Clase storemanager  #
# ¡NO TIENE VARIABLES! #
#----------------------#

class ManejoDeInscripciones:
    #----------------------------------------------------------------#
    #                     Decorador staticmethod                     #
    #        El objeto sólo tiene la función inscribirUsuario        #
    #        ENVUELVE LA FUNCIÓN SIN LLAMAR VARIABLES LOCALES        #
    # el objeto ManejoDeInscripciones es la interface intercambiable #
    #----------------------------------------------------------------#
    @staticmethod
    def inscribirUsuario(usuario:Usuario, repositoriodeusuarios: RepositorioDeUsuarios) -> None:
        print("----------> Guardando usuario...\n")
        repositoriodeusuarios.abrir()
        repositoriodeusuarios.guardar(usuario)
        repositoriodeusuarios.cerrar()