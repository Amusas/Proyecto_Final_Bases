
#comando para instalar la libreria: pip install customtkinter
#se instalan ambas
import customtkinter as ctk
import tkinter

#eventos de botones y funciones
def iniciar_sesion():
    nombre_usuario = nombre_usuario_input.get()
    contrasenia = contrasena_input.get()
    """ACA debe estar el llamado a un controlador para validar los datos"""


#Creacion de la ventana principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.geometry("480x600")
app.title("login")
app.resizable(False, False)

#Creacion de la seccion donde iran los elementos
frame = ctk.CTkFrame(master=app, width=360, height=400, corner_radius=30)
frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)

#creacion de los labels, inputs y buttons
label1 = ctk.CTkLabel(master=frame,text="Ingresa con tu cuenta", font=("Century gothic", 23))
label1.place(x=50,y=60)

nombre_usuario_input = ctk.CTkEntry(master=frame, width=260, placeholder_text="nombre de usuario")
nombre_usuario_input.place(x=50, y=130)

contrasena_input = ctk.CTkEntry(master=frame, width=260, placeholder_text="contraseña", show="•")
contrasena_input.place(x=50, y=190)

boton_login = ctk.CTkButton(master=frame, width=260, text="Iniciar Sesion", corner_radius=10, command=iniciar_sesion)
boton_login.place(x=50, y = 250)

app.mainloop()
