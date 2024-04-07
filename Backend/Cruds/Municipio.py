import sys
sys.path.append("./Backend/consultas")
from Consulta import *

class Municipio:
    
    #Metodo para guardar los municipios en la base de datos
    def ingresarMunicipio(codigo, nombre, poblacion, tipoMunicipio, departamento):
        consultaSql = "INSERT INTO Proyecto.Municipios VALUES(%s,%s,%s,%s,%s);"# %s hace referencia a que son parametros
        valores = (codigo, nombre, poblacion, tipoMunicipio, departamento) #los valores tienen que estar en una tupla
        Consulta.agregarRegistro(consultaSql, valores)
        
        
    #esta funcion me devuelve todos los municipios de la base de datos
    def obtenerMunicipios():
        consultaSql = "SELECT * FROM Proyecto.Municipios;"
        return Consulta.obtenerRegistros(consultaSql)
    
    
    #Funcion para obtener un municipio por su id
    def obtenerMunicipio(codigo):
        consultaSql = "SELECT * FROM Proyecto.Municipios WHERE Municipios.codigo=%s;"
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        return Consulta.obtenerRegistro(consultaSql, valores)
            
    
    #Funcion para modificar un municipio
    def modificarMunicipio(codigo, nombre, poblacion, tipoMunicipio, departamento):
        consultaSql = ("UPDATE Proyecto.Municipios "
               "SET Municipios.nombre = %s, "
               "Municipios.poblacion = %s, "
               "Municipios.tipo_municipio = %s, "
               "Municipios.departamento = %s "
               "WHERE codigo = %s;")#hace referencia a que son parametros
        valores = (nombre, poblacion, tipoMunicipio, departamento, codigo) #los valores tienen que estar en una tupla
        Consulta.modificarRegistro(consultaSql, valores)   


    #Funcion para eliminar el municipio por su codigo
    def eliminarMunicipio(codigo):
        consultaSql = "DELETE FROM Proyecto.Municipios WHERE Municipios.codigo=%s;"# %s hace referencia a que son parametros
        valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
        Consulta.eliminarRegistro(consultaSql, valores)
       
