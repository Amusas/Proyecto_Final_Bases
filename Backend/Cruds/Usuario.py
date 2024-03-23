import sys
sys.path.append("./Backend/Conexion_base_datos")#para que el compilador de python encuntre los modulos
from Conexion import *

class Usuario:
    
    #Metodo para guardar los usuarios en la base de datos
    def ingresarUsuarios(codigo, nombreUsario, contrasenia, permisos):
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() #Ejecuta las consultas en la base de datos
            consultaSql = "INSERT INTO Proyecto.Usuarios VALUES(%s,%s,%s,%s);"# %s hace referencia a que son parametros
            valores = (codigo, nombreUsario, contrasenia, permisos) #los valores tienen que estar en una tupla
            cursor.execute(consultaSql, valores)
            conexion.commit()
            print(cursor.rowcount, " registro se ha guardado el registro correctamente")
            conexion.close()
            
        except mysql.connector.Error as error:
            print(f"hubo un error en el guardado de datos {error}")
        
        
    #esta funcion me devuelve todos los usuarios de la base de datos
    def obtenerUsuarios():
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() #Ejecuta las consultas en la base de datos
            cursor.execute("SELECT * FROM Proyecto.Usuarios;")
            usuarios = cursor.fetchall()
            conexion.commit()
            print(usuarios)
            conexion.close()
            return usuarios
            
        except mysql.connector.Error as error:
            print(f"Error al mostrar los datos: {error}")
            
    
    #Funcion para modificar un usuario
    def modificarUsuario(codigo, nombreUsario, contrasenia, permisos):
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() #Ejecuta las consultas en la base de datos
            consultaSql = ("UPDATE Proyecto.Usuarios "
               "SET Usuarios.nombre_usuario = %s, "
               "Usuarios.contrasenia = %s, "
               "Usuarios.nivel_permisos = %s "
               "WHERE codigo = %s;")#hace referencia a que son parametros
            valores = (nombreUsario, contrasenia, permisos, codigo) #los valores tienen que estar en una tupla
            cursor.execute(consultaSql, valores)
            conexion.commit()
            print(cursor.rowcount, " registro se ha actualizado correctamente")
            conexion.close()
            
        except mysql.connector.Error as error:
            print(f"hubo un error actualizando los datos: {error}")
        

    #Funcion para eliminar el usuario por su codigo
    def eliminarUsuario(codigo):
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() #Ejecuta las consultas en la base de datos
            consultaSql = "DELETE FROM Proyecto.Usuarios WHERE Usuarios.codigo=%s;"# %s hace referencia a que son parametros
            valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores
            cursor.execute(consultaSql, valores)
            conexion.commit()
            print(cursor.rowcount, " registro se elimino satisfactoriamente")
            conexion.close()
            
        except mysql.connector.Error as error:
            print(f"hubo un error al eliminar el usuario: {error}")       
        
