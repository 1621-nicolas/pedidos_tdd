from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Pedido:
    tipo_cliente: str
    productos: list
    subtotal: float
    descuento: float
    impuesto: float
    total: float
    id: Optional[int] = field(default=None)