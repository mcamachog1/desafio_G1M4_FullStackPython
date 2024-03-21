from abc import ABC, abstractmethod

class Anuncio(ABC):


    def __init__(self, ancho:int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str):
        self.__ancho = ancho
        self.__alto = alto
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo


    @staticmethod
    def mostrar_formatos():
        print("FORMATO VIDEO:")
        print("==============")
        for v in Video.SUB_TIPOS:
            print(f"- {v}")

        print("FORMATO DISPLAY:")
        print("==============")
        for d in Display.SUB_TIPOS:
            print(f"- {d}")

        print("FORMATO SOCIAL:")
        print("==============")
        for s in Social.SUB_TIPOS:
            print(f"- {s}")



    # Metodos no estáticos
    @abstractmethod
    def comprimir_anuncios(self):
        pass
    
    @abstractmethod
    def redimensionar_anuncios(self):
        pass



class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream","outstream")    




    def __init__(self, duracion:int) -> None:
        super().__init__(ancho=1, alto=1)
        self.__duracion = duracion



    def comprimir_anuncios(self):
        pass
    def redimensionar_anuncios(self):
        pass

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional","native")

    def comprimir_anuncios(self):
        pass
    def redimensionar_anuncios(self):
        pass


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook","linkedin")


    def comprimir_anuncios(self):
        pass
    def redimensionar_anuncios(self):
        pass