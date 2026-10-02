def calcular_subtotal(productos):
    subtotal = 0

    for producto in productos:
        subtotal += producto["precio"] * producto["cantidad"]

    return subtotal