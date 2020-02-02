import datetime as dt

#Condiciones para obtener el delta. Deben estar en orden de coincidencia.
#date es la fecha que se comparará
CONDICIONES = {
    "Hoy": "today == date",
    "Ayer": "today - date == dt.timedelta(days=1)",
    "Esta semana": "today.isocalendar()[1] == date.isocalendar()[1]",
    "La semana pasada": "today.isocalendar()[1] - date.isocalendar()[1] == 1",
    "Este mes": "today.month == date.month",
    "El mes pasado": "today.month - date.month == 1",
    "Este año": "today.year == date.year",
    "El año pasado": "today.year - date.year == 1",
}

def ultima_modificacion(fecha, *args):
    ''' Devuelve hace cuanto fue modificado un archivo recibiendo la fecha en la cual fue modificado.

    Parameters:
        str fecha: Fecha en isoformat en la que fue modificado el archivo.
    Returns:
        str: Representación textual de hace cuanto fue modificado el archivo.
    Raises:
        ValueError: En caso que la fecha que se ingresa sea mayor al día actual.
    '''
    date = dt.datetime.fromisoformat(fecha).date()
    today = dt.date.today()

    if date > today:
        raise ValueError("La fecha es mayor al día actual.")

    for k,v in CONDICIONES.items():
        if eval(v):
            return k
            
    # En caso que no se cumpla ninguna condición
    return "Hace más de un año"

if __name__ == '__main__':
    print(ultima_modificacion("2019-11-14"))