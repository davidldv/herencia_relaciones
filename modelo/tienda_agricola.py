from crud.cliente_crud import ClienteCRUD
from crud.producto_crud import ProductoCRUD
from crud.pedido_crud import PedidoCRUD
from crud.factura_crud import FacturaCRUD
from modelo.factura import Factura

class TiendaAgricola:
    def __init__(self):
        self.cliente_crud = ClienteCRUD()
        self.producto_crud = ProductoCRUD()
        self.pedido_crud = PedidoCRUD()
        self.factura_crud = FacturaCRUD()

    def registrar_cliente(self, cliente):
        return self.cliente_crud.crear(cliente)

    def agregar_producto(self, producto):
        return self.producto_crud.crear(producto)
        
    def buscar_por_cedula(self, cedula):
        try:
            cliente = self.cliente_crud.obtener(cedula)
        except ValueError:
            raise ValueError(f"No se encontró cliente con cédula {cedula}")
        
        facturas = []
        print(f"\nHistorial de compras para {cliente.nombre} (Cédula: {cedula}):")
        
        for pedido in cliente.pedidos:
            factura = Factura(cliente, pedido)
            self.factura_crud.crear(factura)
            facturas.append(factura)
            
            print(f"\nFactura del {factura.fecha}:")
            print("Productos:")
            for producto in pedido.productos:
                if hasattr(producto, 'valor'):
                    precio = producto.valor
                else:
                    precio = producto.precio
                print(f"- {producto.nombre}: ${precio:,.2f}")
            print(f"Total: ${factura.valor_total:,.2f}")
        
        return facturas
