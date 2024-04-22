from abc import ABC , abstractmethod
from error import SubTipoInvalidoError

class Anuncio(ABC):
    def __init__(self, ancho:int, alto:int, url_archivo: str, url_clic: str, sub_tipo: str) -> None:
        self.__ancho = ancho if ancho > 1 else 1
        self.__alto = alto if alto > 1 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
    
    
    @staticmethod
    def mostrar_formatos() -> None:
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

    @abstractmethod
    def comprimir_anuncios(self) -> None: 
        pass

    @abstractmethod
    def redimensionar_anuncio(self) -> None :
        pass

    @property
    def ancho(self) -> int:
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho) -> None:
        self.__ancho = ancho if ancho > 0 else 1

    @property
    def alto(self) -> int:
        return self.__alto
    
    @alto.setter
    def alto(self, alto) -> None:
        self.__alto = alto if alto > 0 else 1

    @property
    def url_archivo(self) -> str:
        return self.__url_archivo
    @url_archivo.setter
    def url_archivo(self, url_archivo: str) -> None:
        self.__url_archivo = url_archivo

    @property
    def url_clic(self) -> str:
        return self.__url_clic
    @url_clic.setter
    def url_clic(self, url_clic:str)->None:
        self.__url_clic = url_clic

    @property
    def sub_tipo(self) -> str:
        return self.__sub_tipo
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo: str) -> None:
        if (isinstance(self, Video) and sub_tipo not in Video.SUB_TIPOS
        or isinstance(self, Display) and sub_tipo not in Display.SUB_TIPOS
        or isinstance(self, Social) and sub_tipo not in Social.SUB_TIPOS):
            raise SubTipoInvalidoError("El sub tipo indicado no está "
        "permitido para este formato")
        else:
            self.__sub_tipo = sub_tipo


class Video(Anuncio):
    # Atributos de clase - Estáticos
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo: str, url_clic: str,
        sub_tipo: str, duracion: int) -> None:
        super().__init__(1,1,url_archivo,url_clic,sub_tipo)
        self.__duracion = duracion if duracion > 0 else 5

    def comprimir_anuncios(self) -> None:
        print("Comprimiendo video...")

    def redimensionar_anuncio(self) -> None:
        print("Recortando video...")
    
    @property
    def duracion(self) -> int:
        return self.__duracion
    @duracion.setter
    def duracion(self, duracion) -> None:
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def ancho(self) -> int:
        return self.__ancho
    @ancho.setter
    def ancho(self, ancho) -> None:
        pass
    @property
    def alto(self) -> int:
        return self.__alto
    @alto.setter
    def alto(self, alto) -> None:
        pass


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional","native")

    def comprimir_anuncios(self) -> None:
        print("Comprimiendo display...")

    def redimensionar_anuncio(self) -> None:
        print("Recortando display...")    

class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def comprimir_anuncios(self) -> None:
        print("Comprimiendo redes sociales...")

    def redimensionar_anuncio(self) -> None:
        print("Recortando redes sociales...")    
    