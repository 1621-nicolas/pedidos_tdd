from app.pedido_service import calcular_subtotal


def test_calcular_subtotal_pedido_vacio():
    # Arrange
    productos = []

    # Act
    subtotal = calcular_subtotal(productos)

    # Assert
    assert subtotal == 0