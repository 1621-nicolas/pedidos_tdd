def calcular_subtotal(productos):
    subtotal = 0

    for producto in productos:
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