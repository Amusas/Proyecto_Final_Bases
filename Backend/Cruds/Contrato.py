import sys
sys.path.append("./Backend/Conexion_base_datos")#para que el compilador de python encuntre los modulos
sys.path.append("./Backend/consultas")
from Conexion import *
from Consulta import *

class Contrato:
    
    #las fechas se tienen que enviar como tipo datetime
    #Metodo para guardar los contratos en la base de datos
    def ingresarContrato(codigo, empleado, cargo, sucursal, fecha_inicio, fecha_terminacion):
        consultaSql = "INSERT INTO Proyecto.Contratos VALUES(%s,%s,%s,%s,%s,%s);"# %s hace referencia a que son parametros
        valores = (codigo, empleado, cargo, sucursal, fecha_inicio, fecha_terminacion) #los valores tienen que estar en una tupla
        Consulta.agregarRegistro(consultaSql, valores)
        
        
    #esta funcion me devuelve todos los contratos de la base de datos
    def obtenerContratos():
        consultaSql = "SELECT * FROM Proyecto.Contratos;"
        return Consulta.obtenerRegistros(consultaSql)
    
    
    #Funcion para obtener un contrato por su id
    def obtenerContrato(codigo):
        consultaSql = "SELECT * FROM Proyecto.Contratos WHERE Contratos.codigo=%s;"
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        return Consulta.obtenerRegistro(consultaSql, valores)
            
    
    #Funcion para modificar un contrato
    def modificarContrato(codigo, empleado, cargo, sucursal, fecha_inicio, fecha_terminacion):
        consultaSql = ("UPDATE Proyecto.Contratos "
               "SET Contratos.empleado = %s, "
               "Contratos.cargo = %s, "
               "Contratos.sucursal = %s, "
               "Contratos.fecha_inicio = %s, "
               "Contratos.fecha_terminacion = %s "
               "WHERE codigo = %s;")#hace referencia a que son parametros
        valores = (empleado, cargo, sucursal, fecha_inicio, fecha_terminacion, codigo) #los valores tienen que estar en una tupla
        Consulta.modificarRegistro(consultaSql, valores)   


    #Funcion para eliminar el contrato por su codigo
    def eliminarContrato(codigo):
        consultaSql = "DELETE FROM Proyecto.Contratos WHERE Contratos.codigo=%s;"# %s hace referencia a que son parametros
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        Consulta.eliminarRegistro(consultaSql, valores)
        
        