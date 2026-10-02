from app.pedido_service import calcular_subtotal


def test_calcular_subtotal_pedido_vacio():
    # Arrange
    productos = []

    # Act
    subtotal = calcular_subtotal(productos)

    # Assert
    assert subtotal == 0

def test_calcular_subtotal_con_productos():
    # Arrange
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
    subtotal = calcular_subtotal(productos)

    # Assert
    assert subtotal == 250