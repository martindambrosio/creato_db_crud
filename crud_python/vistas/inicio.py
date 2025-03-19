import tkinter as tk
from tkinter import ttk

from .alumno import open_vista_alumno
from .cursos import open_vista_cursos
from .notas import open_vista_notas
from .licencia import open_vista_licencia
from .creador import open_vista_creador
from .claseg import Frame


def barra_menu(root):
    barra = tk.Menu(root)
    root.config(menu = barra, width = 300 , height = 300)
    menu_inicio = tk.Menu(barra, tearoff=0)
    menu_acerca = tk.Menu(barra, tearoff=0)

    #  niveles  #

    #principal

    barra.add_cascade(label='Inicio', menu = menu_inicio)
    barra.add_cascade(label='Acerca de..', menu = menu_acerca)

    #submenu
    menu_inicio.add_command(label='Editor Alumnos', command = lambda: open_vista_alumno(root))
    menu_inicio.add_command(label='Editor Cursos', command = lambda: open_vista_cursos(root))
    menu_inicio.add_command(label='Editor Notas', command = lambda: open_vista_notas(root))
    menu_inicio.add_command(label='Salir', command= root.destroy)

    menu_acerca.add_command(label='Licencia', command = lambda: open_vista_licencia(root))
    menu_acerca.add_command(label='Creador', command = lambda: open_vista_creador(root))

class Frame2(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()

        self.label_principal()
        self.botonera_principal(root)

    def label_principal(self):
        self.label_titulo = tk.Label(self, text="Sistema de Gestion - Escuela de Artes",background="#FFC0CB")
        self.label_titulo.config(font=('Arial',15,'bold'))
        self.label_titulo.grid(row= 1, column=0,padx=10,pady=10, columnspan=4)

        self.label_version = tk.Label(self, text="V1.0 ", background="#FFC0CB")
        self.label_version.config(font=('Arial',8,'bold'))
        self.label_version.grid(row= 3, column=2,padx=10,pady=10)
    
    def botonera_principal(self,root):
        self.btn_alumno = tk.Button(self, text='Alumnos', command=lambda: open_vista_alumno(root))
        self.btn_alumno.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#C8A2C8',cursor='hand2',activebackground='#8D3DAF',activeforeground='#000000')
        self.btn_alumno.grid(row= 2, column=0,padx=10,pady=10)

        self.btn_cursos = tk.Button(self, text='Cursos', command=lambda: open_vista_cursos(root))
        self.btn_cursos.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#C8A2C8',cursor='hand2',activebackground='#8D3DAF',activeforeground='#000000')
        self.btn_cursos.grid(row= 2, column=2,padx=10,pady=10)

        self.btn_notas = tk.Button(self, text='Notas', command=lambda: open_vista_notas(root))
        self.btn_notas.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#C8A2C8',cursor='hand2',activebackground='#8D3DAF',activeforeground='#000000')
        self.btn_notas.grid(row= 3, column=0,padx=10,pady=10)
