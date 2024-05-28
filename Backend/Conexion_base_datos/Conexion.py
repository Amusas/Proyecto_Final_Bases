#comando para instalar la libreria: pip install mysql-connector-python
import mysql.connector

class Conexion:
    
    def conexionBaseDatos():
        try:
            #cambiar el usuario y la contraseña si es necesario
            conexion = mysql.connector.connect(user='root',
                                               host='127.0.0.1',#referencia a localHost 
                                               password='1234', 
                                               database='Proyecto', 
                                               port='3306')
            print("conexion establecida correctamente")
            return conexion
        except mysql.connector.Error as error:
            print(f"Error al conectarse a la base de datos {error}")
    