import sys
sys.path.append("./Backend/Conexion_base_datos")#para que el compilador de python encuntre los modulos
sys.path.append("./Backend/consultas")
from Conexion import *
from Consulta import *

class Sucursal:
    
    #Metodo para guardar las sucursales en la base de datos
    def ingresarSucursal(codigo, nombre, departamento, municipio, director, presupuesto):
        consultaSql = "INSERT INTO Proyecto.Sucursales VALUES(%s,%s,%s,%s,%s,%s);"# %s hace referencia a que son parametros
        valores = (codigo, nombre, departamento, municipio, director, presupuesto) #los valores tienen que estar en una tupla
        Consulta.agregarRegistro(consultaSql, valores)
        
        
    #esta funcion me devuelve todos las sucursales de la base de datos
    def obtenerSucursales():
        consultaSql = "SELECT * FROM Proyecto.Sucursales;"
        return Consulta.obtenerRegistros(consultaSql)
    
    
    #Funcion para obtener una sucursal por su id
    def obtenerSucursal(codigo):
        consultaSql = "SELECT * FROM Proyecto.Sucursales WHERE Sucursales.codigo=%s;"
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        return Consulta.obtenerRegistro(consultaSql, valores)
            
    
    #Funcion para modificar una sucursal
    def modificarSucursal(codigo, nombre, departamento, municipio, director, presupuesto):
        consultaSql = ("UPDATE Proyecto.Sucursales "
               "SET Sucursales.nombre = %s, "
               "Sucursales.departamento = %s, "
               "Sucursales.municipio = %s, "
               "Sucursales.director = %s, "
               "Sucursales.presupuesto_anual = %s "
               "WHERE codigo = %s;")#hace referencia a que son parametros
        valores = (nombre, departamento, municipio, director, presupuesto, codigo) #los valores tienen que estar en una tupla
        Consulta.modificarRegistro(consultaSql, valores)   


    #Funcion para eliminar la sucursal por su codigo
    def eliminarSucursal(codigo):
        consultaSql = "DELETE FROM Proyecto.Sucursales WHERE Sucursales.codigo=%s;"# %s hace referencia a que son parametros
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        Consulta.eliminarRegistro(consultaSql, valores)
       
           
    