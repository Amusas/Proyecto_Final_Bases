import sys
sys.path.append("./Backend/consultas")
from Consulta import *


#Metodo para guardar los Departamentos en la base de datos
def ingresarDepartamento(codigo, nombre, poblacion):
    consultaSql = "INSERT INTO Proyecto.Departamentos VALUES(%s,%s,%s);"# %s hace referencia a que son parametros
    valores = (codigo, nombre, poblacion) #los valores tienen que estar en una tupla
    Consulta.agregarRegistro(consultaSql, valores)
        
        
#esta funcion me devuelve todos los Departamentos de la base de datos
def obtenerDepartamentos():
    consultaSql = "SELECT * FROM Proyecto.Departamentos;"
    return Consulta.obtenerRegistros(consultaSql)
    
    
#Funcion para obtener un departamento por su id
def obtenerDepartamento(codigo):
    consultaSql = "SELECT * FROM Proyecto.Departamentos WHERE Departamentos.codigo=%s;"
    valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
    return Consulta.obtenerRegistro(consultaSql, valores)
            
    
#Funcion para modificar un departamento
def modificarDepartamento(codigo, nombre, poblacion):
    consultaSql = ("UPDATE Proyecto.Departamentos "
            "SET Departamentos.nombre = %s, "
            "Departamentos.poblacion = %s "
            "WHERE codigo = %s;")#hace referencia a que son parametros
    valores = (nombre, poblacion, codigo) #los valores tienen que estar en una tupla
    Consulta.modificarRegistro(consultaSql, valores)   


#Funcion para eliminar el departamento por su codigo
def eliminarDepartamento(codigo):
    consultaSql = "DELETE FROM Proyecto.Departamentos WHERE Departamentos.codigo=%s;"# %s hace referencia a que son parametros
    valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
    Consulta.eliminarRegistro(consultaSql, valores)
        
