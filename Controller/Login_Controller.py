import sys
from datetime import datetime
sys.path.append("./Backend/Cruds")
import UsuarioCRUD
import BitacoraSesionesCRUD as bs
from Sesion import Sesion


"""
    Funcion que valida que los datos no esten nulos
    retorna un false si algun campo es nulo
    retorna un true si no estan nulos
"""
    
def validarDatos(nombre_usuario, contrasenia):
    if nombre_usuario == "" or contrasenia == "":
        return False
    return True


"""
    Obtiene el usuario en la base de datos
"""
def obtenerUsuario(nombreUsuario):
    usuario = {}
    usuarioBaseDatos = UsuarioCRUD.obtenerUsuarioxNombre(nombreUsuario)   
    for atributo in usuarioBaseDatos:
        usuario = {
            "id": atributo[0],
            "nombreUsuario": atributo[1],
            "contrasenia": atributo[2],
            "permiso": atributo[3]
        }
    return usuario
            
"""
    funcion para inicio de sesion
    retorna numeros que hacen refernecia a
    -1 = algun campo esta nulo
    0 = contraseña incorrecta
    1 = inicio de sesion correcto
"""
    
def iniciarSesion(nombre_usuario, contrasenia):
    if validarDatos(nombre_usuario, contrasenia) == False:
        return -1
    usuario = obtenerUsuario(nombre_usuario)
    if usuario == {}:
        return 2
    if contrasenia != usuario["contrasenia"]:
        print(f"Warning: el usuario {nombre_usuario} ingreso mal su contraseña")
        return 0
    #se guarda la sesion hasta salirse de la app
    Sesion(usuario["id"], usuario["nombreUsuario"], usuario["permiso"])
    bs.ingresarBitacora(usuario["id"], datetime.now())
    return 1


def cerrarSesion():
    sesion = Sesion.obtener_instancia()
    sesion.cerrar_sesion()
    bs.fechaSalidaBitacora(datetime.now(), sesion.codigo)
    print("Cerrando sesion.....")
    
    
    
    
        
            

    



