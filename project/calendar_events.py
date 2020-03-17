'''
    Calendar Events Manager.

    Módulo para la gestión de un calendario personal.

    Repo actualizado en el siguiente link:
    https://github.com/lucaslucyk/python-course

'''

import datetime as dt
import sqlite3

DB_NAME = "calendar.sqlite3"
DB_CONN = sqlite3.connect(DB_NAME)

def close_conn(conexion=DB_CONN):
    conexion.close()

def create_tables():

    cursor = DB_CONN.cursor()

    #creamos una tabla
    cursor.execute('''
        CREATE TABLE if not exists eventos(
            pk integer PRIMARY KEY AUTOINCREMENT, 
            titulo text, 
            ubicacion text, 
            inicio datetime, 
            fin datetime, 
            descripcion text
            )'''
        )

    cursor.execute('''
        CREATE TABLE if not exists asistentes(
            pk integer PRIMARY KEY AUTOINCREMENT, 
            mail text,
            evento INTEGER REFERENCES evento(pk) ON UPDATE CASCADE
            )'''
        )

    cursor.close()

class QuerySet(object):
    def __init__(self, *args, **kwargs):
        [setattr(self, k, v) for k,v in kwargs.items()]

class Asistente(object):
    def __init__(self, mail, evento, pk=None):
        self.pk = pk
        self.mail = mail
        self.evento = evento

    def __str__(self):
        return self.mail

    def __eq__(self, other):
        return self.mail == other.email and self.evento == other.evento

    @classmethod
    def objects(cls, _operator="AND", **kwargs):
        if not DB_CONN:
            raise RuntimeError("No hay conexión a la base de datos.")

        cursor = DB_CONN.cursor()

        sql = "SELECT * FROM asistentes"
        if kwargs:
            sql += " WHERE "
            sql += f' {_operator} '.join([f'{k} = "{v}"' for k, v in kwargs.items()])

        #print(sql)

        cursor.execute(sql)
        registros = cursor.fetchall()

        asists = []
        for registro in registros:

            asists.append(cls(
                pk = registro[0],
                mail = registro[1],
                evento = registro[2],
                ))

        cursor.close()

        return asists

    @property
    def exists(self):
        if not DB_CONN:
            raise RuntimeError("No hay conexión a la base de datos.")

        #if not self.pk:
        #    return False

        cursor = DB_CONN.cursor()
        sql = f'SELECT * FROM asistentes where (mail="{self.mail}" AND evento={self.evento}) OR (pk={self.pk if self.pk else -1});'
        #print(sql)
        cursor.execute(sql)

        existe = True if cursor.fetchone() else False
        cursor.close()

        return existe

    def save(self):

        cursor = DB_CONN.cursor()
        
        #Creamos los valores
        valores = (
            self.mail,
            self.evento,
            self.pk,
            )

        if not self.exists:
            #Insertamos los valores
            
            cursor.execute('''
                INSERT INTO asistentes(
                    mail, 
                    evento, 
                    pk ) 
                VALUES (?, ?, ?)''',
                
                valores)
            self.pk = int(cursor.lastrowid)


        DB_CONN.commit()
        cursor.close()

    def delete(self):
        if not self.exists:
            raise ValueError(f'El objeto de pk {self.pk} no existe en la base de datos')

        cursor = DB_CONN.cursor()
        sql = f'DELETE FROM asistentes WHERE pk = "{self.pk}"'
        cursor.execute(sql)

        DB_CONN.commit()
        cursor.close()

class Evento(object):

    def __init__(self, titulo, pk=None, ubicacion="", inicio=dt.datetime.now(), fin=dt.datetime.now(), descripcion=""):

        self.pk = pk
        self.titulo = titulo
        self.ubicacion = ubicacion
        self.inicio = inicio
        self.fin = fin
        self.descripcion = descripcion
        self.asistentes = []

    def __str__(self):
        return f'{self.titulo} desde el {self.inicio} hasta el {self.fin}'

    @classmethod
    def objects(cls, _operator="AND", **kwargs):
        if not DB_CONN:
            raise RuntimeError("No hay conexión a la base de datos.")

        cursor = DB_CONN.cursor()

        sql = "SELECT * FROM eventos"
        if kwargs:
            sql += " WHERE "
            sql += f' {_operator} '.join([f'{k} = "{v}"' for k, v in kwargs.items()])

        #print(sql)

        cursor.execute(sql)
        registros = cursor.fetchall()

        evs = []
        for registro in registros:

            ev = cls(
                pk = registro[0],
                titulo = registro[1],
                ubicacion = registro[2],
                inicio = registro[3],
                fin = registro[4],
                descripcion = registro[5],
                )

            #get all assistents
            asistentes = Asistente.objects(evento=registro[0])
            ev.asistentes.extend([asistente.mail for asistente in asistentes])
            evs.append(ev)

        cursor.close()
        return evs

    @property
    def exists(self):
        if not DB_CONN:
            raise RuntimeError("No hay conexión a la base de datos.")

        if not self.pk:
            return False

        cursor = DB_CONN.cursor()
        cursor.execute(f"SELECT * FROM eventos where pk={self.pk}")

        existe = True if cursor.fetchone() else False
        cursor.close()

        return existe

    def add_asistente(self, mail):
        if not self.exists:
            raise ValueError("Guadar el evento antes de añadir un asistnte")

        asist = Asistente(mail=mail, evento=self.pk)
        
        if asist.mail not in self.asistentes:
            asist.save()
            self.asistentes.append(asist.mail)

    def delete_asistente(self, mail):
        if not self.exists:
            raise ValueError("Guadar el evento antes de eliminar un asistnte")

        asists = Asistente.objects(mail=mail, evento=self.pk)
        if asists:
            asists[0].delete()

    def save(self):

        cursor = DB_CONN.cursor()
        
        #Creamos los valores
        valores = (
            #self.pk,
            self.titulo,
            self.ubicacion,
            self.inicio,
            self.fin,
            self.descripcion,
            self.pk,
            )

        if not self.exists:
            #Insertamos los valores
            
            cursor.execute('''
                INSERT INTO eventos(
                    titulo, 
                    ubicacion, 
                    inicio, 
                    fin, 
                    descripcion, 
                    pk ) 
                VALUES (?, ?, ?, ?, ?, ?)''',
                
                valores)

            self.pk = int(cursor.lastrowid)
        else:
            #Actualizamos valores
            sql = ''' 
                UPDATE eventos
                SET titulo = ? ,
                    ubicacion = ? ,
                    inicio = ? ,
                    fin = ? ,
                    descripcion = ?
                WHERE pk = ? '''
            
            cursor.execute(sql, valores)

        DB_CONN.commit()
        cursor.close()

    def delete(self):
        if not self.exists:
            raise ValueError(f'El objeto de pk {self.pk} no existe en la base de datos')

        cursor = DB_CONN.cursor()
        sql = f'DELETE FROM eventos WHERE pk = "{self.pk}"'
        cursor.execute(sql)

        DB_CONN.commit()
        cursor.close()

if __name__ == '__main__':
    
    create_tables()

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

    for obj in Evento.objects():
        print (obj, obj.asistentes)


    close_conn(DB_CONN)
    
