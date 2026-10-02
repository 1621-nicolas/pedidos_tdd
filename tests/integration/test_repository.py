from app.models import Pedido
from app.repository import PedidoRepository


def test_guardar_y_recuperar_pedido(tmp_path):
    # Arrange
    db_path = tmp_path / "test_pedidos.db"
    repository = PedidoRepository(str(db_path))

    pedido = Pedido(
        tipo_cliente="VIP",
        productos=[
            {
                "nombre": "Teclado",
                "precio": 100,
                "cantidad": 2
            }
        ],
        subtotal=200,
        descuento=20,
        impuesto=32.4,
        total=212.4
    )

    # Act
    pedido_guardado = repository.guardar(pedido)
    pedido_recuperado = repository.obtener_por_id(pedido_guardado.id)

    # Assert
    assert pedido_guardado.id is not None
    assert pedido_recuperado is not None

    assert pedido_recuperado.id == pedido_guardado.id
    assert pedido_recuperado.tipo_cliente == "VIP"
    assert pedido_recuperado.subtotal == 200
    assert pedido_recuperado.descuento == 20
    assert pedido_recuperado.impuesto == 32.4
    assert pedido_recuperado.total == 212.4