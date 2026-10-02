from app.pedido_service import (
    calcular_subtotal,
    calcular_descuento,
    calcular_impuesto,
    calcular_total
)
import pytest

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

def test_calcular_impuesto_y_total():
    # Arrange
    subtotal = 200
    descuento = 20
    monto_con_descuento = subtotal - descuento

    # Act
    impuesto = calcular_impuesto(monto_con_descuento)
    total = calcular_total(monto_con_descuento, impuesto)

    # Assert
    assert impuesto == pytest.approx(32.40)
    assert total == pytest.approx(212.40)

def test_descuento_cliente_regular():
    # Arrange
    subtotal = 300
    tipo_cliente = "REGULAR"

    # Act
    descuento = calcular_descuento(subtotal, tipo_cliente)

    # Assert
    assert descuento == 0
def test_calcular_subtotal_con_cantidad_negativa():
    # Arrange
    productos = [
        {
            "nombre": "Teclado",
            "precio": 100,
            "cantidad": -2
        }
    ]

    # Act / Assert
    with pytest.raises(ValueError):
        calcular_subtotal(productos)