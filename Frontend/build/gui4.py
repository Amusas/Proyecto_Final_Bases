
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\LENOVO\Jeremias\Universidad\6_Semestre\BasesDatos\proyectoFinal\Proyecto_Final_Bases\Frontend\build\assets\frame4")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

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
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=69.96240234375,
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
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=0.0,
    y=0.0,
    width=67.55000305175781,
    height=57.900001525878906
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=813.0,
    y=0.0,
    width=152.1999053955078,
    height=58.0
)

canvas.create_rectangle(
    33.77490234375,
    91.67498779296875,
    916.7498779296875,
    496.9749755859375,
    fill="#6CD4A8",
    outline="")

canvas.create_text(
    103.737548828125,
    308.79998779296875,
    anchor="nw",
    text="Sucursal:",
    fill="#FFFFFF",
    font=("MontserratAlternates Bold", 24 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    534.3687515258789,
    326.89372634887695,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#73F7C0",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=410.125,
    y=303.9749755859375,
    width=248.4875030517578,
    height=43.837501525878906
)

canvas.create_text(
    103.737548828125,
    441.48748779296875,
    anchor="nw",
    text="Fecha de terminación:",
    fill="#FFFFFF",
    font=("MontserratAlternates Bold", 24 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    534.3687515258789,
    455.9624996185303,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#73F7C0",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=410.125,
    y=434.25,
    width=248.4875030517578,
    height=41.42499923706055
)

canvas.create_text(
    103.737548828125,
    373.9375,
    anchor="nw",
    text="Fecha de inicio:",
    fill="#FFFFFF",
    font=("MontserratAlternates Bold", 24 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    534.3687515258789,
    392.0312385559082,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#73F7C0",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=410.125,
    y=369.11248779296875,
    width=248.4875030517578,
    height=43.837501525878906
)

canvas.create_text(
    103.737548828125,
    118.2125244140625,
    anchor="nw",
    text="Código:",
    fill="#FFFFFF",
    font=("MontserratAlternates Bold", 24 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    534.3687515258789,
    132.68747520446777,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#73F7C0",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=410.125,
    y=110.9749755859375,
    width=248.4875030517578,
    height=41.42499923706055
)

canvas.create_text(
    103.737548828125,
    173.70001220703125,
    anchor="nw",
    text="Empleado",
    fill="#FFFFFF",
    font=("MontserratAlternates Bold", 24 * -1)
)

canvas.create_text(
    103.737548828125,
    246.07501220703125,
    anchor="nw",
    text="Cargo:",
    fill="#FFFFFF",
    font=("MontserratAlternates Bold", 24 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    534.3687515258789,
    264.16875076293945,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#73F7C0",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=410.125,
    y=241.25,
    width=248.4875030517578,
    height=43.837501525878906
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    534.3687515258789,
    199.0312385559082,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#73F7C0",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=410.125,
    y=176.11248779296875,
    width=248.4875030517578,
    height=43.837501525878906
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=697.0,
    y=367.0,
    width=176.1521759033203,
    height=41.21741485595703
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=697.0,
    y=304.0,
    width=176.1521759033203,
    height=41.47827911376953
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=697.0,
    y=178.978271484375,
    width=176.1521759033203,
    height=41.02173614501953
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=699.0,
    y=241.7174072265625,
    width=176.5652618408203,
    height=41.2825927734375
)
window.resizable(False, False)
window.mainloop()
