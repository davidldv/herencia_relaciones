from modelo.cliente import Cliente
from modelo.fertilizante import Fertilizante
from modelo.control_plaga import ControlPlaga
from modelo.antibiotico import Antibiotico
from modelo.pedido import Pedido
from modelo.factura import Factura

# Crear cliente
cliente1 = Cliente("Carlos Ramírez", "123456789")

# Crear productos
fertilizante = Fertilizante("ICA-001", "NitroGreen", "Cada 30 días", 50000, "2025-04-20")
plaguicida = ControlPlaga("ICA-002", "PlaguicidaX", "Cada 15 días", 60000, 10)
antibiotico = Antibiotico("Antibovino", 500, "Bovinos", 75000)

# Crear pedido y agregarlo al cliente
pedido = Pedido([fertilizante, plaguicida, antibiotico])
cliente1.agregar_pedido(pedido)

# Crear factura
factura = Factura(cliente1, pedido)
factura.resumen()
