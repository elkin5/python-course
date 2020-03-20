import calendar_events as ce, calendar_interfaces as ci

if __name__ == '__main__':
    
    #Iniciamos la base de datos y lanzamos la interfaz creada
    ce.iniciar_bbdd()
    app = ci.App()