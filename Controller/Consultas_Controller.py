import sys
sys.path.append("./Backend/consultas")
from Consulta import *

def ejecutarConsulta():
    consultaSQL = (
        "SELECT d.nombre AS departamento, "
        "COUNT(s.codigo) AS cantidad_sucursales "
        "FROM Sucursales s "
        "JOIN Departamentos d ON s.id_departamento = d.codigo "
        "GROUP BY d.nombre "
        "ORDER BY cantidad_sucursales DESC;"
    )
    return Consulta.obtenerRegistros(consultaSQL)


def ejecutarConsulta2():
    consultaSQL = ("SELECT s.nombre AS sucursal, "
                        "COUNT(c.codigo) AS cantidad_contratos "
                    "FROM "
                        "Contratos c "
                    "JOIN "
                        "Sucursales s ON c.id_sucursal = s.codigo "
                    "WHERE "
                        "c.fecha_inicio >= '2024-01-01' "
                    "GROUP BY "
                        "s.nombre "
                    "ORDER BY "
                        "cantidad_contratos DESC; ")
    return Consulta.obtenerRegistros(consultaSQL)
    
    

def ejecutarConsultaEsporadico():
    consultaSQL = (
        "SELECT s.nombre AS sucursal, "
        "COUNT(c.id_empleado) AS cantidad_empleados "
        "FROM Contratos c "
        "JOIN Sucursales s ON c.id_sucursal = s.codigo "
        "GROUP BY s.nombre "
        "ORDER BY cantidad_empleados DESC;"
    )
    return Consulta.obtenerRegistros(consultaSQL)


def ejecutarConsulta2Esporadico():
    consultaSQL = """
        SELECT
            e.nombre AS nombre_empleado,
            e.cedula,
            s.nombre AS nombre_sucursal
        FROM
            Empleados e
        JOIN
            Contratos co ON e.codigo = co.id_empleado
        JOIN
            Sucursales s ON co.id_sucursal = s.codigo;
    """
    return Consulta.obtenerRegistros(consultaSQL)
    
def ejecutarConsultaChichi():
    # Realizar la consulta SQL
    consultaSQL = """
        SELECT
            d.nombre AS nombre_departamento,
            SUM(s.presupuesto_anual) AS total_presupuesto
        FROM
            Departamentos d
        JOIN
            Sucursales s ON d.codigo = s.id_departamento
        GROUP BY
            d.nombre;
    """
    return Consulta.obtenerRegistros(consultaSQL)


def ejecutarConsulta2Chichi():
    consultaSQL = """
        SELECT
            d.nombre AS nombre_departamento,
            s.codigo AS codigo_sucursal,
            s.nombre AS nombre_sucursal,
            s.presupuesto_anual AS presupuesto_asignado
        FROM
            Departamentos d
        JOIN
            Sucursales s ON d.codigo = s.id_departamento
        WHERE
            (s.presupuesto_anual, s.id_departamento) IN (
                SELECT
                    MAX(s1.presupuesto_anual) AS max_presupuesto,
                    s1.id_departamento
                FROM
                    Sucursales s1
                GROUP BY
                    s1.id_departamento
            );
    """
    return Consulta.obtenerRegistros(consultaSQL)