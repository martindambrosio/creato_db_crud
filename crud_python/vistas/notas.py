import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from .claseg import Frame
from controlador.notas_dao import leer_notas, guardar_notas, editar_notas


def open_vista_notas(root):
    vista_notas = tk.Toplevel(root)
    vista_notas.title('Gestor Escuela de Artes "Creato" - Notas de Alumnos')
    vista_notas.iconbitmap('img/iconescuela.ico')
    vista_notas.resizable(0,0)

    app = Frame10(root = vista_notas)
    app.config(background='#FFC0CB')


class Frame10(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.id_nt = None

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.tabla_nota()

    def label_form(self):

        self.label_id_de_curso = tk.Label(self, text="ID Curso:")
        self.label_id_de_curso.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_id_de_curso.grid(row= 1, column=0,padx=10,pady=10)

        self.label_id_de_alumno = tk.Label(self, text="ID Alumno:")
        self.label_id_de_alumno.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_id_de_alumno.grid(row= 1, column=3,padx=10,pady=10)

        self.label_tipo_de_examen = tk.Label(self, text="Tipo de examen:")
        self.label_tipo_de_examen.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_tipo_de_examen.grid(row= 2, column=0,padx=10,pady=10)

        self.label_fecha = tk.Label(self, text="Fecha:")
        self.label_fecha.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_fecha.grid(row= 2, column=3,padx=10,pady=10)

        self.label_nota = tk.Label(self, text="Nota:")
        self.label_nota.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_nota.grid(row= 3, column=0,padx=10,pady=10)

        self.label_observaciones = tk.Label(self, text="Observaciones:")
        self.label_observaciones.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_observaciones.grid(row= 4, column=0,padx=10,pady=10)

    def input_form(self):

        self.id_de_curso_c = tk.StringVar()
        self.entry_id_de_curso= tk.Entry(self,textvariable=self.id_de_curso_c)
        self.entry_id_de_curso.config(width=20, font=('Arial',12),state='disabled')
        self.entry_id_de_curso.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')

        self.id_de_alumno_c = tk.StringVar()
        self.entry_id_de_alumno = tk.Entry(self,textvariable=self.id_de_alumno_c)
        self.entry_id_de_alumno.config(width=20, font=('Arial',12),state='disabled')
        self.entry_id_de_alumno.grid(row= 1, column=4,padx=10,pady=10, columnspan='2')

        y = ["Parcial","Final"]
        self.tipo_n = ['Seleccione uno'] + y

        self.entry_tipo_de_examen = ttk.Combobox(self, state="readonly")
        self.entry_tipo_de_examen['values'] = self.tipo_n
        self.entry_tipo_de_examen.current(0)
        self.entry_tipo_de_examen.config(width=15, state='disabled',font=('Arial',12))
        self.entry_tipo_de_examen.bind("<<ComboboxSelected>>")
        self.entry_tipo_de_examen.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.fecha_c = tk.StringVar()
        self.entry_fecha = tk.Entry(self,textvariable=self.fecha_c)
        self.entry_fecha.config(width=25, font=('Arial',12),state='disabled')
        self.entry_fecha.grid(row= 2, column=4,padx=10,pady=10, columnspan='3')

        self.nota_c = tk.StringVar()
        self.entry_nota = tk.Entry(self,textvariable=self.nota_c)
        self.entry_nota.config(width=15, font=('Arial',12),state='disabled')
        self.entry_nota.grid(row= 3, column=1,padx=10,pady=10, columnspan='2')

        self.observaciones_c = tk.StringVar()
        self.entry_observaciones = tk.Entry(self,textvariable=self.observaciones_c)
        self.entry_observaciones.config(width=50, font=('Arial',12),state='disabled')
        self.entry_observaciones.grid(row= 4, column=1,padx=10,pady=10, columnspan='6')
    
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
        self.entry_id_de_curso.config(state='normal')
        self.entry_id_de_alumno.config(state='normal')
        self.entry_fecha.config(state='normal')
        self.entry_observaciones.config(state='normal')
        self.entry_nota.config(state='normal')
        self.entry_tipo_de_examen.config(state="readonly")
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_id_de_curso.config(state='disabled')
        self.entry_id_de_alumno.config(state='disabled')
        self.entry_tipo_de_examen.current(0)
        self.entry_tipo_de_examen.config(state="disabled")
        self.entry_fecha.config(state='disabled')
        self.entry_nota.config(state='disabled')
        self.entry_observaciones.config(state='disabled')

        self.nota_c.set('')
        self.observaciones_c.set('')
        self.fecha_c.set('')
        self.entry_tipo_de_examen.current(0)
        self.id_de_alumno_c.set('')
        self.id_de_curso_c.set('')

        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')


    def tabla_nota(self):
        self.tabla = ttk.Treeview(self, columns=('ID curso','ID alumno','Tipo de Examen','Fecha','Nota','Observaciones'))
        self.tabla.grid(row=6,column=0,columnspan=6,sticky='nse')

        self.scroll = tk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=6,sticky='nse')
        self.tabla.configure(yscrollcommand= self.scroll.set)
        
        self.contenido_t = leer_notas('notas')
        self.contenido_t.reverse()
        for p in self.contenido_t:
            self.tabla.insert('',0,text=p['id_nota'],
                              values = (p['id_curso'],p['id_alumno'],p['tipo_examen'],p['fecha'],p['nota'],p['observaciones']))

        self.tabla.heading('#0',text='ID nota')
        self.tabla.heading('#1',text='ID curso')
        self.tabla.heading('#2',text='ID alumno')
        self.tabla.heading('#3',text='Tipo de examen')
        self.tabla.heading('#4',text='Fecha')
        self.tabla.heading('#5',text='Nota')
        self.tabla.heading('#6',text='Observaciones')

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

    def editar_registro(self):
        try:
            self.id_nt = self.tabla.item(self.tabla.selection())['text']
            self.nota = self.tabla.item(self.tabla.selection())['values'][4]
            self.id_c = self.tabla.item(self.tabla.selection())['values'][0]
            self.id_a = self.tabla.item(self.tabla.selection())['values'][1]
            self.obv = self.tabla.item(self.tabla.selection())['values'][5]
            self.fech = self.tabla.item(self.tabla.selection())['values'][3]
            self.tipo = self.tabla.item(self.tabla.selection())['values'][2]

            self.habilitar_campos()
            self.nota_c.set(self.nota)
            self.observaciones_c.set(self.obv)
            self.fecha_c.set(self.fech)
            self.entry_tipo_de_examen.current(1 if self.tipo == 'Compra' else 2)
            self.id_de_alumno_c.set(self.id_a)
            self.id_de_curso_c.set(self.id_c)

        except Exception as e:
            messagebox.showerror("Error", f"{e}")

    def guardar_campos(self):
            nota = {
            "id_nota": '',
            "id_curso": self.id_de_curso_c.get(),
            "id_alumno": self.id_de_alumno_c.get(),
            "tipo_examen": self.entry_tipo_de_examen.get(),
            "fecha":  self.fecha_c.get(),
            "nota": self.nota_c.get(),
            "observaciones": self.observaciones_c.get()
        }

            if self.id_nt == None:
                guardar_notas(nota,'notas')
            else:
                editar_notas(nota,'notas', int(self.id_nt))

            self.id_nt = None
            self.tabla_nota()
            self.bloquear_campos()
        