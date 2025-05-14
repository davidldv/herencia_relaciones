from modelo.cliente import Cliente
from modelo.fertilizante import Fertilizante
from modelo.control_plaga import ControlPlaga
from modelo.antibiotico import Antibiotico
from modelo.pedido import Pedido
from modelo.factura import Factura
from modelo.tienda_agricola import TiendaAgricola

tienda = TiendaAgricola()

cliente1 = Cliente("Carlos Ramírez", "123456789")
cliente2 = Cliente("Ana Martínez", "987654321")

tienda.registrar_cliente(cliente1)
tienda.registrar_cliente(cliente2)

fertilizante1 = Fertilizante("ICA-001", "NitroGreen", "Cada 30 días", 50000, "2025-04-20")
fertilizante2 = Fertilizante("ICA-002", "FosfoMax", "Cada 45 días", 75000, "2025-04-15")
plaguicida1 = ControlPlaga("ICA-003", "PlaguicidaX", "Cada 15 días", 60000, 10)
plaguicida2 = ControlPlaga("ICA-004", "InsectKill", "Cada 20 días", 45000, 7)
antibiotico1 = Antibiotico("Antibovino", 500, "Bovinos", 75000)
antibiotico2 = Antibiotico("PorciHealth", 450, "Porcinos", 65000)

for producto in [fertilizante1, fertilizante2, plaguicida1, plaguicida2, antibiotico1, antibiotico2]:
    tienda.agregar_producto(producto)

pedido1 = Pedido([fertilizante1, plaguicida1, antibiotico1])
pedido2 = Pedido([fertilizante2, antibiotico2])
cliente1.agregar_pedido(pedido1)
cliente1.agregar_pedido(pedido2)

pedido3 = Pedido([plaguicida2, antibiotico1])
cliente2.agregar_pedido(pedido3)

print("\nBúsqueda de historial de compras")
tienda.buscar_por_cedula("123456789")
print("\n----------------------------------------")
tienda.buscar_por_cedula("987654321")
