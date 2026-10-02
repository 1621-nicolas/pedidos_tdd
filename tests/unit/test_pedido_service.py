from app.pedido_service import calcular_subtotal, calcular_descuento

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
def test_descuento_cliente_vip():
    # Arrange
    subtotal = 200
    tipo_cliente = "VIP"

    # Act
    descuento = calcular_descuento(subtotal, tipo_cliente)

    # Assert
    assert descuento == 20
def test_descuento_mayorista_menor_a_500():
    # Arrange
    subtotal = 400
    tipo_cliente = "MAYORISTA"

    # Act
    descuento = calcular_descuento(subtotal, tipo_cliente)

    # Assert
    assert descuento == 20


def test_descuento_mayorista_exactamente_500():
    # Arrange
    subtotal = 500
    tipo_cliente = "MAYORISTA"

    # Act
    descuento = calcular_descuento(subtotal, tipo_cliente)

    # Assert
    assert descuento == 25


def test_descuento_mayorista_mayor_a_500():
    # Arrange
    subtotal = 600
    tipo_cliente = "MAYORISTA"

    # Act
    descuento = calcular_descuento(subtotal, tipo_cliente)

    # Assert
    assert descuento == 120