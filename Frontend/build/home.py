
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import sys
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
sys.path.append("./Frontend")
import build.municipios as municipio
import build.empleado as empleado
import build.departamento as departamento
import build.profesiones as profesion
import build.cargos as cargos
import build.sucursales as sucursal
import build.menu as menu
import Login_Controller as lc


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame1")

def cerrar(app):
    try:
        lc.cerrarSesion()
        app.destroy()
    except:
        app.destroy()  

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def iniciarunicipio(window):
    window.destroy()
    municipio.iniciar()
    

def iniciarEmpleadoGui(window):
    window.destroy()
    empleado.iniciar()
    
def iniciarDepartamentoGui(window):
    window.destroy()
    departamento.iniciar()
    
def iniciarProfesionGui(window):
    window.destroy()
    profesion.iniciar()
    
def iniciarCargoGui(window):
    window.destroy()
    cargos.iniciar()
    
def iniciarSucursalGui(window):
    window.destroy()
    sucursal.iniciar()
    
def iniciarMenu(window):
    window.destroy()
    menu.iniciar()

def iniciar():
    window = Tk()
    window.protocol("WM_DELETE_WINDOW", lambda: cerrar(window))
    window.geometry("965x554")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 554,
        width = 965,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        58.0,
        965.0,
        555.0,
        fill="#BCF3DC",
        outline="")

    canvas.create_rectangle(
        -2.4124999046325684,
        55.487524509429704,
        965.0,
        57.9000244140625,
        fill="#BCF3DC",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    btnHome = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciarMenu(window),
        relief="flat"
    )
    btnHome.place(
        x=64.0,
        y=0.0,
        width=64.56745910644531,
        height=58.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    btnVolver = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciarMenu(window),
        relief="flat"
    )
    btnVolver.place(
        x=0.0,
        y=0.0,
        width=64.53239440917969,
        height=58.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    btnDepartamento = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciarDepartamentoGui(window),
        relief="flat"
    )
    btnDepartamento.place(
        x=251.0,
        y=5.0,
        width=166.0,
        height=63.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    btnMunicipio = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciarunicipio(window),
        relief="flat"
    )
    btnMunicipio.place(
        x=418.0,
        y=5.0,
        width=117.0,
        height=63.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    btnSucursales = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciarSucursalGui(window),
        relief="flat"
    )
    btnSucursales.place(
        x=536.0,
        y=5.0,
        width=114.0,
        height=63.0
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    btnProfesiones = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciarProfesionGui(window),
        relief="flat"
    )
    btnProfesiones.place(
        x=725.0,
        y=5.0,
        width=118.0,
        height=63.0
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    btnEmpleado = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciarEmpleadoGui(window),
        relief="flat"
    )
    btnEmpleado.place(
        x=844.0,
        y=5.0,
        width=121.0,
        height=63.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    btnCargos = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciarCargoGui(window),
        relief="flat"
    )
    btnCargos.place(
        x=651.0,
        y=5.0,
        width=73.0,
        height=63.0
    )

    canvas.create_rectangle(
        41.0,
        90.0,
        923.9749755859375,
        495.29998779296875,
        fill="#6CD4A8",
        outline="")

    canvas.create_text(
        323.2749938964844,
        123.0374755859375,
        anchor="nw",
        text="Bienvenid@",
        fill="#225B43",
        font=("MuseoModerno Bold", 38 * -1)
    )

    canvas.create_text(
        104.0,
        215.0,
        anchor="nw",
        text="Nombre_usuario",
        fill="#225B43",
        font=("MontaguSlab Bold", 48 * -1)
    )

    canvas.create_text(
        104.0,
        296.0,
        anchor="nw",
        text="Acá puede encontrar lo siguiente:",
        fill="#225B43",
        font=("MontaguSlab Bold", 24 * -1)
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    btnSucursales2 = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    btnSucursales2.place(
        x=205.0625,
        y=359.4625244140625,
        width=269.9375,
        height=33.775001525878906
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    btnDepartamento2 = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_10 clicked"),
        relief="flat"
    )
    btnDepartamento2.place(
        x=205.0,
        y=430.0,
        width=270.0,
        height=34.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    btnMunicipio2 = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_11 clicked"),
        relief="flat"
    )
    btnMunicipio2.place(
        x=207.0,
        y=396.0,
        width=268.0,
        height=34.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    btnCargos2 = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_12 clicked"),
        relief="flat"
    )
    btnCargos2.place(
        x=530.75,
        y=393.0,
        width=243.66250610351562,
        height=34.012489318847656
    )

    button_image_13 = PhotoImage(
        file=relative_to_assets("button_13.png"))
    btnProfesiones2 = Button(
        image=button_image_13,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_13 clicked"),
        relief="flat"
    )
    btnProfesiones2.place(
        x=531.0,
        y=427.0,
        width=243.66250610351562,
        height=34.012489318847656
    )

    button_image_14 = PhotoImage(
        file=relative_to_assets("button_14.png"))
    btnEmpleado2 = Button(
        image=button_image_14,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_14 clicked"),
        relief="flat"
    )
    btnEmpleado2.place(
        x=530.75,
        y=357.04998779296875,
        width=243.66250610351562,
        height=33.775001525878906
    )
    window.resizable(False, False)
    window.mainloop()

