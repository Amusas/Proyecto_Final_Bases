import sys
sys.path.append("./Backend/consultas")
from Consulta import *

    
#metodo para la relacion muchos a muchos de empleado y profesion
def ingresarProfesiones(codigo, profesiones):
    #Asignacion de profesion al Empleado
    consultaSql = "INSERT INTO Proyecto.Profesion_Empleado (id_empleado, id_profesion) VALUES (%s, %s)"
    for profesion in profesiones:
        valores = (codigo, profesion)
        Consulta.agregarRegistro(consultaSql, valores)
    
#Metodo para guardar los empleados en la base de datos
#las profesiones deben ser enviadas como una lista de strings
def ingresarEmpleado(codigo, cedula, nombre, apellido, direccion, telefono, cargo, profesiones):
    consultaSql = "INSERT INTO Proyecto.Empleados VALUES(%s,%s,%s,%s,%s,%s,%s);" 
    #los valores tienen que estar en una tupla
    valores = (codigo, cedula, nombre, apellido, direccion, telefono, cargo) 
    codigoValidacion = Consulta.agregarRegistro(consultaSql, valores)
    if codigoValidacion == -1:#retorna -1 si hubo un error de integridad(llave primaria repetida)
        return codigoValidacion
    ingresarProfesiones(codigo, profesiones)
        
              
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
def modificarEmpleado(codigo, cedula, nombre, apellido, direccion, telefono, cargo, profesiones, codigosEmpleadoProfesion):
    consultaSql = ("UPDATE Proyecto.Empleados "
           "SET Empleados.cedula = %s, "
           "Empleados.nombre = %s, "
           "Empleados.apellido = %s, "
           "Empleados.direccion = %s, "
           "Empleados.telefono_contacto = %s, "
           "Empleados.id_cargo = %s "
           "WHERE codigo = %s;")#hace referencia a que son parametros
    valores = (cedula, nombre, apellido, direccion, telefono, cargo, codigo)
    Consulta.modificarRegistro(consultaSql, valores)
    modificarProfesiones(codigosEmpleadoProfesion, profesiones)   

#modifica las profesiones en la tabla de muchos a muchos
def modificarProfesiones(codigos, profesiones):
    consultaSQL = ("UPDATE Proyecto.Profesion_Empleado "
           "SET Profesion_Empleado.id_profesion  = %s "
           "WHERE codigo = %s;")
    for codigo,profesion in zip(codigos,profesiones):
        valores = (profesion, codigo)
        Consulta.modificarRegistro(consultaSQL, valores)


#Funcion para eliminar el empleado por su codigo
def eliminarEmpleado(codigo):
    consultaSql = "DELETE FROM Proyecto.Empleados WHERE Empleados.codigo=%s;"# %s hace referencia a que son parametros
    valores = (codigo,) #se agrega la ',' para que python reconozca que es una tupla y no genere errores   
    #eliminar las filas en Profesion_Empleado que hacen referencia al idEmpleado
    Consulta.eliminarRegistro("DELETE FROM Proyecto.Profesion_Empleado WHERE Profesion_Empleado.id_empleado = %s", (codigo,))   
    Consulta.eliminarRegistro(consultaSql, valores)


modificarEmpleado('10', '6543', 'Camilo', 'Bedoya', 'ghfds', '12344', '01', ['01','02'], [4,5] )

    