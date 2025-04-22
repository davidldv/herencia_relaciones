from modelo.producto_control import ProductoControl

class Fertilizante(ProductoControl):
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, valor, fecha_ultima_aplicacion):
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, valor)
        self.fecha_ultima_aplicacion = fecha_ultima_aplicacion
