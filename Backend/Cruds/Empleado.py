import sys
sys.path.append("./Backend/consultas")
from Consulta import *

class Empleado:
    
    #Metodo para guardar los empleados en la base de datos
    def ingresarEmpleado(codigo, cedula, nombre, direccion, telefono, cargo, profesion):
        consultaSql = "INSERT INTO Proyecto.Empleados VALUES(%s,%s,%s,%s,%s,%s,%s);" 
        #los valores tienen que estar en una tupla
        valores = (codigo, cedula, nombre, direccion, telefono, cargo, profesion) 
        Consulta.agregarRegistro(consultaSql, valores)
        
        
    #esta funcion me devuelve todos los empleados de la base de datos
    def obtenerEmpleados():
        consultaSql = "SELECT * FROM Proyecto.Empleados;"
        return Consulta.obtenerRegistros(consultaSql)
    
    
    #Funcion para obtener un empleado por su id
    def obtenerEmpleado(codigo):
        consultaSql = "SELECT * FROM Proyecto.Empleados WHERE Empleados.codigo=%s;"
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        return Consulta.obtenerRegistro(consultaSql, valores)
            
    
    #Funcion para modificar un empleado
    def modificarEmpleado(codigo, cedula, nombre, direccion, telefono, cargo, profesion):
        consultaSql = ("UPDATE Proyecto.Empleados "
               "SET Empleados.cedula = %s, "
               "Empleados.nombre = %s, "
               "Empleados.direccion = %s, "
               "Empleados.telefono = %s, "
               "Empleados.cargo = %s, "
               "Empleados.profesion = %s "
               "WHERE codigo = %s;")#hace referencia a que son parametros
        valores = (cedula, nombre, direccion, telefono, cargo, profesion, codigo) 
        Consulta.modificarRegistro(consultaSql, valores)   


    #Funcion para eliminar el empleado por su codigo
    def eliminarEmpleado(codigo):
        consultaSql = "DELETE FROM Proyecto.Empleados WHERE Empleados.codigo=%s;"# %s hace referencia a que son parametros
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        Consulta.eliminarRegistro(consultaSql, valores)
        
        