
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import ttk
import sys
sys.path.append("./Frontend")
sys.path.append("./Controller")
import build.menu as menu
import Login_Controller as lc

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame11")

def cerrar(app):
    try:
        lc.cerrarSesion()
        app.destroy()
    except:
        app.destroy()  

def iniciarMenu(window):
    window.destroy()
    menu.iniciar()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

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
        55.48740243911698,
        965.0,
        57.89990234375,
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
        x=69.9625244140625,
        y=0.0,
        width=68.03759765625,
        height=58.0
    )

    canvas.create_rectangle(
        0.0,
        0.0,
        68.0,
        58.0,
        fill="#FFFFFF",
        outline="")

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
        width=67.55000305175781,
        height=57.900001525878906
    )

    canvas.create_rectangle(
        33.7750244140625,
        91.675048828125,
        916.75,
        496.97503662109375,
        fill="#6CD4A8",
        outline="")

    canvas.create_text(
        261.0,
        259.0,
        anchor="nw",
        text="Le tocó a usted profesor",
        fill="#FFFFFF",
        font=("MontserratAlternates Bold", 36 * -1)
    )


    window.resizable(False, False)
    window.mainloop()
