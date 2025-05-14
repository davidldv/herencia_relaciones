import unittest
from datetime import date
from crud.cliente_crud import ClienteCRUD
from crud.producto_crud import ProductoCRUD
from crud.pedido_crud import PedidoCRUD
from crud.factura_crud import FacturaCRUD
from modelo.cliente import Cliente
from modelo.fertilizante import Fertilizante
from modelo.control_plaga import ControlPlaga
from modelo.antibiotico import Antibiotico
from modelo.pedido import Pedido
from modelo.factura import Factura

class TestCRUD(unittest.TestCase):
    def setUp(self):
        self.cliente_crud = ClienteCRUD()
        self.producto_crud = ProductoCRUD()
        self.pedido_crud = PedidoCRUD()
        self.factura_crud = FacturaCRUD()
        self.cliente = Cliente("Test Cliente", "123456789")
        self.fertilizante = Fertilizante("ICA-001", "TestFert", "Cada 30 días", 50000, "2025-04-20")
        self.plaguicida = ControlPlaga("ICA-002", "TestPlag", "Cada 15 días", 60000, 10)
        self.antibiotico = Antibiotico("TestAnti", 500, "Bovinos", 75000)

    def test_cliente_crud(self):
        # Create
        cliente_creado = self.cliente_crud.crear(self.cliente)
        self.assertEqual(cliente_creado.cedula, "123456789")

        # Read
        cliente_obtenido = self.cliente_crud.obtener("123456789")
        self.assertEqual(cliente_obtenido.nombre, "Test Cliente")

        # Update
        cliente_actualizado = self.cliente_crud.actualizar("123456789", "Nuevo Nombre")
        self.assertEqual(cliente_actualizado.nombre, "Nuevo Nombre")

        # Delete
        cliente_eliminado = self.cliente_crud.eliminar("123456789")
        self.assertEqual(cliente_eliminado.cedula, "123456789")
        with self.assertRaises(ValueError):
            self.cliente_crud.obtener("123456789")

    def test_producto_crud(self):
        # Create
        producto = self.producto_crud.crear(self.fertilizante)
        self.assertEqual(producto.registro_ica, "ICA-001")

        # Read all
        productos = self.producto_crud.obtener_todos()
        self.assertEqual(len(productos), 1)

        # Update precio
        producto_actualizado = self.producto_crud.actualizar_precio("TestFert", 55000)
        self.assertEqual(producto_actualizado.valor, 55000)

        # Delete
        producto_eliminado = self.producto_crud.eliminar("TestFert")
        self.assertEqual(producto_eliminado.registro_ica, "ICA-001")
        self.assertEqual(len(self.producto_crud.obtener_todos()), 0)

    def test_pedido_crud(self):
        # Create
        pedido = Pedido([self.fertilizante, self.plaguicida])
        pedido_creado = self.pedido_crud.crear(pedido)
        self.assertEqual(len(pedido_creado.productos), 2)

        # Read
        pedidos = self.pedido_crud.obtener_todos()
        self.assertEqual(len(pedidos), 1)

        # Update
        nuevos_productos = [self.antibiotico]
        pedido_actualizado = self.pedido_crud.actualizar_productos(pedido, nuevos_productos)
        self.assertEqual(len(pedido_actualizado.productos), 1)

        # Delete
        pedido_eliminado = self.pedido_crud.eliminar(pedido)
        self.assertEqual(len(self.pedido_crud.obtener_todos()), 0)

    def test_factura_crud(self):
        # Create
        pedido = Pedido([self.fertilizante, self.plaguicida])
        factura = Factura(self.cliente, pedido)
        factura_creada = self.factura_crud.crear(factura)
        self.assertEqual(factura_creada.cliente.cedula, "123456789")

        # Read
        facturas = self.factura_crud.obtener_todas()
        self.assertEqual(len(facturas), 1)

        facturas_cliente = self.factura_crud.obtener_por_cliente("123456789")
        self.assertEqual(len(facturas_cliente), 1)

        facturas_fecha = self.factura_crud.obtener_por_fecha(date.today())
        self.assertEqual(len(facturas_fecha), 1)

        # Delete
        factura_eliminada = self.factura_crud.eliminar(factura)
        self.assertEqual(len(self.factura_crud.obtener_todas()), 0)

if __name__ == '__main__':
    unittest.main()
