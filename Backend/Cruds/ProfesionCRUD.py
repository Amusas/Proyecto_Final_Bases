import sys
sys.path.append("./Backend/consultas")
from Consulta import *


#Metodo para guardar los Profesion en la base de datos
def ingresarProfesion(codigo, nombre):
    consultaSql = "INSERT INTO Proyecto.Profesiones VALUES(%s,%s);"# %s hace referencia a que son parametros
    valores = (codigo, nombre) #los valores tienen que estar en una tupla
    Consulta.agregarRegistro(consultaSql, valores)
        
        
#esta funcion me devuelve todos los Profesion de la base de datos 
def obtenerProfesiones():
    consultaSql = "SELECT * FROM Proyecto.Profesiones;"
    return Consulta.obtenerRegistros(consultaSql)
    
    
#Funcion para obtener un Profesion por su id
def obtenerProfesion(codigo):
    consultaSql = "SELECT * FROM Proyecto.Profesiones WHERE Profesiones.codigo=%s;"
    valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
    return Consulta.obtenerRegistro(consultaSql, valores)
            
    
#Funcion para modificar un Profesion
def modificarProfesion(codigo, nombre):
    consultaSql = ("UPDATE Proyecto.Profesiones "
            "SET Profesiones.nombre = %s "
            "WHERE codigo = %s;")#hace referencia a que son parametros
    valores = (nombre, codigo) #los valores tienen que estar en una tupla
    Consulta.modificarRegistro(consultaSql, valores)   


#Funcion para eliminar el Profesion por su codigo
def eliminarProfesion(codigo):
    consultaSql = "DELETE FROM Proyecto.Profesiones WHERE Profesiones.codigo=%s;"# %s hace referencia a que son parametros
    valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
    Consulta.eliminarRegistro(consultaSql, valores)
        