class Error(Exception):
    """Clase Base Excepciones"""
    pass

class LargoExcedidoError(Error):

    def __init__(self, mensaje: str, dimension: int = None,
            maximo: int = None) -> None:
        self.mensaje = mensaje
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self) -> str:
        if self.dimension is None and self.maximo is None:
            return super().__str__()
        else:
            ret = self.mensaje

            if self.dimension:
                ret += f" Se ingresó dimensión {self.dimension}."
            
            if self.maximo:
                ret += f" El valor máximo permitido es {self.maximo}."

            return ret
        
class SubTipoInvalidoError(Error):
    pass
    