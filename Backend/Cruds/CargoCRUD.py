import sys
sys.path.append("./Backend/consultas")
from Consulta import *


#metodo para la relacion muchos a muchos de Cargos y sus funciones
def ingresarFunciones(codigo, funciones):
    #Asignacion de profesion al Empleado
    consultaSql = "INSERT INTO Proyecto.Cargos_Funciones_Asignadas (id_cargo, id_funcion) VALUES (%s, %s)"
    for funcion in funciones:
        valores = (codigo, funcion)
        Consulta.agregarRegistro(consultaSql, valores)

    
#Metodo para guardar los cargos en la base de datos
def ingresarCargo(codigo, nombre, salario, funciones):
    consultaSql = "INSERT INTO Proyecto.Cargos VALUES(%s,%s,%s);"# %s hace referencia a que son parametros
    valores = (codigo, nombre, salario) #los valores tienen que estar en una tupla
    codigoValidacion = Consulta.agregarRegistro(consultaSql, valores)
    if codigoValidacion == -1:#retorna -1 si hubo un error de integridad(llave primaria repetida)
        return codigoValidacion
    ingresarFunciones(codigo, funciones)
        
        
#esta funcion me devuelve todos los cargos de la base de datos
def obtenerCargos():
    consultaSql = "SELECT * FROM Proyecto.Cargos;"
    return Consulta.obtenerRegistros(consultaSql)
    
    
#Funcion para obtener un cargo por su id
def obtenerCargo(codigo):
    consultaSql = "SELECT * FROM Proyecto.Cargos WHERE Cargos.codigo=%s;"
    consultaSql2 = "SELECT * FROM Proyecto.Cargos_Funciones_Asignadas WHERE Cargos_Funciones_Asignadas.id_cargo=%s"
    valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores     
    return Consulta.obtenerRegistro(consultaSql, valores), Consulta.obtenerRegistro(consultaSql2, valores)
   

#modifica las funciones de la tabla muchos a muchos
def modificarFunciones(codigos, funciones):
    consultaSQL = ("UPDATE Proyecto.Cargos_Funciones_Asignadas "
           "SET Cargos_Funciones_Asignadas.id_funcion  = %s "
           "WHERE codigo = %s;")
    for codigo,funcion in zip(codigos,funciones):
        valores = (funcion, codigo)
        Consulta.modificarRegistro(consultaSQL, valores)   
            
    
#Funcion para modificar un Cargo
def modificarCargo(codigo, nombre, salario, funciones, codigosCargosFunciones):
    consultaSql = ("UPDATE Proyecto.Cargos "
           "SET Cargos.nombre = %s, "
           "Cargos.salario = %s, "
           "WHERE codigo = %s;")#hace referencia a que son parametros
    valores = (nombre, salario, funciones, codigo) #los valores tienen que estar en una tupla
    Consulta.modificarRegistro(consultaSql, valores) 
    modificarFunciones(codigosCargosFunciones, funciones)  


#Funcion para eliminar el cargo por su codigo
def eliminarCargo(codigo):
    consultaSql = "DELETE FROM Proyecto.Cargos WHERE Cargos.codigo=%s;"# %s hace referencia a que son parametros
    valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores    
    Consulta.eliminarRegistro(consultaSql, valores) 
    
        