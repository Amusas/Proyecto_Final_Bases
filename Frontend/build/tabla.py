import tkinter as tk
from tkinter import ttk

def __crear_tabla(root, datos, columnas):
    # Crear el widget Treeview
    tree = ttk.Treeview(root, columns=columnas, show='headings')
    
    # Ajustar el ancho de las columnas
    for i in columnas:
        tree.heading(i, text=i)
        tree.column(i, width=200)


    # Insertar los datos
    for fila in datos:
        tree.insert('', tk.END, values=fila)

    # Empaquetar el Treeview
    tree.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

def crear_tabla(datos, columnas):
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Resultado_Consulta")
    __crear_tabla(root, datos, columnas)


