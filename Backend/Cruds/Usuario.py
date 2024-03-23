from Conexion import *

class Usuario:
    
    #Metodo para guardar los usuarios en la base de datos
    def ingresarUsuarios(codigo, nombreUsario, contrasenia, permisos):
        
        try:
            conexion = Conexion.conexionBaseDatos()
            cursor = conexion.cursor() #Ejecuta las consultas en la base de datos
            consultaSql = "INSERT INTO Proyecto.Usuarios VALUES(%s,%s,%s,%s)"# %s hace referencia a que son parametros
            valores = (codigo, nombreUsario, contrasenia, permisos) #los valores tienen que estar en una tupla
            cursor.execute(consultaSql, valores)
            conexion.commit()
            print(cursor.rowcount, "se ha guardado el registro correctamente")
            conexion.close()
            
        except mysql.connector.Error as error:
            print(f"hubo un error en el guardado de datos {error}")
        
    ingresarUsuarios('02', 'Nathaly', '123456789', 'Lider')