import sys
from datetime import datetime
sys.path.append("./Backend/Conexion_base_datos")#para que el compilador de python encuntre los modulos
sys.path.append("./Backend/consultas")
from Conexion import *
from Consulta import *

class BitacoraSesiones:
    
    #Metodo para guardar las bitacoras en la base de datos
    def ingresarBitacora(codigo, usuario, fecha_entrada, fecha_salida):
        consultaSql = "INSERT INTO Proyecto.Bitacora_sesiones VALUES(%s,%s,%s,%s);"# %s hace referencia a que son parametros
        valores = (codigo, usuario, fecha_entrada, fecha_salida) #los valores tienen que estar en una tupla
        Consulta.agregarRegistro(consultaSql, valores)
        
        
    #esta funcion me devuelve todos las bitacoras de la base de datos
    def obtenerBitacoras():
        consultaSql = "SELECT * FROM Proyecto.Bitacora_sesiones;"
        return Consulta.obtenerRegistros(consultaSql)
    
    
    #Funcion para obtener una bitacora por su id
    def obtenerBitacora(codigo):
        consultaSql = "SELECT * FROM Proyecto.Bitacora_sesiones WHERE Bitacora_sesiones.codigo=%s;"
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        return Consulta.obtenerRegistro(consultaSql, valores)
            
    
    #Funcion para modificar una bitacora
    def modificarBitacora(codigo, usuario, fecha_entrada, fecha_salida):
        consultaSql = ("UPDATE Proyecto.Bitacora_sesiones "
               "SET Bitacora_sesiones.usuario = %s, "
               "Bitacora_sesiones.fecha_entrada = %s, "
               "Bitacora_sesiones.fecha_salida = %s "
               "WHERE codigo = %s;")#hace referencia a que son parametros
        valores = (usuario, fecha_entrada, fecha_salida, codigo) #los valores tienen que estar en una tupla
        Consulta.modificarRegistro(consultaSql, valores)   


    #Funcion para eliminar una bitacora por su codigo
    def eliminarBitacora(codigo):
        consultaSql = "DELETE FROM Proyecto.Bitacoras WHERE Bitacoras.codigo=%s;"# %s hace referencia a que son parametros
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        Consulta.eliminarRegistro(consultaSql, valores)
        
        