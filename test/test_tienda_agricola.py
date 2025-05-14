import unittest
from datetime import date
from modelo.tienda_agricola import TiendaAgricola
from modelo.cliente import Cliente
from modelo.fertilizante import Fertilizante
from modelo.control_plaga import ControlPlaga
from modelo.antibiotico import Antibiotico
from modelo.pedido import Pedido
from modelo.factura import Factura

class TestTiendaAgricola(unittest.TestCase):
    def setUp(self):
        self.tienda = TiendaAgricola()
        self.cliente = Cliente("Test Cliente", "123456789")
        self.fertilizante = Fertilizante("ICA-001", "TestFert", "Cada 30 días", 50000, "2025-04-20")
        self.plaguicida = ControlPlaga("ICA-002", "TestPlag", "Cada 15 días", 60000, 10)
        self.antibiotico = Antibiotico("TestAnti", 500, "Bovinos", 75000)

    def test_registrar_cliente(self):
        self.tienda.registrar_cliente(self.cliente)
        self.assertIn("123456789", self.tienda.clientes)
        self.assertEqual(self.tienda.clientes["123456789"], self.cliente)

    def test_agregar_producto(self):
        self.tienda.agregar_producto(self.fertilizante)
        self.assertIn(self.fertilizante, self.tienda.productos)

    def test_buscar_por_cedula_cliente_existente(self):
        self.tienda.registrar_cliente(self.cliente)
        pedido = Pedido([self.fertilizante, self.plaguicida])
        self.cliente.agregar_pedido(pedido)
        facturas = self.tienda.buscar_por_cedula("123456789")
        self.assertEqual(len(facturas), 1)
        self.assertEqual(facturas[0].valor_total, 110000)

    def test_buscar_por_cedula_cliente_inexistente(self):
        with self.assertRaises(ValueError):
            self.tienda.buscar_por_cedula("999999999")

if __name__ == '__main__':
    unittest.main()
