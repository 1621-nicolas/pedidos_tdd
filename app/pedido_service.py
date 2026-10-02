def calcular_subtotal(productos):
    subtotal = 0

    for producto in productos:
        subtotal += producto["precio"] * producto["cantidad"]

    return subtotal
def calcular_descuento(subtotal, tipo_cliente):
    if tipo_cliente == "VIP":
        return subtotal * 0.10

    return 0