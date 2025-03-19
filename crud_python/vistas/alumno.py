import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from .claseg import Frame
from controlador.alumno_dao import leer_alumno, guardar_alumno, editar_alumno, eliminar_alumno, buscar_alumno


def open_vista_alumno(root):
    vista_alumno = tk.Toplevel(root)
    vista_alumno.title('Gestor Escuela de Artes "Creato" - Alumnos')
    vista_alumno.iconbitmap('img/iconescuela.ico')
    vista_alumno.resizable(0,0)

    app = Frame3(root = vista_alumno)
    app.config(background='#FFC0CB')


class Frame3(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.id_alu = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.tabla_alumno()

    def label_form(self):
        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_nombre.grid(row= 1, column=0,padx=10,pady=10)

        self.label_apellido = tk.Label(self, text="Apellido:")
        self.label_apellido.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_apellido.grid(row= 1, column=3,padx=10,pady=10)

        self.label_documento = tk.Label(self, text="Documento:")
        self.label_documento.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_documento.grid(row= 2, column=0,padx=10,pady=10)

        self.label_telefono = tk.Label(self, text="Telefono:")
        self.label_telefono.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_telefono.grid(row= 2, column=3,padx=10,pady=10)

        self.label_direccion = tk.Label(self, text="Dirección:")
        self.label_direccion.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_direccion.grid(row= 3, column=0,padx=10,pady=10)

        self.label_correo = tk.Label(self, text="Mail:")
        self.label_correo.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_correo.grid(row= 4, column=0,padx=10,pady=10)

    def input_form(self):
        self.nombre_a = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.nombre_a)
        self.entry_nombre.config(width=20, font=('Arial',12),state='disabled')
        self.entry_nombre.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')

        self.apellido_a = tk.StringVar()
        self.entry_apellido = tk.Entry(self,textvariable=self.apellido_a)
        self.entry_apellido.config(width=20, font=('Arial',12),state='disabled')
        self.entry_apellido.grid(row= 1, column=4,padx=10,pady=10, columnspan='2')

        self.documento_a = tk.StringVar()
        self.entry_documento = tk.Entry(self,textvariable=self.documento_a)
        self.entry_documento.config(width=20, font=('Arial',12),state='disabled')
        self.entry_documento.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.telefono_a = tk.StringVar()
        self.entry_telefono = tk.Entry(self,textvariable=self.telefono_a)
        self.entry_telefono.config(width=20, font=('Arial',12),state='disabled')
        self.entry_telefono.grid(row= 2, column=4,padx=10,pady=10, columnspan='2')

        self.direccion_a = tk.StringVar()
        self.entry_direccion = tk.Entry(self,textvariable=self.direccion_a)
        self.entry_direccion.config(width=25, font=('Arial',12),state='disabled')
        self.entry_direccion.grid(row= 3, column=1,padx=10,pady=10, columnspan='4')

        self.correo_a = tk.StringVar()
        self.entry_correo = tk.Entry(self,textvariable=self.correo_a)
        self.entry_correo.config(width=50, font=('Arial',12),state='disabled')
        self.entry_correo.grid(row= 4, column=1,padx=10,pady=10, columnspan='6')
    
    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo',command= self.habilitar_campos)
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#28A745',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_alta.grid(row= 5, column=0,padx=10,pady=10, columnspan='2')

        self.btn_modi = tk.Button(self, text='Guardar',command= self.guardar_campos)
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#007BFF',cursor='hand2',activebackground='#7594F5',activeforeground='#000000',state='disabled')
        self.btn_modi.grid(row= 5, column=2,padx=10,pady=10, columnspan='2')

        self.btn_cance = tk.Button(self, text='Cancelar', command= self.bloquear_campos)
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#DC3545',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000',state='disabled')
        self.btn_cance.grid(row= 5, column=4,padx=10,pady=10, columnspan='2')

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_apellido.config(state='normal')
        self.entry_documento.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_direccion.config(state='normal')
        self.entry_correo.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_apellido.config(state='disabled')
        self.entry_documento.config(state='disabled')
        self.entry_telefono.config(state='disabled')
        self.entry_direccion.config(state='disabled')
        self.entry_correo.config(state='disabled')

        self.nombre_a.set('')
        self.apellido_a.set('')
        self.documento_a.set('')
        self.direccion_a.set('')
        self.telefono_a.set('')
        self.correo_a.set('')

        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')

    def tabla_alumno(self):

        self.contenido_alu = leer_alumno('alumnos')
        self.contenido_alu.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre','Apellido','Documento','Direccion','Telefono','Mail'))
        self.tabla.grid(row=6,column=0,columnspan=6,sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=6,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        for p in self.contenido_alu:
            self.tabla.insert('',0,text=p['id_alumno'],
                              values = (p['nombre'],p['apellido'],p['documento'],p['direccion'],p['telefono'],p['mail']))

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Apellido')
        self.tabla.heading('#3',text='Documento')
        self.tabla.heading('#4',text='Direccion')
        self.tabla.heading('#5',text='Telefono')
        self.tabla.heading('#6',text='Mail')

        self.tabla.column('#0', width=50)
        self.tabla.column('#1', width=100)
        self.tabla.column('#2', width=100)
        self.tabla.column('#3', width=80)
        self.tabla.column('#4', width=120)
        self.tabla.column('#5', width=80)
        self.tabla.column('#6', width=150)

        self.btn_editar = tk.Button(self, text='Editar', command= self.editar_registro)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#FFC107',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar.grid(row= 7, column=0,padx=10,pady=10, columnspan=2)

        self.btn_delete = tk.Button(self, text='Borrar', command= self.borrar_alumno)
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#C82333',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete.grid(row= 7, column=2,padx=10,pady=10, columnspan=2)

        self.buscar_a = tk.StringVar()
        self.buscar_a.set("example@example.com")
        self.entry_buscar = tk.Entry(self,textvariable=self.buscar_a)
        self.entry_buscar.config(width=30, font=('Arial',12))
        self.entry_buscar.grid(row= 7, column=4,padx=10,pady=10, columnspan='2')
        self.entry_buscar.bind("<FocusIn>", lambda e: self.buscar_a.set(""))

        self.btn_buscar = tk.Button(self, text='Buscar', command= self.buscar_registro)
        self.btn_buscar.config(width= 10,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#343A40',cursor='hand2',activebackground='#C6C6C0',activeforeground='#FFFFFF')
        self.btn_buscar.grid(row= 7, column=7,padx=10,pady=10)


    def editar_registro(self):
        try:
            self.id_alu = self.tabla.item(self.tabla.selection())['text']

            self.nombre_alumno = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellido_alumno = self.tabla.item(self.tabla.selection())['values'][1]
            self.doc_alumno = self.tabla.item(self.tabla.selection())['values'][2]
            self.dir_alumno = self.tabla.item(self.tabla.selection())['values'][3]
            self.mail_alumno = self.tabla.item(self.tabla.selection())['values'][5]
            self.tel_alumno = self.tabla.item(self.tabla.selection())['values'][4]

            self.habilitar_campos()
            self.nombre_a.set(self.nombre_alumno)
            self.apellido_a.set(self.apellido_alumno)
            self.documento_a.set(self.doc_alumno)
            self.direccion_a.set(self.dir_alumno)
            self.telefono_a.set(self.tel_alumno)
            self.correo_a.set(self.mail_alumno)

        except Exception as e:
            messagebox.showerror("Error", f"{e}")

    def guardar_campos(self):
        persona = {
        "id_alumno": '',
        "nombre": self.nombre_a.get(),
        "apellido": self.apellido_a.get(),
        "documento": self.documento_a.get(),
        "direccion":  self.direccion_a.get(),
        "telefono": self.telefono_a.get(),
        "mail": self.correo_a.get()
    }

        if self.id_alu == None:
            guardar_alumno(persona,'alumnos')
        else:
            editar_alumno(persona,'alumnos', int(self.id_alu))

        self.id_alu = None
        self.tabla_alumno()
        self.bloquear_campos()
    
    def borrar_alumno(self):
        try:
            response = messagebox.askyesno("Confirmar acción", "¿Desea eliminar al Alumno?")
            if response:
                eliminar_alumno('alumnos', int(self.tabla.item(self.tabla.selection())['text']))
                self.tabla_alumno()
        except Exception as e:
            messagebox.showerror("Error", f"{e}")
    
    def buscar_registro(self):
        persona = buscar_alumno('alumnos',self.buscar_a.get())

        
        if persona != None:
            self.habilitar_campos()
            self.nombre_a.set(persona['nombre'])
            self.apellido_a.set(persona['apellido'])
            self.documento_a.set(persona['documento'])
            self.direccion_a.set(persona['direccion'])
            self.telefono_a.set(persona['telefono'])
            self.correo_a.set(persona['mail'])

            self.id_cli = persona['id_alumno']

            self.buscar_a.set('')
        else:
            messagebox.showerror("Error", f"El correo {self.buscar_a.get()}. No esta registrado")








