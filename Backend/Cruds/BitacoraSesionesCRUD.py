import sys
sys.path.append("./Backend/consultas")
from Consulta import *

    
#Metodo para guardar las bitacoras en la base de datos
def ingresarBitacora(usuario, fecha_entrada):
    consultaSql = "INSERT INTO Proyecto.Bitacora_sesiones VALUES(%s,%s,%s);"# %s hace referencia a que son parametros
    valores = (usuario, fecha_entrada, None) #los valores tienen que estar en una tupla
    Consulta.agregarRegistro(consultaSql, valores)
    
    
#Funciones para Auditar la salida
def fechaSalidaBitacora(fecha_salida, usuario):
    consultaSql = ("UPDATE Proyecto.Bitacora_sesiones "
            "SET Bitacora_sesiones.fecha_salida = %s "
            "WHERE id_usuario = %s AND fecha_salida IS NULL;")# %s hace referencia a que son parametros
    valores = (fecha_salida, usuario) #los valores tienen que estar en una tupla
    Consulta.modificarRegistro(consultaSql, valores)
    
        
#esta funcion me devuelve todos las bitacoras de la base de datos
def obtenerBitacoras():
    consultaSql = "SELECT * FROM Proyecto.Bitacora_sesiones;"
    return Consulta.obtenerRegistros(consultaSql)
    
    
#Funcion para obtener bitacoras por su usuario
def obtenerBitacora(codigoUsuario):
    consultaSql = "SELECT * FROM Proyecto.Bitacora_sesiones WHERE Bitacora_sesiones.id_usuario=%s;"
    valores = (codigoUsuario,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
    return Consulta.obtenerRegistro(consultaSql, valores)
    
    