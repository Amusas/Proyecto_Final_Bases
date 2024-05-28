import sys
sys.path.append("./Backend/Cruds")
import DepartamentoCRUD as crud

def crearDepartamento(codigo, nombre, poblacion):
    crud.ingresarDepartamento(codigo, nombre, poblacion)

def buscarDepartamento(codigo):
    return(crud.obtenerDepartamento(codigo))

def actualizarDepartamento(codigo, nombre, poblacion):
    crud.modificarDepartamento(codigo, nombre, poblacion)

def eliminarDepartamento(codigo):
    crud.eliminarDepartamento(codigo)