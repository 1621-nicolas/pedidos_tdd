class FakePedidoRepository:
    def __init__(self):
        self._pedidos = {}
        self._siguiente_id = 1

    def guardar(self, pedido):
        pedido.id = self._siguiente_id
        self._pedidos[pedido.id] = pedido
        self._siguiente_id += 1
        return pedido

    def obtener_por_id(self, pedido_id):
        return self._pedidos.get(pedido_id)
