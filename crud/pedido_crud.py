class PedidoCRUD:
    def __init__(self):
        self.pedidos = []

    def crear(self, pedido):
        """Create - Crear un nuevo pedido"""
        self.pedidos.append(pedido)
        return pedido

    def obtener_todos(self):
        """Read - Obtener todos los pedidos"""
        return self.pedidos

    def obtener_por_fecha(self, fecha):
        """Read - Obtener pedidos por fecha"""
        return [p for p in self.pedidos if p.fecha == fecha]

    def actualizar_productos(self, pedido, nuevos_productos):
        """Update - Actualizar los productos de un pedido"""
        if pedido not in self.pedidos:
            raise ValueError("El pedido no existe")
        pedido.productos = nuevos_productos
        return pedido

    def eliminar(self, pedido):
        """Delete - Eliminar un pedido"""
        if pedido not in self.pedidos:
            raise ValueError("El pedido no existe")
        self.pedidos.remove(pedido)
        return pedido
