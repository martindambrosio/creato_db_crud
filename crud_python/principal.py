import tkinter as tk
from vistas.inicio import Frame2, barra_menu

def main():
    ventana = tk.Tk()
    ventana.title('Gestor Escuela de Artes "Creato" - Inicio')
    ventana.iconbitmap('img/iconescuela.ico')
    ventana.resizable(0,0)

    barra_menu(ventana)
    app = Frame2(root = ventana)
    app.config(background='#FFC0CB')
    ventana.mainloop()

if __name__ == '__main__':
    main()