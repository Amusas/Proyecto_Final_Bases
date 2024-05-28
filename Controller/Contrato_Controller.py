import sys
sys.path.append("./Backend/Cruds")
import ContratoCRUD as crud

def ingresarContrato(codigo, empleado, cargo, sucursal, fecha_inicio, fecha_terminacion):
    crud.ingresarContrato(codigo, empleado, cargo, sucursal, fecha_inicio, fecha_terminacion)

def obtenerContrato(codigo):
    return crud.obtenerContrato(codigo)

def modificarContrato(codigo, empleado, cargo, sucursal, fecha_inicio, fecha_terminacion):
    crud.modificarContrato(codigo, empleado, cargo, sucursal, fecha_inicio, fecha_terminacion)

def eliminarContrato(codigo):
    crud.eliminarContrato(codigo)