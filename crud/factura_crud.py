class FacturaCRUD:
    def __init__(self):
        self.facturas = []

    def crear(self, factura):
        self.facturas.append(factura)
        return factura

    def obtener_todas(self):
        return self.facturas

    def obtener_por_cliente(self, cedula_cliente):
        return [f for f in self.facturas if f.cliente.cedula == cedula_cliente]

    def obtener_por_fecha(self, fecha):
        return [f for f in self.facturas if f.fecha == fecha]

    def eliminar(self, factura):
        if factura not in self.facturas:
            raise ValueError("La factura no existe")
        self.facturas.remove(factura)
        return factura
