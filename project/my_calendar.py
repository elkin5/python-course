'''
    UI for Calendar Event Manager

    Repo actualizado en el siguiente link:
    https://github.com/lucaslucyk/python-course

'''

import calendar_events as ce, tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar

def save_event(topObj, **kwargs):
    [print(f'{k}:{v}') for k,v in kwargs.items()]
    messagebox.showinfo("Guardado", "Datos guardados!")

    close_top(topObj)

def close_top(topObj):
    topObj.destroy()

def insert_asistente(mail, listbox, topToClose):
    listbox.insert(0, mail)
    close_top(topToClose)

def asistente_form(asistentesBox, **kwargs):
    asist_window = tk.Toplevel(kwargs.get("window"))

    lbl_mail = ttk.Label(asist_window, text="E-mail", width=10)
    lbl_mail.grid(row=0, column=0, sticky="w", pady=5, padx=5)

    mail_text = tk.StringVar()
    entry_mail = ttk.Entry(asist_window, textvariable=mail_text, width=30)
    entry_mail.grid(row=0, column=1, columnspan=2, sticky="w", pady=5, padx=5)

    #buttons
    btn_save = ttk.Button(asist_window, text="Insertar", command=lambda: insert_asistente(entry_mail.get(), asistentesBox, asist_window))
    btn_save.grid(row=1, column=1, sticky="ew", pady=5, padx=5)

    btn_cancel = ttk.Button(asist_window, text="Cancelar", command=lambda: close_top(asist_window))
    btn_cancel.grid(row=1, column=2, sticky="ew", pady=5, padx=5)

def event_form(**kwargs):
    event_window = tk.Toplevel(ROOT)

    #labels
    labels = [("Título", 0), ("Asistentes", 2), ("Inicio", 4), ("Fin", 5), ("Ubicación", 6)]

    for k, v in labels:
        lbl = ttk.Label(event_window, text=k, width=10)
        lbl.grid(row=v, column=0, sticky="w", pady=5, padx=5)

    #inputs
    #titulo_text = tk.StringVar()
    entry_titulo = ttk.Entry(event_window, textvariable=tk.StringVar(), width=50)
    entry_titulo.grid(row=0, column=1, columnspan=3, sticky="w", pady=5, padx=5)

    scroll = ttk.Scrollbar(event_window)
    scroll.grid(row=1, column=4, rowspan=3, sticky="w", pady=5, padx=5)

    asistentes = tk.Listbox(event_window, height=6, width=50)
    asistentes.grid(row=1, column=1, rowspan=3, columnspan=3, sticky="w", pady=5, padx=5)

    asistentes.configure(yscrollcommand=scroll.set)
    scroll.configure(command=asistentes.yview)

    #inicio_date = tk.StringVar()
    entry_inicio_date = ttk.Entry(event_window, textvariable=tk.StringVar(), width=32)
    entry_inicio_date.grid(row=4, column=1, columnspan=2, sticky="w", pady=5, padx=5)

    #inicio_hour = tk.StringVar()
    entry_inicio_hour = ttk.Entry(event_window, textvariable=tk.StringVar(), width=15)
    entry_inicio_hour.grid(row=4, column=3, sticky="w", pady=5, padx=5)

    #fin_date = tk.StringVar()
    entry_fin_date = ttk.Entry(event_window, textvariable=tk.StringVar(), width=32)
    entry_fin_date.grid(row=5, column=1, columnspan=2, sticky="w", pady=5, padx=5)

    #fin_hour = tk.StringVar()
    entry_fin_hour = ttk.Entry(event_window, textvariable=tk.StringVar(), width=15)
    entry_fin_hour.grid(row=5, column=3, sticky="w", pady=5, padx=5)

    #ubicacion_text = tk.StringVar()
    entry_ubicacion = ttk.Entry(event_window, textvariable=tk.StringVar(), width=50)
    entry_ubicacion.grid(row=6, column=1, columnspan=3, sticky="w", pady=5, padx=5)

    #buttons

    btn_add_ass = ttk.Button(event_window, text="Agregar", command=lambda: asistente_form(asistentes, window=event_window))
    btn_add_ass.grid(row=1, column=5, sticky="ew", pady=5, padx=5)

    btn_del_ass = ttk.Button(event_window, text="Eliminar", command=lambda: asistentes.delete(asistentes.curselection()))
    btn_del_ass.grid(row=2, column=5,  sticky="ew", pady=5, padx=5)

    btn_cancel = ttk.Button(event_window, text="Cancelar", command=lambda: close_top(event_window))
    btn_cancel.grid(row=7, column=3, columnspan=1, sticky="ew", pady=5, padx=5)

    btn_save = ttk.Button(
        event_window, 
        text="Guardar", 
        command=lambda: save_event(
            topObj = event_window,
            titulo = entry_titulo.get(),
            asistentes = asistentes.get(0, tk.END),
            fecha_inicio = entry_inicio_date.get(),
            hora_inicio = entry_inicio_hour.get(),
            fecha_fin = entry_fin_date.get(),
            hora_fin = entry_fin_hour.get(),
            ubicacion = entry_ubicacion.get(),
            ))
    btn_save.grid(row=7, column=1, columnspan=2, sticky="ew", pady=5, padx=5)
 
def pick_date_dialog():
    '''Display GUI date picker dialog,
       print date selected when OK clicked'''
 
    def print_sel():
        selected_date = (cal.get_date())
        print(selected_date)
 
    top = tk.Toplevel(ROOT)
 
    #defaults to today's date
    cal = Calendar(top,
                   font="Arial 10", background='darkblue',
                   foreground='white', selectmode='day')

    #print(dir(cal))
 
    cal.grid()
    ttk.Button(top, text="Ver eventos", command=print_sel).grid(sticky="ew", pady=5, padx=5)
    ttk.Button(top, text="Nuevo evento", command=event_form).grid(sticky="ew", pady=5, padx=5)

if __name__ == '__main__':
    
    ce.create_tables()

    # ev = Evento(titulo="Test", pk=1, ubicacion="new location 2", inicio=dt.datetime.now(), fin=dt.datetime.now(), descripcion="Save testing")
    # ev.save()
    # ev = Evento(titulo="Test33", pk=2, ubicacion="new location 2", inicio=dt.datetime.now(), fin=dt.datetime.now(), descripcion="Save testing")
    # ev.save()
    #ev = Evento(titulo="Test777", pk=2, ubicacion="new location 2", inicio=dt.datetime.now(), fin=dt.datetime.now(), descripcion="Save testing")
    #ev.save()

    #ev.add_asistente("lucaslucyk@gmail.com")
    #ev.add_asistente("lucyklucas@gmail.com")

    #print([asistente for asistente in ev.asistentes])
    #evs = Evento.objects(pk=2)
    #evs[0].delete_asistente("lucyklucas@gmail.com")

    for obj in ce.Evento.objects():
        print (obj, obj.asistentes)


    ce.close_conn(ce.DB_CONN)
    
    ROOT = tk.Tk()
    ROOT.withdraw()# hide naff extra window
    ROOT.title('Calendario Personal')
     
    pick_date_dialog()
     
    ROOT.mainloop()