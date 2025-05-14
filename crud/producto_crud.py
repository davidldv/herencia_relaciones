class ProductoCRUD:
    def __init__(self):
        self.productos = []

    def crear(self, producto):
        """Create - Crear un nuevo producto"""
        self.productos.append(producto)
        return producto

    def obtener_todos(self):
        """Read - Obtener todos los productos"""
        return self.productos

    def obtener_por_nombre(self, nombre):
        """Read - Obtener un producto por su nombre"""
        productos = [p for p in self.productos if p.nombre == nombre]
        if not productos:
            raise ValueError(f"No existe un producto con nombre {nombre}")
        return productos[0]

    def actualizar_precio(self, nombre, nuevo_precio):
        """Update - Actualizar el precio de un producto"""
        producto = self.obtener_por_nombre(nombre)
        if hasattr(producto, 'valor'):
            producto.valor = nuevo_precio
        else:
            producto.precio = nuevo_precio
        return producto

    def eliminar(self, nombre):
        """Delete - Eliminar un producto"""
        producto = self.obtener_por_nombre(nombre)
        self.productos.remove(producto)
        return producto
