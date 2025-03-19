import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from vistas.claseg import Frame
from controlador.cursos_dao import leer_curso, guardar_curso, editar_curso, eliminar_curso, buscar_curso


def open_vista_cursos(root):
    vista_cursos = tk.Toplevel(root)
    vista_cursos.title('Gestor Escuela de Artes "Creato" - Cursos')
    vista_cursos.iconbitmap('img/iconescuela.ico')
    vista_cursos.resizable(0,0)

    app = Frame4(root = vista_cursos)
    app.config(background='#FFC0CB')

class Frame4(Frame):
    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.id_cur = None

        self.label_form()
        self.input_form()
        self.tabla_cursos()
        self.botones_principales()

    def label_form(self):
        self.label_id_curso = tk.Label(self, text="ID Curso:")
        self.label_id_curso.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_id_curso.grid(row= 1, column=0,padx=10,pady=10)

        self.label_nombre = tk.Label(self, text="Nombre:")
        self.label_nombre.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_nombre.grid(row= 1, column=3,padx=10,pady=10)

        self.label_id_profesor = tk.Label(self, text="ID Profesor:")
        self.label_id_profesor.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_id_profesor.grid(row= 2, column=3,padx=10,pady=10)

        self.label_nivel = tk.Label(self, text="Nivel:")
        self.label_nivel.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_nivel.grid(row= 2, column=0,padx=10,pady=10)

        self.label_turno = tk.Label(self, text="Turno:")
        self.label_turno.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_turno.grid(row= 4, column=0,padx=10,pady=10)

        self.label_dia = tk.Label(self, text="Día:")
        self.label_dia.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_dia.grid(row= 4, column=3,padx=10,pady=10)

        self.label_horario = tk.Label(self, text="Horario:")
        self.label_horario.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_horario.grid(row= 6, column=0,padx=10,pady=10)

        self.label_costo = tk.Label(self, text="Costo:")
        self.label_costo.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_costo.grid(row= 6, column=3,padx=10,pady=10)

        self.label_estado = tk.Label(self, text="Estado:")
        self.label_estado.config(font=('Arial',12,'bold'),background='#FFC0CB')
        self.label_estado.grid(row= 8, column=0,padx=10,pady=10)

        

    def input_form(self):
        self.id_curso_c = tk.StringVar()
        self.entry_id_curso = tk.Entry(self,textvariable=self.id_curso_c)
        self.entry_id_curso.config(width=20, font=('Arial',12),state='disabled')
        self.entry_id_curso.grid(row= 1, column=1,padx=10,pady=10, columnspan='2')

        self.nombre_c = tk.StringVar()
        self.entry_nombre = tk.Entry(self,textvariable=self.nombre_c)
        self.entry_nombre.config(width=20, font=('Arial',12),state='disabled')
        self.entry_nombre.grid(row= 1, column=4,padx=10,pady=10, columnspan='2')
        
        self.id_profesor_c = tk.StringVar()
        self.entry_id_profesor = tk.Entry(self,textvariable=self.id_profesor_c)
        self.entry_id_profesor.config(width=20, font=('Arial',12),state='disabled')
        self.entry_id_profesor.grid(row= 2, column=4,padx=10,pady=10, columnspan='2')

        self.nivel_c = tk.StringVar()
        self.entry_nivel = tk.Entry(self,textvariable=self.nivel_c)
        self.entry_nivel.config(width=20, font=('Arial',12),state='disabled')
        self.entry_nivel.grid(row= 2, column=1,padx=10,pady=10, columnspan='2')

        self.turno_c = tk.StringVar()
        self.entry_turno = tk.Entry(self,textvariable=self.turno_c)
        self.entry_turno.config(width=20, font=('Arial',12),state='disabled')
        self.entry_turno.grid(row= 4, column=1,padx=10,pady=10, columnspan='2')

        self.dia_c = tk.StringVar()
        self.entry_dia = tk.Entry(self,textvariable=self.dia_c)
        self.entry_dia.config(width=20, font=('Arial',12),state='disabled')
        self.entry_dia.grid(row= 4, column=4,padx=10,pady=10, columnspan='4')

        self.horario_c = tk.StringVar()
        self.entry_horario = tk.Entry(self,textvariable=self.horario_c)
        self.entry_horario.config(width=20, font=('Arial',12),state='disabled')
        self.entry_horario.grid(row=6, column=1,padx=10,pady=10, columnspan='2')

        self.costo_c = tk.StringVar()
        self.entry_costo = tk.Entry(self,textvariable=self.costo_c)
        self.entry_costo.config(width=20, font=('Arial',12),state='disabled')
        self.entry_costo.grid(row= 6, column=4,padx=10,pady=10, columnspan='3')

        self.estado_var = tk.StringVar()
        self.entry_estado = ttk.OptionMenu(self, self.estado_var, "Estado", "Activo", "Finalizado", "Pendiente")
        self.entry_estado.grid(row=8, column=1, padx=10, pady=10)
    
    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command= self.habilitar_campos)
        self.btn_alta.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#28A745',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_alta.grid(row=9, column=0, padx=(5, 5), pady=5)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_modi.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#007BFF',cursor='hand2',activebackground='#7594F5',activeforeground='#000000',state='disabled')
        self.btn_modi.grid(row=9, column=2, padx=(5, 5), pady=5)

        self.btn_cance = tk.Button(self, text='Cancelar', command = self.bloquear_campos)
        self.btn_cance.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#DC3545',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000',state='disabled')
        self.btn_cance.grid(row=9, column=4, padx=(5, 5), pady=5)
    
    def habilitar_campos(self):
        self.entry_id_curso.config(state='normal')
        self.entry_nombre.config(state='normal')
        self.entry_id_profesor.config(state='normal')
        self.entry_nivel.config(state='normal')
        self.entry_turno.config(state='normal')
        self.entry_dia.config(state='normal')
        self.entry_horario.config(state='normal')
        self.entry_costo.config(state='normal')
        self.entry_estado.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.id_cur = None
        self.entry_id_curso.config(state='disabled')
        self.entry_nombre.config(state='disabled')
        self.entry_id_profesor.config(state='disabled')
        self.entry_nivel.config(state='disabled')
        self.entry_turno.config(state='disabled')
        self.entry_dia.config(state='disabled')
        self.entry_horario.config(state='disabled')
        self.entry_costo.config(state='disabled')
        self.entry_estado.config(state='disabled')

        self.id_curso_c.set('')
        self.nombre_c.set('')
        self.id_profesor_c.set('')
        self.nivel_c.set('')
        self.turno_c.set('')
        self.dia_c.set('')
        self.horario_c.set('')
        self.costo_c.set('')
        self.estado_var.set('Disponible')

        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')
      

    def tabla_cursos(self):

        self.contenido_cur = leer_curso('cursos')
        self.contenido_cur.reverse()


        self.tabla = ttk.Treeview(self, columns=('ID_curso','Nombre','Id_profesor','Nivel','Turno','Día','Horario', 'Costo', 'Estado'))
        self.tabla.grid(row=10, column=0, columnspan=6, sticky='nsew')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=6, sticky='ns')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        for p in self.contenido_cur:
            self.tabla.insert('',0,text=p['id_curso'],
                                values = (p['id_curso'],p['nombre'],p['id_profesor'],p['nivel'],p['turno'],p['dia'],p['horario'],p['costo'],p['estado']))
        
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='ID Curso')
        self.tabla.heading('#2', text='Nombre')
        self.tabla.heading('#3', text='ID Profesor')
        self.tabla.heading('#4', text='Nivel')
        self.tabla.heading('#5', text='Turno')
        self.tabla.heading('#6', text='Día')
        self.tabla.heading('#7', text='Horario')
        self.tabla.heading('#8', text='Costo')
        self.tabla.heading('#9', text='Estado')

        
        self.tabla.column('#0', minwidth=80, width=100)
        self.tabla.column('#1', minwidth=80, width=100)
        self.tabla.column('#2', minwidth=60, width=80)
        self.tabla.column('#3', minwidth=60, width=80)
        self.tabla.column('#4', minwidth=80, width=100)
        self.tabla.column('#5', minwidth=80, width=100)
        self.tabla.column('#6', minwidth=100, width=110)
        self.tabla.column('#7', minwidth=100, width=110)
        self.tabla.column('#8', minwidth=80, width=90)
        self.tabla.column('#9', minwidth=80, width=90)

        self.btn_editar = tk.Button(self, text='Editar', command= self.editar_registro)
        self.btn_editar.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#FFC107',cursor='hand2',activebackground='#3FD83F',activeforeground='#000000')
        self.btn_editar.grid(row=11, column=0, padx=10, pady=10,)
        

        self.btn_delete = tk.Button(self, text='Borrar', command= self.borrar_cursos )
        self.btn_delete.config(width= 20,font=('Arial', 12,'bold'),fg ='#FFFFFF' , bg='#C82333',cursor='hand2',activebackground='#F35B5B',activeforeground='#000000')
        self.btn_delete.grid(row=11, column=1, padx=10, pady=10)

    def editar_registro(self):
        try:
            selected_item = self.tabla.selection()
            if not selected_item:
                raise Exception("No se ha seleccionado ningún registro")

            self.id_cur = self.tabla.item(selected_item)['text']

            self.id_curso_cur = self.tabla.item(selected_item)['values'][0]
            self.nombre_cur = self.tabla.item(selected_item)['values'][1]
            self.id_profesor_cur = self.tabla.item(selected_item)['values'][2]
            self.nivel_cur = self.tabla.item(selected_item)['values'][3]
            self.turno_cur = self.tabla.item(selected_item)['values'][4]
            self.dia_cur = self.tabla.item(selected_item)['values'][5]
            self.horario_cur = self.tabla.item(selected_item)['values'][6]
            self.costo_cur = self.tabla.item(selected_item)['values'][7]
            self.estado_cur = self.tabla.item(selected_item)['values'][8]

            self.habilitar_campos()
            self.id_curso_c.set(self.id_curso_cur)
            self.nombre_c.set(self.nombre_cur)
            self.id_profesor_c.set(self.id_profesor_cur)
            self.nivel_c.set(self.nivel_cur)
            self.turno_c.set(self.turno_cur)
            self.dia_c.set(self.dia_cur)
            self.horario_c.set(self.horario_cur)
            self.costo_c.set(self.costo_cur)
            self.estado_var.set(self.estado_cur)

        except Exception as e:
            messagebox.showerror("Error", f"Error al editar el curso: {e}")

    def guardar_campos(self):
        curs = {
        "id_curso": '',
        "id_curso": self.id_curso_c.get().upper(),
        "nombre": self.nombre_c.get(),
        "id_profesor": self.id_profesor_c.get(),
        "nivel": self.nivel_c.get(),
        "turno": self.turno_c.get(),
        "dia": self.dia_c.get(),
        "horario": self.horario_c.get(),
        "costo": self.costo_c.get(),
        "estado": self.estado_var.get(),
    }
        if self.id_cur == None:
            guardar_curso(curs, 'cursos')
        else:
            editar_curso(curs, 'cursos', int(self.id_cur))

        self.id_cur = None
        self.tabla_cursos()
        self.bloquear_campos()
    

    def borrar_cursos(self):
        try:
            response = messagebox.askyesno("Confirmar accion", "Desea eliminar un curso?")
            if response:
                eliminar_curso('cursos', int(self.tabla.item(self.tabla.selection())['text']))
                self.tabla_cursos()
        except Exception as e:
            messagebox.showerror("Error", f"Error al eliminar el curso: {e}")








