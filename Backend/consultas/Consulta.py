import sys
sys.path.append("./Backend/Conexion_base_datos")#para que el compilador de python encuntre los modulos
from Conexion import *

class Consulta:
    
    def agregarRegistro(consultaSql, valores):
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() #Ejecuta las consultas en la base de datos
            cursor.execute(consultaSql, valores)
            conexion.commit()
            print(cursor.rowcount, " registro se ha guardado el registro correctamente")
            conexion.close()
        except mysql.connector.errors.IntegrityError as error:
            print(error)
            return -1 #retorna -1 si hubo un error de integridad(llave primaria repetida)
        except mysql.connector.Error as error:
            print(f"hubo un error en el guardado de datos {error}") 
            
            
    #Retorna todos los registros de la vase de datos        
    def obtenerRegistros(consulta):
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() #Ejecuta las consultas en la base de datos
            cursor.execute(consulta)
            usuarios = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return usuarios
            
        except mysql.connector.Error as error:
            print(f"Error al mostrar los datos: {error}")
            
       
    #retorna un registro mediante su llave primaria     
    def obtenerRegistro(consultaSql, valores):        
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() #Ejecuta las consultas en la base de datos
            cursor.execute(consultaSql, valores)
            usuarios = cursor.fetchall()
            conexion.commit()
            conexion.close()
            return usuarios
            
        except mysql.connector.Error as error:
            print(f"Error al mostrar los datos: {error}")
            
    
    def modificarRegistro(consultaSql, valores):
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() #Ejecuta las consultas en la base de datos
            cursor.execute(consultaSql, valores)
            conexion.commit()
            print(cursor.rowcount, " registro se ha actualizado correctamente")
            conexion.close()
            
        except mysql.connector.Error as error:
            print(f"hubo un error actualizando los datos: {error}")
        
        
    def ejecutar(consultaSql):
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() # Ejecuta las consultas en la base de datos
            cursor.execute(consultaSql)
            conexion.commit()
        except mysql.connector.Error as error:
            print(f"hubo un error ejecutando la consulta: {error}")
        finally:
            cursor.close()
            conexion.close()


    def eliminarRegistro(consultaSql, valores):
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() #Ejecuta las consultas en la base de datos
            cursor.execute(consultaSql, valores)
            conexion.commit()
            print(cursor.rowcount, " registro se elimino satisfactoriamente")
            conexion.close()
            
        except mysql.connector.Error as error:
            print(f"hubo un error al eliminar el registro: {error}") 
