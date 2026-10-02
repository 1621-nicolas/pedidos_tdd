from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

from app.pedido_service import PedidoService
from app.repository import PedidoRepository


class ProductoEntrada(BaseModel):
    nombre: str
    precio: float
    cantidad: int


class PedidoEntrada(BaseModel):
    tipo_cliente: str
    productos: list[ProductoEntrada]


def pedido_a_dict(pedido):
    return {
        "id": pedido.id,
        "tipo_cliente": pedido.tipo_cliente,
        "productos": pedido.productos,
        "subtotal": pedido.subtotal,
        "descuento": pedido.descuento,
        "impuesto": pedido.impuesto,
        "total": pedido.total,
    }


def crear_app(db_path="pedidos.db"):
    app = FastAPI(
        title="API de Pedidos",
        version="1.0.0"
    )

    repository = PedidoRepository(db_path)
    service = PedidoService(repository)

    @app.post(
        "/pedidos",
        status_code=status.HTTP_201_CREATED
    )
    def crear_pedido(datos: PedidoEntrada):
        try:
            productos = [
                producto.model_dump()
                for producto in datos.productos
            ]

            pedido = service.crear_pedido(
                productos,
                datos.tipo_cliente.upper()
            )

            return pedido_a_dict(pedido)

        except ValueError as error:
            raise HTTPException(
                status_code=400,
                detail=str(error)
            )

    @app.get("/pedidos/{pedido_id}")
    def obtener_pedido(pedido_id: int):
        pedido = service.obtener_pedido(pedido_id)

        if pedido is None:
            raise HTTPException(
                status_code=404,
                detail="Pedido no encontrado"
            )

        return pedido_a_dict(pedido)

    return app


app = crear_app()