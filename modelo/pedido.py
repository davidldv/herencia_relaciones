from datetime import date

class Pedido:
    def __init__(self, productos):
        self.productos = productos
        self.fecha = date.today()

    def valor_total(self):
        return sum(producto.valor if hasattr(producto, 'valor') else producto.precio for producto in self.productos)
