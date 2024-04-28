import sys
sys.path.append("./Backend/consultas")
from Consulta import *


#Metodo para guardar los Funciones_Asignadas en la base de datos
def ingresarFuncionesAsignadas(codigo, funcion):
    consultaSql = "INSERT INTO Proyecto.Funciones_Asignadas VALUES(%s,%s);"# %s hace referencia a que son parametros
    valores = (codigo, funcion) #los valores tienen que estar en una tupla
    Consulta.agregarRegistro(consultaSql, valores)
        
        
#esta funcion me devuelve todos los Funciones_Asignadas de la base de datos
def obtenerFuncionesAsignadas():
    consultaSql = "SELECT * FROM Proyecto.Funciones_Asignadas;"
    return Consulta.obtenerRegistros(consultaSql)
    
    
#Funcion para obtener una Funciones_Asignadas por su id
def obtenerFuncionAsignada(codigo):
    consultaSql = "SELECT * FROM Proyecto.Funciones_Asignadas WHERE Funciones_Asignadas.codigo=%s;"
    valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
    return Consulta.obtenerRegistro(consultaSql, valores)
            
    
#Funcion para modificar una Funciones_Asignadas
def modificarFuncionesAsignadas(codigo, funcion):
    consultaSql = ("UPDATE Proyecto.Funciones_Asignadas "
            "SET Funciones_Asignadas.nombre = %s "
            "WHERE codigo = %s;")#hace referencia a que son parametros
    valores = (funcion, codigo) #los valores tienen que estar en una tupla
    Consulta.modificarRegistro(consultaSql, valores)   


#Funcion para eliminar el Funciones_Asignadas por su codigo
def eliminarFuncionesAsignadas(codigo):
    consultaSql = "DELETE FROM Proyecto.Funciones_Asignadas WHERE Funciones_Asignadas.codigo=%s;"# %s hace referencia a que son parametros
    valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
    Consulta.eliminarRegistro(consultaSql, valores)
    
eliminarFuncionesAsignadas('01')
        