
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\LENOVO\Jeremias\Universidad\6_Semestre\BasesDatos\proyectoFinal\Proyecto_Final_Bases\Frontend\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("965x611")
window.configure(bg = "#BBF3DB")


canvas = Canvas(
    window,
    bg = "#BBF3DB",
    height = 611,
    width = 965,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    965.0,
    611.4974365234375,
    fill="#BCF3DC",
    outline="")

canvas.create_text(
    412.0,
    20.4852294921875,
    anchor="nw",
    text="Menú",
    fill="#A693F1",
    font=("MontaguSlab Bold", 44 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
btnEntidades = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
btnEntidades.place(
    x=204.85430908203125,
    y=111.4852294921875,
    width=556.53173828125,
    height=57.133949279785156
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
btnAyuda = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
btnAyuda.place(
    x=203.0,
    y=442.4852294921875,
    width=557.0616455078125,
    height=57.55206298828125
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
btnUtilidades = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
btnUtilidades.place(
    x=205.0,
    y=362.4852294921875,
    width=556.53173828125,
    height=57.06479263305664
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
btnConsultas = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
btnConsultas.place(
    x=205.0,
    y=281.4852294921875,
    width=556.53173828125,
    height=58.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
btnTransacciones = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
btnTransacciones.place(
    x=205.0,
    y=197.4852294921875,
    width=557.0,
    height=56.81453323364258
)

canvas.create_rectangle(
    141.40102458000183,
    95.50774105219273,
    834.7622243283404,
    99.22882080078125,
    fill="#9F70DA",
    outline="")

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
btnAcerca = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
btnAcerca.place(
    x=203.0,
    y=519.4852294921875,
    width=557.0616455078125,
    height=57.55206298828125
)
window.resizable(False, False)
window.mainloop()