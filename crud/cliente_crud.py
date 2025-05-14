class ClienteCRUD:
    def __init__(self):
        self.clientes = {}

    def crear(self, cliente):
        if cliente.cedula in self.clientes:
            raise ValueError(f"Ya existe un cliente con cédula {cliente.cedula}")
        self.clientes[cliente.cedula] = cliente
        return cliente

    def obtener(self, cedula):
        if cedula not in self.clientes:
            raise ValueError(f"No existe un cliente con cédula {cedula}")
        return self.clientes[cedula]

    def actualizar(self, cedula, nuevo_nombre):
        if cedula not in self.clientes:
            raise ValueError(f"No existe un cliente con cédula {cedula}")
        self.clientes[cedula].nombre = nuevo_nombre
        return self.clientes[cedula]

    def eliminar(self, cedula):
        if cedula not in self.clientes:
            raise ValueError(f"No existe un cliente con cédula {cedula}")
        return self.clientes.pop(cedula)
