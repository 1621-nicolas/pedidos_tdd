from app.models import Pedido

def calcular_subtotal(productos):
    subtotal = 0

    for producto in productos:
        if producto["cantidad"] < 0:
            raise ValueError("La cantidad no puede ser negativa")

        subtotal += producto["precio"] * producto["cantidad"]

    return subtotal
def calcular_descuento(subtotal, tipo_cliente):
    if tipo_cliente == "VIP":
        return subtotal * 0.10

    if tipo_cliente == "MAYORISTA":
        if subtotal > 500:
            return subtotal * 0.20

        return subtotal * 0.05

    return 0

def calcular_impuesto(monto_con_descuento):
    return monto_con_descuento * 0.18


def calcular_total(monto_con_descuento, impuesto):
    return monto_con_descuento + impuesto


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

class PedidoService:

    def __init__(self, repository):
        self.repository = repository

    def crear_pedido(self, productos, tipo_cliente):
        subtotal = calcular_subtotal(productos)
        descuento = calcular_descuento(subtotal, tipo_cliente)

        monto_con_descuento = subtotal - descuento

        impuesto = calcular_impuesto(monto_con_descuento)
        total = calcular_total(monto_con_descuento, impuesto)

        pedido = Pedido(
            tipo_cliente=tipo_cliente,
            productos=productos,
            subtotal=subtotal,
            descuento=descuento,
            impuesto=impuesto,
            total=total
        )

        return self.repository.guardar(pedido)

    def obtener_pedido(self, pedido_id):
        return self.repository.obtener_por_id(pedido_id)