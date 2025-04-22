class Cliente:
    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)
