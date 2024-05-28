

# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer



from pathlib import Path
from datetime import datetime
import sys
sys.path.append("./Frontend")
sys.path.append("./Controller")
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import build.menu as menu
import Login_Controller as lc
import Consultas_Controller as cc
import build.tabla as tabla


def iniciarMenu(window):
    window.destroy()
    menu.iniciar()


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame8")

def cerrar(app):
    try:
        lc.cerrarSesion()
        app.destroy()
    except:
        app.destroy()  

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def ejecutarConsulta2():
    consulta = cc.ejecutarConsulta2()
    tabla.crear_tabla(consulta, ('nombre_sucursal', 'cantidad_contratos'))
    
def ejecutarConsulta():
    consulta = cc.ejecutarConsulta()
    tabla.crear_tabla(consulta, ('departamento', 'cantidad_sucursales'))


def iniciar():
    window = Tk()
    window.protocol("WM_DELETE_WINDOW", lambda: cerrar(window))
    window.geometry("977x561")
    window.configure(bg = "#FFFFFF")


    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 561,
        width = 977,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        -2.442500114440918,
        56.17737293243363,
        977.0,
        58.619873046875,
        fill="#BCF3DC",
        outline="")

    canvas.create_rectangle(
        0.0,
        58.0,
        977.0,
        562.0,
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
        x=70.83251953125,
        y=0.0,
        width=68.38999938964844,
        height=58.619998931884766
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    btnAtras = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: iniciarMenu(window),
        relief="flat"
    )
    btnAtras.place(
        x=0.0,
        y=0.0,
        width=69.0,
        height=58.619998931884766
    )

    canvas.create_rectangle(
        34.195068359375,
        92.81494140625,
        928.1500854492188,
        503.1549377441406,
        fill="#6CD4A8",
        outline="")

    canvas.create_text(
        226.0,
        200.0,
        anchor="nw",
        text="listado que muestre la cantidad de sucursales por departamento:\n",
        fill="#FFFFFF",
        font=("MontserratAlternates Bold", 15 * -1)
    )
    
    consulta1 = Button(
        text = "realizar consulta",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ejecutarConsulta(),
        relief="flat"
    )
     
    consulta1.place(
        x=410.0,
        y=250.0,
        width=130.0,
        height=40.619998931884766
    )
    
    canvas.create_text(
        226.0,
        330.0,
        anchor="nw",
        text="listado en el que aparezcan la cantidad de contratos que se \n hayan realizado por Sucursal a partir del 01/01/2024 :",
        fill="#FFFFFF",
        font=("MontserratAlternates Bold", 15 * -1)
    )
    
    
    consulta2 = Button(
        text = "realizar consulta",
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ejecutarConsulta2(),
        relief="flat"
    )
     
    consulta2.place(
        x=410.0,
        y=380.0,
        width=130.0,
        height=40.619998931884766
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    btnUsuarios = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_3 clicked"),
        relief="flat"
    )
    btnUsuarios.place(
        x=263.0,
        y=5.0,
        width=166.0,
        height=63.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    btnFecha = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_4 clicked"),
        relief="flat"
    )
    
    
    btnFecha.place(
        x=430.0,
        y=5.0,
        width=117.0,
        height=63.0
    )
    window.resizable(False, False)
    window.mainloop()
