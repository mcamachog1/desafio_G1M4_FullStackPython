from datetime import date

class Campania():
    def __init__(self, nombre:str, fecha_inicio:date, fecha_termino:date):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__lista_anuncios = []
        
    def __str__(self):
        return super().__str__()