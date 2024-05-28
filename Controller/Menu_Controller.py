from Sesion import Sesion

def comprobar_Permisos_General():
    sesion = Sesion.obtener_instancia()
    if sesion.permisos == '03':
        return False
    return True

def comprobar_Permisos():
    sesion = Sesion.obtener_instancia()
    if sesion.permisos == '03':
        return 3
    elif sesion.permisos == '02':
        return 2
    else:
        return 1