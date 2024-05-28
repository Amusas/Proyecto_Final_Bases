import sys
sys.path.append("./Backend/Cruds")
import SucursalCRUD as crud

def ingresarSucursal(codigo, nombre, departamento, municipio, director, presupuesto):
    crud.ingresarSucursal(codigo, nombre, departamento, municipio, director, presupuesto)

def obtenerSucursal(codigo):
    return crud.obtenerSucursal(codigo)

def modificarSucursal(codigo, nombre, departamento, municipio, director, presupuesto):
    crud.modificarSucursal(codigo, nombre, departamento, municipio, director, presupuesto)
    
def eliminarSucursal(codigo):
    crud.eliminarSucursal(codigo)   