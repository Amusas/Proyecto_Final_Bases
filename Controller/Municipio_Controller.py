import sys
sys.path.append("./Backend/Cruds")
import MunicipioCRUD as crud


def agregarMunicipio(codigo, nombre, poblacion, tipoMunicipio, departamento):
    crud.ingresarMunicipio(codigo, nombre, poblacion, tipoMunicipio, departamento)

def buscarMunicipio(codigo):
    return crud.obtenerMunicipio(codigo)

def actualizarMunicipio(codigo, nombre, poblacion, tipoMunicipio, departamento):
    crud.modificarMunicipio(codigo, nombre, poblacion, tipoMunicipio, departamento)

def eliminarMunicipio(codigo):
    crud.eliminarMunicipio(codigo)