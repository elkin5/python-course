'''
    Interfaz gráfica para el Gestor de Calendario Personal

    Repo actualizado en el siguiente link:
    https://github.com/lucaslucyk/python-course

'''

### imports ###
import sys, calendar_events as ce, tkinter as tk, datetime as dt
from tkinter import ttk, messagebox
from tkcalendar import Calendar

class App:
    ''' Interfaz básica del módulo tkinter y se agrega el widget tkcalendar.Calendar 
        Más info en https://pypi.org/project/tkcalendar/
    '''

    def __init__(self):
        
        #Interfaz base de tkinter.
        #Más información en https://docs.python.org/3/library/tkinter.html
        self.root = tk.Tk()

        #método que se ejecuta al cerrar la ventana
        self.root.protocol("WM_DELETE_WINDOW", self.exit)

        self.root.withdraw()
        self.root.title('Calendario Personal')

        #Widget para mostrar calendario
        self.top = tk.Toplevel(self.root)
        self.top.protocol("WM_DELETE_WINDOW", self.exit)

        #es necesario instalar el módulo tkcalendar
        #python -m pip install tkcalendar
        #más info en https://pypi.org/project/tkcalendar/
        self.cal = Calendar(self.top,
                   font="Arial 10", background='darkblue',
                   foreground='white', selectmode='day')

        self.cal.grid()

        #Boton para ver registros del día
        ttk.Button(
            self.top, text="Ver eventos", 

            #Como command recibe el nombre de un método, no nos permite pasar argumentos.
            #Para ello, utilizamos lambda, que crea una función anónima.
            #Puede recibir varios parámetros pero puede ejecutar una sola expresión/acción.
            #Más documentación en https://docs.python.org/3/reference/expressions.html#lambda
            command=lambda: ListView(
                root = self.root,
                day = self.cal.get_date()
            )).grid(sticky="ew", pady=5, padx=5)
        
        #Botón para crear un nuevo evento
        ttk.Button(
            self.top, text="Nuevo evento", 
            command=lambda: EventoForm(
                self.root,
            )).grid(sticky="ew", pady=5, padx=5)

        #Loop para mostrar la ventana sin cerrarse
        self.root.mainloop()

    def exit(self):
        """ Cierr conexión a base de datos y todas las interfaces gráficas """

        #Cierra conexión a la base de datos
        ce.close_conn(ce.DB_CONN)
        
        #Cierra ventana de Calendario (widget)
        self.top.quit()
        self.top.destroy()

        #Cierra ventana principal
        self.root.quit()
        self.root.destroy()

        #Cierra el intérprete de Python
        sys.exit()

