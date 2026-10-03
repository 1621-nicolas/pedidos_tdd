from app.models import Pedido


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
