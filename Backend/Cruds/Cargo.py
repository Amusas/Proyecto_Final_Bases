import sys
sys.path.append("./Backend/Conexion_base_datos")#para que el compilador de python encuntre los modulos
sys.path.append("./Backend/consultas")
from Conexion import *
from Consulta import *

class Cargo:
    
    #Metodo para guardar los cargos en la base de datos
    def ingresarCargo(codigo, nombre, salario, funciones):
        consultaSql = "INSERT INTO Proyecto.Cargos VALUES(%s,%s,%s,%s);"# %s hace referencia a que son parametros
        valores = (codigo, nombre, salario, funciones) #los valores tienen que estar en una tupla
        Consulta.agregarRegistro(consultaSql, valores)
        
        
    #esta funcion me devuelve todos los cargos de la base de datos
    def obtenerCargos():
        consultaSql = "SELECT * FROM Proyecto.Cargos;"
        return Consulta.obtenerRegistros(consultaSql)
    
    
    #Funcion para obtener un cargo por su id
    def obtenerCargo(codigo):
        consultaSql = "SELECT * FROM Proyecto.Cargos WHERE Cargos.codigo=%s;"
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        return Consulta.obtenerRegistro(consultaSql, valores)
            
    
    #Funcion para modificar un Cargo
    def modificarCargo(codigo, nombre, salario, funciones):
        consultaSql = ("UPDATE Proyecto.Cargos "
               "SET Cargos.nombre = %s, "
               "Cargos.salario = %s, "
               "Cargos.funciones_asignadas = %s "
               "WHERE codigo = %s;")#hace referencia a que son parametros
        valores = (nombre, salario, funciones, codigo) #los valores tienen que estar en una tupla
        Consulta.modificarRegistro(consultaSql, valores)   


    #Funcion para eliminar el cargo por su codigo
    def eliminarCargo(codigo):
        consultaSql = "DELETE FROM Proyecto.Cargos WHERE Cargos.codigo=%s;"# %s hace referencia a que son parametros
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        Consulta.eliminarRegistro(consultaSql, valores)
        
  