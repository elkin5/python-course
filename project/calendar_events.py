'''
    Calendar Events Manager.

    Módulo para la gestión de un calendario personal.

    Repo actualizado en el siguiente link:
    https://github.com/lucaslucyk/python-course

'''

### imports ###
import datetime as dt
import sqlite3

### constantes ###
DB_NAME = "calendar.sqlite3"
DB_CONN = sqlite3.connect(DB_NAME)

def close_conn(conexion=DB_CONN):
    ''' Cierra una conexión a una base de datos

    Parameters:
        sqlite3.Connection: Objeto de conexión a una base de datos

    '''
    conexion.close()

def iniciar_bbdd():
    ''' Crea las tablas de la base de datos para guardar 
        los eventos y asistentes en caso de que no existan.
    '''
    cursor = DB_CONN.cursor()

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
            evento INTEGER REFERENCES evento(pk) ON DELETE CASCADE ON UPDATE CASCADE
            )'''
        )

    cursor.close()


class Evento:
    ''' Datos de un evento. Los objetos se guardan en la base de datos. '''

    def __init__(self, titulo, pk=None, ubicacion="", inicio=dt.datetime.now(), fin=dt.datetime.now(), descripcion="", asistentes=[]):

        self.pk = pk
        self.titulo = titulo
        self.ubicacion = ubicacion
        self.inicio = inicio if isinstance(inicio, dt.datetime) else dt.datetime.fromisoformat(inicio)
        self.fin = fin if isinstance(fin, dt.datetime) else dt.datetime.fromisoformat(fin)
        self.descripcion = descripcion
        self.asistentes = asistentes

    def __str__(self):
        return f'{self.titulo} | Del {self.inicio.strftime("%Y-%m-%d a las %H:%M")} al {self.fin.strftime("%Y-%m-%d a las %H:%M")}'

    @classmethod
    def objects(cls, _operator:str="AND", **kwargs):
        ''' Método de clase. Devuelve como instancias de Evento, los registros de la 
            base de datos que conincidan con las condiciones recibidas como kwargs.

            El atributo asistentes es una lista de mails, NO objetos instancia de Asistente.

        Parameters:
            dict kwargs: conjunto de pares "campo=valor" como condicón de filtro.
            str _operator: "AND" por defecto. Indica como se conjugan el conjunto de condiciones recibidas.
        Returns:
            list:   - Lista de objetos coincidentes con los criterios indicados.
                    - Lista vacía en caso que ningún registro coincida con los criterios indicados.
        Raises:
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''

        if not DB_CONN:
            raise RuntimeError("No hay conexión a la base de datos.")

        cursor = DB_CONN.cursor()

        sql = "SELECT * FROM eventos"
        if kwargs:
            sql += " WHERE "
            sql += f' {_operator} '.join([f'{k} = "{v}"' for k, v in kwargs.items()])

        cursor.execute(sql)
        registros = cursor.fetchall()

        evs = []
        for registro in registros:
            #Por cada registro obtenido al ejecutar la sentencia select,
            #Creo un objeto de clase Evento.

            ev = cls(
                pk = int(registro[0]),
                titulo = registro[1],
                ubicacion = registro[2],
                inicio = dt.datetime.fromisoformat(registro[3]),
                fin = dt.datetime.fromisoformat(registro[4]),
                descripcion = registro[5],
                )

            #Obtengo todos los asistentes con el método de clase "Asistente.objects"
            asistentes = Asistente.objects(evento=registro[0])
            ev.asistentes = [asistente.mail for asistente in asistentes]
            evs.append(ev)

        cursor.close()
        return evs

    @classmethod
    def day_events(cls, day):
        ''' Método de clase. Devuelve como instancias de Evento, los registros de la 
            base de datos para el día indicado en el parámetro "day".

        Parameters:
            datetime.datetime day: día del que se se desea obtener los Eventos.
        Returns:
            list:   - Lista de objetos que incluyen el día indicado.
                    - Lista vacía en caso que no existan registros coincidentes.
        Raises:
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''

        if not DB_CONN:
            raise RuntimeError("No hay conexión a la base de datos.")

        cursor = DB_CONN.cursor()

        sql = f'''
            SELECT * FROM eventos
            WHERE DATE("{str(day)}") BETWEEN DATE(inicio) AND DATE(fin)
            '''
        cursor.execute(sql)
        registros = cursor.fetchall()

        evs = []
        for registro in registros:
            #Por cada registro obtenido al ejecutar la sentencia select,
            #Creo un objeto de clase Evento.

            ev = cls(
                pk = int(registro[0]),
                titulo = registro[1],
                ubicacion = registro[2],
                inicio = dt.datetime.fromisoformat(registro[3]),
                fin = dt.datetime.fromisoformat(registro[4]),
                descripcion = registro[5],
                )

            #Obtengo todos los asistentes con el método de clase "Asistente.objects"
            asistentes = Asistente.objects(evento=registro[0])
            ev.asistentes = [asistente.mail for asistente in asistentes]
            evs.append(ev)

        cursor.close()
        return evs

    @property
    def exists(self):
        ''' Indica si el objeto se encuentra guardado en la base de datos.

        Returns:
            bool:   True en caso que el objeto esta guardado en la base de datos (pk = self.pk). 
                    False en caso contrario.
        Raises:
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''

        if not DB_CONN:
            raise RuntimeError("No hay conexión a la base de datos.")

        #No existe un registro de pk = None
        #Si self.pk no esta definido, no existe en la bbdd
        if not self.pk:
            return False

        #Compruebo si obtengo registros de "pk = self.pk"
        cursor = DB_CONN.cursor()
        cursor.execute(f"SELECT * FROM eventos where pk={self.pk}")

        existe = True if cursor.fetchone() else False
        cursor.close()

        return existe

    def save(self):
        ''' Guarda el objeto en la base de datos en caso que no exista. Lo actualiza en caso contrario. '''

        cursor = DB_CONN.cursor()
        
        #Valores a guardar
        valores = (
            self.titulo,
            self.ubicacion,
            self.inicio,
            self.fin,
            self.descripcion,
            self.pk,
            )

        if not self.exists:

            #Si el objeto no existe, insertamos los valores
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

            #Como el evento no existe, inserto los asistentes sin comprobar si existen
            [Asistente(mail=asistente, evento=self.pk).save() for asistente in self.asistentes]

        else:
            #Si el objeto existe, actualiamos los valores.
            sql = ''' 
                UPDATE eventos
                SET titulo = ? ,
                    ubicacion = ? ,
                    inicio = ? ,
                    fin = ? ,
                    descripcion = ?
                WHERE pk = ? '''
            
            cursor.execute(sql, valores)

            #Elimino todos los asistentes que no estan incluidos en self.asistentes
            for asistente in Asistente.objects(evento=self.pk):
                asistente.delete() if asistente.mail not in self.asistentes else None

            #Inserto los asistentes. El método save del objeto de clase Asistente 
            #se encarga de determinar si ya existe en la bbdd
            [Asistente(mail=asistente, evento=self.pk).save() for asistente in self.asistentes]

        DB_CONN.commit()
        cursor.close()

    def delete(self):
        ''' Elimina los eventos y asistentes correspondientes al objeto.

        Raises:
            ValueError: En caos que no exista el registro en la base de datos.
        '''

        if not self.exists:
            raise ValueError(f'El objeto de pk {self.pk} no existe en la base de datos')

        #Elimino todos los registros de asistentes del evento
        [asistente.delete() for asistente in Asistente.objects(evento=self.pk)]

        cursor = DB_CONN.cursor()
        sql = f'DELETE FROM eventos WHERE pk = "{self.pk}"'
        cursor.execute(sql)

        DB_CONN.commit()
        cursor.close()

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