class ListView:
    ''' Ventana para listar los eventos de un día determinado '''

    def __init__(self, root, day, *args, **kwargs):
        self.root = root
        self.window = tk.Toplevel(root)

        ### Ingresos ###
        self.eventos = tk.Listbox(self.window, height=6, width=80)
        self.eventos.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="w", pady=5, padx=5)

        ### Acciones ###
        self.scroll = ttk.Scrollbar(self.window)
        self.scroll.grid(row=0, column=4, rowspan=3, sticky="ew", pady=5, padx=5)

        self.eventos.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.eventos.yview)

        self.btn_cancel = ttk.Button(self.window, text="Salir", command=self.close_window)
        self.btn_cancel.grid(row=10, column=2, columnspan=2, sticky="ew", pady=5, padx=5)

        self.btn_detail = ttk.Button(self.window, text="Detalle", command=self.event_detail)
        self.btn_detail.grid(row=10, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

        self.day_events = ce.Evento.day_events(day=dt.datetime.strptime(day, "%x"))

        #Una vez creada la ventana, busco y agrego los eventos del día
        self.insert_events()

    def close_window(self):
        ''' Cierra la ventana ListView '''
        self.window.destroy()

    def insert_events(self):
        ''' Limpia el listbox de eventos de la ventana ListView.
            Luego busca y agrega al listbox, todos los eventos para el día especificado.
        '''

        self.eventos.delete(0, tk.END)

        for event in self.day_events:
            self.eventos.insert(self.day_events.index(event), str(event.pk) + " | " + str(event))
        
    def event_detail(self):
        ''' Abre una nueva ventana de tipo EventoForm especificando la pk de un evento
            en base al evento seleccionado en la ventana ListView
        '''

        if self.eventos.curselection():
            pk = self.eventos.get(self.eventos.curselection()).split(" | ")[0]
            EventoForm(root=self.root, evento=pk)
        else:
            messagebox.showerror("Error", "Debe seleccionar un evento.")

class EventoForm:
    ''' Ventana para crear o mostrar detalle de un evento '''

    def __init__(self, root, evento=None, *args, **kwargs):

        #Nueva ventana que pertenece a la principal.
        self.root = root
        self.window = tk.Toplevel(root)

        #Guardamos el evento (pk) como un atributo en caso de que lo recibamos como argumento.
        self.evento = evento

        ### Etiquetas ###
        labels = [("Título", 0), ("Asistentes", 2), ("Inicio", 4), ("Fin", 5), ("Ubicación", 6), ("Descrip", 8)]

        for k, v in labels:
            lbl = ttk.Label(self.window, text=k, width=10)
            lbl.grid(row=v, column=0, sticky="w", pady=5, padx=5)

        #Si crea un lvl del valor recibido como evento (pk)
        #Si es None, no se muestra ningún valor
        self.pk_lbl = ttk.Label(self.window, text=self.evento, width=10)
        self.pk_lbl.grid(row=0, column=5, sticky="ew", pady=5, padx=5)

        ### Ingresos ###
        self.titulo = ttk.Entry(self.window, textvariable=tk.StringVar(), width=50)
        self.titulo.grid(row=0, column=1, columnspan=3, sticky="w", pady=5, padx=5)

        self.asistentes = tk.Listbox(self.window, height=6, width=50)
        self.asistentes.grid(row=1, column=1, rowspan=3, columnspan=3, sticky="w", pady=5, padx=5)

        self.inicio_dia = ttk.Entry(self.window, textvariable=tk.StringVar(), width=32)
        self.inicio_dia.grid(row=4, column=1, columnspan=2, sticky="w", pady=5, padx=5)

        self.inicio_hora = ttk.Entry(self.window, textvariable=tk.StringVar(), width=15)
        self.inicio_hora.grid(row=4, column=3, sticky="w", pady=5, padx=5)

        self.fin_dia = ttk.Entry(self.window, textvariable=tk.StringVar(), width=32)
        self.fin_dia.grid(row=5, column=1, columnspan=2, sticky="w", pady=5, padx=5)

        self.fin_hora = ttk.Entry(self.window, textvariable=tk.StringVar(), width=15)
        self.fin_hora.grid(row=5, column=3, sticky="w", pady=5, padx=5)

        self.ubicacion = ttk.Entry(self.window, textvariable=tk.StringVar(), width=50)
        self.ubicacion.grid(row=6, column=1, columnspan=3, sticky="w", pady=5, padx=5)

        self.descripcion = tk.Text(self.window, height=6, width=30, font="TkDefaultFont")
        self.descripcion.grid(row=7, rowspan=3, column=1, columnspan=3, sticky="ew", pady=5, padx=5)

        ### Acciones ###
        self.scroll = ttk.Scrollbar(self.window)
        self.scroll.grid(row=1, column=4, rowspan=3, sticky="ew", pady=5, padx=5)
        self.asistentes.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.asistentes.yview)

        self.scroll_desc = ttk.Scrollbar(self.window)
        self.scroll_desc.grid(row=7, column=4, rowspan=3, sticky="ew", pady=5, padx=5)
        self.descripcion.configure(yscrollcommand=self.scroll_desc.set)
        self.scroll_desc.configure(command=self.descripcion.yview)

        self.btn_add_asist = ttk.Button(self.window, text="Agregar", command=lambda: AsistenteForm(listbox=self.asistentes, root=self.window))
        self.btn_add_asist.grid(row=1, column=5, sticky="ew", pady=5, padx=5)

        self.btn_del_ass = ttk.Button(self.window, text="Eliminar", command=lambda: self.asistentes.delete(self.asistentes.curselection()))
        self.btn_del_ass.grid(row=2, column=5,  sticky="ew", pady=5, padx=5)

        self.btn_clean_desc = ttk.Button(self.window, text="Limpiar", command=lambda: self.descripcion.delete(1.0, tk.END))
        self.btn_clean_desc.grid(row=8, column=5,  sticky="ew", pady=5, padx=5)

        self.btn_cancel = ttk.Button(self.window, text="Cancelar", command=self.close_window)
        self.btn_cancel.grid(row=10, column=3, columnspan=1, sticky="ew", pady=5, padx=5)

        self.btn_save = ttk.Button(self.window, text="Guardar", command=self.save_event)
        self.btn_save.grid(row=10, column=1, columnspan=2, sticky="ew", pady=5, padx=5)

        #Llamo al método set_values() para imprimir los valores correspondientes en la nueva ventana generada.
        self.set_values()

    def close_window(self):
        ''' Cierra la ventana EventForm '''
        self.window.destroy()

    def set_values(self, *args, **kwargs):
        ''' Si se especificó un evento, imprime sus valores en el formulario, 
            obteniendo los datos con el método de clase "Evento.objects" '''

        if self.evento:
            #Si recibimos la pk del evento, imprimo todos sus datos en el formulario.

            evs = ce.Evento.objects(pk=self.evento)
            ev = evs[0] if evs else None

            if ev:
                self.titulo.insert(0, ev.titulo)
                self.inicio_dia.insert(0, ev.inicio.strftime("%Y-%m-%d"))
                self.inicio_hora.insert(0, ev.inicio.strftime("%H:%M"))
                self.fin_dia.insert(0, ev.fin.strftime("%Y-%m-%d"))
                self.fin_hora.insert(0, ev.fin.strftime("%H:%M"))
                self.ubicacion.insert(0, ev.ubicacion)
                self.descripcion.insert(1.0, ev.descripcion)

                for asist in ev.asistentes:
                    self.asistentes.insert(ev.asistentes.index(asist), asist)
        else:
            #Si no recibimos la pk del evento, imprimimos únicamente las fechas y horas para mostrar formato.

            now = dt.datetime.now()
            self.inicio_dia.insert(0, now.strftime("%Y-%m-%d"))
            self.inicio_hora.insert(0, now.strftime("%H:%M"))
            self.fin_dia.insert(0, now.strftime("%Y-%m-%d"))
            self.fin_hora.insert(0, now.strftime("%H:%M"))
        

    def save_event(self):
        ''' Guarda en la base de datos los datos ingresados en el formulario de EventoForm.
            Los datos pueden ser de un evento que se esté creando o de un evento que se esté editando.

            Una vez guardado el objeto, muestra un aviso y luego cierra el formulario para volver a la vista de Calendario.
        '''

        try:
            ev = ce.Evento(
                pk = self.evento,
                titulo = self.titulo.get(),
                ubicacion = self.ubicacion.get(),
                inicio = " ".join([self.inicio_dia.get(), self.inicio_hora.get()]),
                fin = " ".join([self.fin_dia.get(), self.fin_hora.get()]), 
                descripcion = self.descripcion.get(1.0, tk.END),
                asistentes = list(self.asistentes.get(0, tk.END))
            )
            ev.save()

            messagebox.showinfo("Guardado", "Datos guardados!")
            self.close_window()
        except:
            messagebox.showerror("Error", "Error guardando los datos")

