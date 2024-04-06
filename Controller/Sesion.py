

class Sesion:
    """
    Clase Sesión que implementa el patrón Singleton para almacenar la sesión actual del usuario.
    """

    __instancia = None

    def __init__(self, usuario, contrasena):
        """
        Constructor privado para evitar la creación de multiples instancias.
        """
        if Sesion.__instancia is not None:
            raise Exception("Ya existe una sesión activa.")
        self.__usuario = usuario
        self.__contrasena = contrasena
        Sesion.__instancia = self

    @staticmethod
    def obtener_instancia():
        """
        Método estático para obtener la instancia única de la clase Sesión.
        """
        if Sesion.__instancia is None:
            raise Exception("No se ha iniciado una sesión.")
        return Sesion.__instancia

    @property
    def usuario(self):
        """
        Propiedad para obtener el nombre de usuario de la sesión actual.
        """
        return self.__usuario

    @property
    def contrasena(self):
        """
        Propiedad para obtener la contraseña de la sesión actual.
        """
        return self.__contrasena

    def cerrar_sesion(self):
        """
        Método para cerrar la sesión actual.
        """
        Sesion.__instancia = None

