import tkinter as tk
from vistas.claseg import Frame


def open_vista_licencia(root):
    vista_licencia = tk.Toplevel(root)
    vista_licencia.title('Gestor Escuela de Artes "Creato" - Licencia')
    vista_licencia.iconbitmap('img/iconescuela.ico')
    vista_licencia.resizable(0,0)

    app = Frame5(root = vista_licencia)
    app.config(background='#FFC0CB')

class Frame5(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.ver_licencia()

    def ver_licencia(self):
        self.label_licencia= tk.Label(self,text= '''Sistema CRUD en Python para la Escuela de Artes "Creato"
    Copyright (C) 2024 
                                      
    =======================================
    This program is free software: you can redistribute it 
    and/or modify it under the terms of the GNU General Public 
    License as published by the Free Software Foundation, 
    either version 3 of the License, or (at your option) any 
    later version. This program is distributed in the hope that it will be 
    useful, but WITHOUT ANY WARRANTY; without even the 
    implied warranty of MERCHANTABILITY or FITNESS FOR A 
    PARTICULAR PURPOSE. See the GNU General Public License 
    for more details.
    You should have received a copy of the GNU General Public 
    License along with this program.  
    If not, see <https://www.gnu.org/licenses/>.''', font=('Arial',10,'bold'),background="#FFC0CB").place(x=1,y=1)


