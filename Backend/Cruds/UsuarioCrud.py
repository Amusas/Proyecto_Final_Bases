import sys
sys.path.append("./Backend/consultas")
from Consulta import *

class UsuarioCrud:
    
    #Metodo para guardar los usuarios en la base de datos
    def ingresarUsuario(codigo, nombreUsario, contrasenia, permisos):
        consultaSql = "INSERT INTO Proyecto.Usuarios VALUES(%s,%s,%s,%s);"# %s hace referencia a que son parametros
        valores = (codigo, nombreUsario, contrasenia, permisos) #los valores tienen que estar en una tupla
        Consulta.agregarRegistro(consultaSql, valores)
        
        
    #esta funcion me devuelve todos los usuarios de la base de datos
    def obtenerUsuarios():
        consultaSql = "SELECT * FROM Proyecto.Usuarios;"
        return Consulta.obtenerRegistros(consultaSql)
    
    
    #Funcion para obtener un usuario por su id
    def obtenerUsuario(codigo):
        consultaSql = "SELECT * FROM Proyecto.Usuarios WHERE Usuarios.codigo=%s;"
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        return Consulta.obtenerRegistro(consultaSql, valores)
    
    #Funcion para obtener un usuario por su nombre de usuario
    def obtenerUsuarioxNombre(nombreUsuario):
        consultaSql = "SELECT * FROM Proyecto.Usuarios WHERE Usuarios.nombre_usuario=%s;"
        valores = (nombreUsuario,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        return Consulta.obtenerRegistro(consultaSql, valores)
            
    
    #Funcion para modificar un usuario
    def modificarUsuario(codigo, nombreUsario, contrasenia, permisos):
        consultaSql = ("UPDATE Proyecto.Usuarios "
               "SET Usuarios.nombre_usuario = %s, "
               "Usuarios.contrasenia = %s, "
               "Usuarios.nivel_permisos = %s "
               "WHERE codigo = %s;")#hace referencia a que son parametros
        valores = (nombreUsario, contrasenia, permisos, codigo) #los valores tienen que estar en una tupla
        Consulta.modificarRegistro(consultaSql, valores)   


    #Funcion para eliminar el usuario por su codigo
    def eliminarUsuario(codigo):
        consultaSql = "DELETE FROM Proyecto.Usuarios WHERE Usuarios.codigo=%s;"# %s hace referencia a que son parametros
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        Consulta.eliminarRegistro(consultaSql, valores)
        
        