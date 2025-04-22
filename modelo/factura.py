class Factura:
    def __init__(self, cliente, pedido):
        self.cliente = cliente
        self.pedido = pedido
        self.fecha = pedido.fecha
        self.valor_total = pedido.valor_total()

    def resumen(self):
        print(f"Factura para {self.cliente.nombre} ({self.cliente.cedula})")
        print(f"Fecha: {self.fecha}")
        print(f"Total: ${self.valor_total:.2f}")
