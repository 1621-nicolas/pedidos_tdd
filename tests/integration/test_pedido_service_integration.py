from app.repository import PedidoRepository
from app.pedido_service import PedidoService


def test_crear_y_recuperar_pedido_desde_servicio(tmp_path):
    # Arrange
    db_path = tmp_path / "test_service.db"

    repository = PedidoRepository(str(db_path))
    service = PedidoService(repository)

    productos = [
        {
            "nombre": "Teclado",
            "precio": 100,
            "cantidad": 2
        },
        {
            "nombre": "Mouse",
            "precio": 50,
            "cantidad": 1
        }
    ]

    # Act
    pedido_creado = service.crear_pedido(productos, "VIP")
    pedido_recuperado = service.obtener_pedido(pedido_creado.id)

    # Assert
    assert pedido_creado.id is not None
    assert pedido_recuperado is not None

    assert pedido_recuperado.subtotal == 250
    assert pedido_recuperado.descuento == 25
    assert pedido_recuperado.impuesto == 40.5
    assert pedido_recuperado.total == 265.5