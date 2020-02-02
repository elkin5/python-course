CONDICIONES = (
    ("today == date", "Hoy"),
    ("today - date == dt.timedelta(days=1)", "Ayer"),
    ("today.isocalendar()[1] == date.isocalendar()[1]", "Esta semana"),
    ("today.isocalendar()[1] - date.isocalendar()[1] == 1", "La semana pasada"),
    ("today.month == date.month", "Este mes"),
    ("today.month - date.month == 1", "El mes pasado"),
    ("today.year == date.year", "Este año"),
    ("today.year - date.year == 1", "El año pasado"),
    #("else", "Hace más de un año"),
)

CONDICIONES = {
    "today == date": "Hoy",
    "today - date == dt.timedelta(days=1)": "Ayer",
    "today.isocalendar()[1] == date.isocalendar()[1]": "Esta semana",
    "today.isocalendar()[1] - date.isocalendar()[1] == 1": "La semana pasada",
    "today.month == date.month": "Este mes",
    "today.month - date.month == 1": "El mes pasado",
    "today.year == date.year": "Este año",
    "today.year - date.year == 1": "El año pasado",
    #"else": "Hace más de un año",
}

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