class Asistente:
    ''' Asistentes de un Evento. Clase para guardar en la base de datos '''

    def __init__(self, mail:str, evento:int, pk:int=None):
        self.pk = pk
        self.mail = mail
        self.evento = evento

    def __str__(self):
        return self.mail

    def __eq__(self, other):
        ''' Comprueba y si un objeto de asistente es igual a otro (other)
            
        Parameters:
            Asistente other: Objeto instancia de Asistente.
        Returns:
            bool: True si los objetos son iguales y False en caso contrario.
        '''

        return self.mail == other.email and self.evento == other.evento

    @classmethod
    def objects(cls, _operator:str="AND", **kwargs):
        ''' Método de clase. Devuelve como instancias de Asistentes, los registros de la 
            base de datos que conincidan con las condiciones recibidas como kwargs.

        Parameters:
            dict kwargs: conjunto de pares "campo=valor" como condicón de filtro.
            str _operator: "AND" por defecto. Indica como se conjugan el conjunto de condiciones recibidas.
        Returns:
            list:   - Lista de objetos coincidentes con los criterios indicados.
                    - Lista vacía en caso que ningún registro coincida con los criterios indicados.
        Raises:
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''

        if not DB_CONN:
            raise RuntimeError("No hay conexión a la base de datos.")

        cursor = DB_CONN.cursor()

        sql = "SELECT * FROM asistentes"
        if kwargs:
            sql += " WHERE "
            sql += f' {_operator} '.join([f'{k} = "{v}"' for k, v in kwargs.items()])

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
        ''' Indica si el objeto se encuentra guardado en la base de datos.

        Returns:
            bool: True en caso que el objeto esta guardado en la base de datos. False en caso contrario.
        Raises:
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''

        if not DB_CONN:
            raise RuntimeError("No hay conexión a la base de datos.")

        cursor = DB_CONN.cursor()
        sql = f'SELECT * FROM asistentes where (mail="{self.mail}" AND evento={self.evento}) OR (pk={self.pk if self.pk else -1});'
        cursor.execute(sql)

        existe = True if cursor.fetchone() else False
        cursor.close()

        return existe

    def save(self):
        ''' Guarda el objeto en la base de datos en caso que no exista. '''

        if not self.exists:

            cursor = DB_CONN.cursor()
            
            #valores a guardar
            valores = (
                self.mail,
                self.evento,
                self.pk,
                )

            #Se insertan los datos en la base de datos.
            cursor.execute('''
                INSERT INTO asistentes(
                    mail, 
                    evento, 
                    pk ) 
                VALUES (?, ?, ?)''',
                valores)

            #asigna a pk el valor de la fila del último registro ingresado.
            self.pk = int(cursor.lastrowid)

            DB_CONN.commit()
            cursor.close()

    def delete(self):
        ''' Elimina el objeto de la base de datos.

        Raises:
            ValueError: En caos que no exista el registro en la base de datos.
        '''

        if not self.exists:
            raise ValueError(f'El objeto de pk {self.pk} no existe en la base de datos')

        cursor = DB_CONN.cursor()
        sql = f'DELETE FROM asistentes WHERE pk = "{self.pk}"'
        cursor.execute(sql)

        DB_CONN.commit()
        cursor.close()

