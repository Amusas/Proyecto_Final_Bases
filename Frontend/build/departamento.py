
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path
import sys
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, END
sys.path.append("./Controller")
import Departamento_Controller as dc


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame6")

def agregarDepartamento(codigo, nombre, poblacion):
    dc.crearDepartamento(codigo, nombre, poblacion)
    
def buscarDepartamento(codigo, tfNombre, tfPoblacion):
    departamento.delete(0, END)
    tfNombre.delete(0, END)
    tfPoblacion.delete(0, END)

    departamento = dc.buscarDepartamento(codigo)
    tfNombre.insert(0, departamento[0][1])
    tfPoblacion.insert(0, str(departamento[0][2]))
    
def actualizarDepartamento(codigo, nombre, poblacion):
    dc.actualizarDepartamento(codigo, nombre, poblacion)

def eliminarDepartamento(codigo):
    dc.eliminarDepartamento(codigo)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def iniciar():  
    window = Tk()

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
        56.177495002746355,
        977.0,
        58.6199951171875,
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
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    btnHome.place(
        x=70.83255004882812,
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
        command=lambda: print("button_2 clicked"),
        relief="flat"
    )
    btnAtras.place(
        x=0.0,
        y=0.0,
        width=69.0,
        height=58.619998931884766
    )

    canvas.create_rectangle(
        34.195037841796875,
        92.81494140625,
        928.1500549316406,
        503.1549377441406,
        fill="#6CD4A8",
        outline="")

    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        501.8687438964844,
        337.20375061035156,
        image=entry_image_1
    )
    poblacion = Entry(
        bd=0,
        bg="#73F7C0",
        fg="#000716",
        highlightthickness=0
    )
    poblacion.place(
        x=337.0,
        y=314.0,
        width=329.73748779296875,
        height=44.407501220703125
    )

    canvas.create_text(
        105.027587890625,
        312.6400146484375,
        anchor="nw",
        text="Poblacion:",
        fill="#FFFFFF",
        font=("MontserratAlternates Bold", 24 * -1)
    )

    canvas.create_text(
        105.027587890625,
        119.6824951171875,
        anchor="nw",
        text="Código:",
        fill="#FFFFFF",
        font=("MontserratAlternates Bold", 24 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        501.9335632324219,
        134.33748054504395,
        image=entry_image_3
    )
    codigo = Entry(
        bd=0,
        bg="#73F7C0",
        fg="#000716",
        highlightthickness=0
    )
    codigo.place(
        x=337.0648193359375,
        y=112.35498046875,
        width=329.73748779296875,
        height=41.96500015258789
    )

    canvas.create_text(
        105.027587890625,
        175.8599853515625,
        anchor="nw",
        text="Nombre:",
        fill="#FFFFFF",
        font=("MontserratAlternates Bold", 24 * -1)
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        501.9335632324219,
        201.50624084472656,
        image=entry_image_5
    )
    tfNombre = Entry(
        bd=0,
        bg="#73F7C0",
        fg="#000716",
        highlightthickness=0
    )
    tfNombre.place(
        x=337.0648193359375,
        y=178.302490234375,
        width=329.73748779296875,
        height=44.407501220703125
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    btnEliminar = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: eliminarDepartamento(codigo.get()),
        relief="flat"
    )
    btnEliminar.place(
        x=718.0,
        y=371.0,
        width=176.1521759033203,
        height=41.21741485595703
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    btnActualizar = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: actualizarDepartamento(codigo.get(),tfNombre.get(), float(poblacion.get())),
        relief="flat"
    )
    btnActualizar.place(
        x=718.0,
        y=308.0,
        width=176.1521759033203,
        height=41.47827911376953
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    btnBuscar = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: buscarDepartamento(codigo.get(),tfNombre, poblacion),
        relief="flat"
    )
    btnBuscar.place(
        x=718.0,
        y=182.978271484375,
        width=176.1521759033203,
        height=41.02173614501953
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    btnAgregar = Button(
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: agregarDepartamento(codigo.get(), tfNombre.get(), float(poblacion.get())),
        relief="flat"
    )
    btnAgregar.place(
        x=720.0,
        y=245.7174072265625,
        width=176.5652618408203,
        height=41.2825927734375
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    btnDepartamento = Button(
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_7 clicked"),
        relief="flat"
    )
    btnDepartamento.place(
        x=263.0,
        y=5.0,
        width=166.0,
        height=63.0
    )

    button_image_8 = PhotoImage(
        file=relative_to_assets("button_8.png"))
    btnMunicipio = Button(
        image=button_image_8,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_8 clicked"),
        relief="flat"
    )
    btnMunicipio.place(
        x=430.0,
        y=5.0,
        width=117.0,
        height=63.0
    )

    button_image_9 = PhotoImage(
        file=relative_to_assets("button_9.png"))
    btnSucursal = Button(
        image=button_image_9,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_9 clicked"),
        relief="flat"
    )
    btnSucursal.place(
        x=548.0,
        y=5.0,
        width=114.0,
        height=63.0
    )

    button_image_10 = PhotoImage(
        file=relative_to_assets("button_10.png"))
    btnProfesiones = Button(
        image=button_image_10,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_10 clicked"),
        relief="flat"
    )
    btnProfesiones.place(
        x=737.0,
        y=5.0,
        width=118.0,
        height=63.0
    )

    button_image_11 = PhotoImage(
        file=relative_to_assets("button_11.png"))
    btnEmpleado = Button(
        image=button_image_11,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_11 clicked"),
        relief="flat"
    )
    btnEmpleado.place(
        x=856.0,
        y=5.0,
        width=121.0,
        height=63.0
    )

    button_image_12 = PhotoImage(
        file=relative_to_assets("button_12.png"))
    btnCargos = Button(
        image=button_image_12,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_12 clicked"),
        relief="flat"
    )
    btnCargos.place(
        x=663.0,
        y=5.0,
        width=73.0,
        height=63.0
    )
    window.resizable(False, False)
    window.mainloop()