class AsistenteForm:
    ''' Ventana para asignar un nuevo asistente a un evento '''

    def __init__(self, listbox, root):
        self.root = root
        self.listbox = listbox
        self.window = tk.Toplevel(root)

        ### Etiquetas ###
        self.lbl_mail = ttk.Label(self.window, text="E-mail", width=10)
        self.lbl_mail.grid(row=0, column=0, sticky="w", pady=5, padx=5)

        ### Ingresos ###
        self.mail = ttk.Entry(self.window, textvariable=tk.StringVar(), width=30)
        self.mail.grid(row=0, column=1, columnspan=2, sticky="w", pady=5, padx=5)

        ### Acciones ###
        self.btn_save = ttk.Button(self.window, text="Insertar", command=self.insert_asistente)
        self.btn_save.grid(row=1, column=1, sticky="ew", pady=5, padx=5)

        self.btn_cancel = ttk.Button(self.window, text="Cancelar", command=self.close_window)
        self.btn_cancel.grid(row=1, column=2, sticky="ew", pady=5, padx=5)

    def insert_asistente(self):
        ''' Agrega el asistente del formulario al listbox de EventoForm.
            Cierra la ventana una vez agregado el asistente.
        '''

        #Si el asistente ya se encuentra en la lista de asistentes, muestra un mensaje y no cierra la ventana
        if self.mail.get() in self.listbox.get(0, tk.END):
            messagebox.showinfo("Info!", "El participante ya se encuentra en la lista")
            return

        self.listbox.insert(0, self.mail.get())
        self.close_window()

    def close_window(self):
        ''' Cierra la ventana AsistenteForm '''
        self.window.destroy()


