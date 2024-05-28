import sys
sys.path.append("./Backend/Cruds")
import EmpleadoCRUD as crud

def registrarEmpleado(codigo, cedula, nombre, apellido, direccion, telefono, cargo, profesiones):
    crud.ingresarEmpleado(codigo, cedula, nombre, apellido, direccion, telefono, cargo, profesiones)

def buscarEmpleado(codigo):
    crud.obtenerEmpleado(codigo)

def actualizarEmpleado(codigo, cedula, nombre, apellido, direccion, telefono, cargo, profesiones, codigosEmpleadoProfesion):
    crud.modificarEmpleado(codigo, cedula, nombre, apellido, direccion, telefono, cargo, profesiones, codigosEmpleadoProfesion)

def eliminarEmpleado(codigo):
    crud.eliminarEmpleado(codigo)