from app.models import Pedido


DESCUENTO_VIP = 0.10
DESCUENTO_MAYORISTA_ALTO = 0.20
DESCUENTO_MAYORISTA_BAJO = 0.05
LIMITE_MAYORISTA = 500
TASA_IMPUESTO = 0.18


def validar_productos(productos):
    for producto in productos:
        if producto["cantidad"] < 0:
            raise ValueError("La cantidad no puede ser negativa")


def calcular_subtotal(productos):
    validar_productos(productos)

    return sum(
        producto["precio"] * producto["cantidad"]
        for producto in productos
    )


def calcular_descuento(subtotal, tipo_cliente):
    if tipo_cliente == "VIP":
        return subtotal * DESCUENTO_VIP

    if tipo_cliente == "MAYORISTA":
        if subtotal > LIMITE_MAYORISTA:
            return subtotal * DESCUENTO_MAYORISTA_ALTO

        return subtotal * DESCUENTO_MAYORISTA_BAJO

    return 0


def calcular_impuesto(monto_con_descuento):
    return monto_con_descuento * TASA_IMPUESTO


def calcular_total(monto_con_descuento, impuesto):
    return monto_con_descuento + impuesto


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
