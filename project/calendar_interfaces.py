'''
    UI for Calendar Event Manager

    Repo actualizado en el siguiente link:
    https://github.com/lucaslucyk/python-course

'''

import sys, calendar_events as ce, tkinter as tk, datetime as dt
from tkinter import ttk, messagebox
from tkcalendar import Calendar

class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", exit)

        self.root.withdraw()# hide naff extra window
        self.root.title('Calendario Personal')

        self.top = tk.Toplevel(self.root)
        self.top.protocol("WM_DELETE_WINDOW", exit)

        self.cal = Calendar(self.top,
                   font="Arial 10", background='darkblue',
                   foreground='white', selectmode='day')

        self.cal.grid()
        ttk.Button(
            self.top, text="Ver eventos", 
            command=lambda: ListView(
                root = self.root,
                day = self.cal.get_date()
            )).grid(sticky="ew", pady=5, padx=5)
        
        ttk.Button(
            self.top, text="Nuevo evento", 
            command=lambda: EventoForm(
                self.root,
            )).grid(sticky="ew", pady=5, padx=5)

        self.root.mainloop()

    def exit():
        #close db connection
        ce.close_conn(ce.DB_CONN)
        
        #close calendar window
        self.top.quit()
        self.top.destroy()

        #close root window
        self.root.quit()
        self.root.destroy()

        #close interpreter
        sys.exit()

    def print_sel(self):
        selected_date = (self.cal.get_date())
        print(selected_date)

class EventoForm:

    def __init__(self, root, evento=None, *args, **kwargs):
        self.root = root
        self.window = tk.Toplevel(root)
        self.evento = evento

        ### labels ###
        labels = [("Título", 0), ("Asistentes", 2), ("Inicio", 4), ("Fin", 5), ("Ubicación", 6), ("Descrip", 8)]

        for k, v in labels:
            lbl = ttk.Label(self.window, text=k, width=10)
            lbl.grid(row=v, column=0, sticky="w", pady=5, padx=5)

        self.pk_lbl = ttk.Label(self.window, text=self.evento, width=10)
        self.pk_lbl.grid(row=0, column=5, sticky="ew", pady=5, padx=5)

        ### entries ###
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

        ### actions ###
        self.scroll = ttk.Scrollbar(self.window)
        self.scroll.grid(row=1, column=4, rowspan=3, sticky="ew", pady=5, padx=5)
        self.asistentes.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.asistentes.yview)

        self.scroll_desc = ttk.Scrollbar(self.window)
        self.scroll_desc.grid(row=7, column=4, rowspan=3, sticky="ew", pady=5, padx=5)
        self.descripcion.configure(yscrollcommand=self.scroll_desc.set)
        self.scroll_desc.configure(command=self.descripcion.yview)

        self.btn_add_ass = ttk.Button(self.window, text="Agregar", command=lambda: AsistenteForm(listbox=self.asistentes, root=self.window))
        self.btn_add_ass.grid(row=1, column=5, sticky="ew", pady=5, padx=5)

        self.btn_del_ass = ttk.Button(self.window, text="Eliminar", command=lambda: self.asistentes.delete(self.asistentes.curselection()))
        self.btn_del_ass.grid(row=2, column=5,  sticky="ew", pady=5, padx=5)

        self.btn_clean_desc = ttk.Button(self.window, text="Limpiar", command=lambda: self.descripcion.delete(1.0, tk.END))
        self.btn_clean_desc.grid(row=8, column=5,  sticky="ew", pady=5, padx=5)

        self.btn_cancel = ttk.Button(self.window, text="Cancelar", command=self.close_window)
        self.btn_cancel.grid(row=10, column=3, columnspan=1, sticky="ew", pady=5, padx=5)

        self.btn_save = ttk.Button(self.window, text="Guardar", command=self.save_event)
        self.btn_save.grid(row=10, column=1, columnspan=2, sticky="ew", pady=5, padx=5)

        self.set_values()

    def close_window(self):
        self.window.destroy()

    def set_values(self, *args, **kwargs):
        if self.evento:
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
            now = dt.datetime.now()
            self.inicio_dia.insert(0, now.strftime("%Y-%m-%d"))
            self.inicio_hora.insert(0, now.strftime("%H:%M"))
            self.fin_dia.insert(0, now.strftime("%Y-%m-%d"))
            self.fin_hora.insert(0, now.strftime("%H:%M"))
        

    def save_event(self):
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

    def __init__(self, listbox, root):
        self.root = root
        self.listbox = listbox
        self.window = tk.Toplevel(root)

        ### labels ###
        self.lbl_mail = ttk.Label(self.window, text="E-mail", width=10)
        self.lbl_mail.grid(row=0, column=0, sticky="w", pady=5, padx=5)

        ### entries ###
        self.mail = ttk.Entry(self.window, textvariable=tk.StringVar(), width=30)
        self.mail.grid(row=0, column=1, columnspan=2, sticky="w", pady=5, padx=5)

        ### actions ###
        self.btn_save = ttk.Button(self.window, text="Insertar", command=self.insert_asistente)
        self.btn_save.grid(row=1, column=1, sticky="ew", pady=5, padx=5)

        self.btn_cancel = ttk.Button(self.window, text="Cancelar", command=self.close_window)
        self.btn_cancel.grid(row=1, column=2, sticky="ew", pady=5, padx=5)

    def insert_asistente(self):
        if self.mail.get() in self.listbox.get(0, tk.END):
            messagebox.showinfo("Info!", "El participante ya se encuentra en la lista")
            return

        self.listbox.insert(0, self.mail.get())
        self.close_window()

    def close_window(self):
        self.window.destroy()

class ListView:
    def __init__(self, root, day, *args, **kwargs):
        self.root = root
        self.window = tk.Toplevel(root)

        ### entries ###
        self.eventos = tk.Listbox(self.window, height=6, width=60)
        self.eventos.grid(row=0, column=0, rowspan=3, columnspan=3, sticky="w", pady=5, padx=5)

        ### actions ###
        self.scroll = ttk.Scrollbar(self.window)
        self.scroll.grid(row=0, column=4, rowspan=3, sticky="ew", pady=5, padx=5)

        self.eventos.configure(yscrollcommand=self.scroll.set)
        self.scroll.configure(command=self.eventos.yview)

        self.btn_cancel = ttk.Button(self.window, text="Salir", command=self.close_window)
        self.btn_cancel.grid(row=10, column=2, columnspan=2, sticky="ew", pady=5, padx=5)

        self.btn_detail = ttk.Button(self.window, text="Detalle", command=self.event_detail)
        self.btn_detail.grid(row=10, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

        self.day_events = ce.Evento.day_events(day=dt.datetime.strptime(day, "%x"))
        self.insert_events()

    def close_window(self):
        self.window.destroy()

    def insert_events(self):
        self.eventos.delete(0, tk.END)

        for event in self.day_events:
            #print(self.day_events.index(event))
            self.eventos.insert(self.day_events.index(event), str(event.pk) + " | " + str(event))
        
    def event_detail(self):
        if self.eventos.curselection():
            pk = self.eventos.get(self.eventos.curselection()).split(" | ")[0]
            EventoForm(root=self.root, evento=pk)
        else:
            messagebox.showerror("Error", "Debe seleccionar un evento.")
    