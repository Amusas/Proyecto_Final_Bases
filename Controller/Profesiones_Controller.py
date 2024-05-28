import sys
sys.path.append("./Backend/Cruds")
import ProfesionCRUD as crud

def registrarProfesion(codigo,nombre):
    crud.ingresarProfesion(codigo, nombre)

def obtenerProfesion(codigo):
    return crud.obtenerProfesion(codigo)

def actualizarProfesion(codigo, nombre):
    crud.modificarProfesion(codigo, nombre)

def eliminarProfesion(codigo):
    crud.eliminarProfesion(codigo)