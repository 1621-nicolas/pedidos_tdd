from app.pedido_service import PedidoService
from tests.fakes import FakePedidoRepository


def test_crear_y_recuperar_pedido_con_fake_repository():
    # Arrange
    repository = FakePedidoRepository()
    service = PedidoService(repository)

    productos = [
        {
            "nombre": "Teclado",
            "precio": 100,
            "cantidad": 2
        }
    ]

    # Act
    pedido_creado = service.crear_pedido(productos, "VIP")
    pedido_recuperado = service.obtener_pedido(pedido_creado.id)

    # Assert
    assert pedido_creado.id == 1
    assert pedido_recuperado is pedido_creado
    assert pedido_recuperado.subtotal == 200
    assert pedido_recuperado.descuento == 20
    assert pedido_recuperado.impuesto == 32.4
    assert pedido_recuperado.total == 212.4
