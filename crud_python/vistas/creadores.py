import tkinter as tk
from vistas.claseg import Frame


def open_vista_creador(root):
    vista_creador = tk.Toplevel(root)
    vista_creador.title('Gestor Escuela de Artes "Creato" - Creador')
    vista_creador.iconbitmap('img/iconescuela.ico')
    vista_creador.resizable(0,0)

    app = Frame6(root = vista_creador)


class Frame6(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.ver_creador()

    def ver_creador(self):
        self.label_titulo_creador= tk.Label(self,text= 'Creador')
        self.label_titulo_creador.config(font=('Arial',20,'bold'))
        self.label_titulo_creador.grid(row= 0, column=3,padx=10,pady=10)

        self.label_titulo_creador2= tk.Label(self,text= 'Nombre')
        self.label_titulo_creador2.config(font=('Arial',15,'bold'))
        self.label_titulo_creador2.grid(row= 1, column=2,padx=10,pady=10)

        self.label_titulo_creador3= tk.Label(self,text= 'Contacto')
        self.label_titulo_creador3.config(font=('Arial',15,'bold'))
        self.label_titulo_creador3.grid(row= 1, column=4,padx=10,pady=10)

        self.label_name_creador= tk.Label(self,text= 'Martín D Ambrosio',fg="#FF5733")
        self.label_name_creador.config(font=('Arial',12,'bold'))
        self.label_name_creador.grid(row= 2, column=2,padx=10,pady=10)


        self.label_correo_creador= tk.Label(self,text= 'martingermandambrosio@gmail.com',fg="#FF5733")
        self.label_correo_creador.config(font=('Arial',12,'bold'))
        self.label_correo_creador.grid(row= 2, column=4,padx=10,pady=10)