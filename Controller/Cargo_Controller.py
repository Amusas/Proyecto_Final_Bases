import sys
sys.path.append("./Backend/Cruds")
import CargoCRUD as crud


def registrarCargo(codigo, nombre, salario, funciones):
    crud.ingresarCargo(codigo, nombre, salario, funciones)

def buscarCargo(codigo):
    return crud.obtenerCargo(codigo)

def eliminarCargo(codigo):
    crud.eliminarCargo(codigo)

def actualizarCargo(codigo):
    crud.modificarCargo(codigo, nombre, salario, funciones, codigosCargosFunciones)