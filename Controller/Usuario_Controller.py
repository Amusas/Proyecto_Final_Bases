import sys
sys.path.append("./Backend/Cruds")
import UsuarioCRUD as crud

def registrarUsuario(codigo, nombreUsario, contrasenia, permiso):
   crud.ingresarUsuario(codigo, nombreUsario, contrasenia, permiso)

def buscarUsuario(codigo):
   return crud.obtenerUsuario(codigo)

def actualizarUsuario(codigo, nombreUsario, contrasenia, permiso):
   crud.modificarUsuario(codigo, nombreUsario, contrasenia, permiso)

def eliminarUsuario(codigo):
   crud.eliminarUsuario(codigo)