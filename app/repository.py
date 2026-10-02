import json
import sqlite3

from app.models import Pedido


class PedidoRepository:

    def __init__(self, db_path="pedidos.db"):
        self.db_path = db_path
        self._crear_tabla()

    def _conectar(self):
        return sqlite3.connect(self.db_path)

    def _crear_tabla(self):
        with self._conectar() as conexion:
            conexion.execute("""
                CREATE TABLE IF NOT EXISTS pedidos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo_cliente TEXT NOT NULL,
                    productos TEXT NOT NULL,
                    subtotal REAL NOT NULL,
                    descuento REAL NOT NULL,
                    impuesto REAL NOT NULL,
                    total REAL NOT NULL
                )
            """)

    def guardar(self, pedido):
        with self._conectar() as conexion:
            cursor = conexion.execute(
                """
                INSERT INTO pedidos (
                    tipo_cliente,
                    productos,
                    subtotal,
                    descuento,
                    impuesto,
                    total
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    pedido.tipo_cliente,
                    json.dumps(pedido.productos),
                    pedido.subtotal,
                    pedido.descuento,
                    pedido.impuesto,
                    pedido.total,
                ),
            )

            pedido.id = cursor.lastrowid

        return pedido

    def obtener_por_id(self, pedido_id):
        with self._conectar() as conexion:
            cursor = conexion.execute(
                """
                SELECT
                    id,
                    tipo_cliente,
                    productos,
                    subtotal,
                    descuento,
                    impuesto,
                    total
                FROM pedidos
                WHERE id = ?
                """,
                (pedido_id,),
            )

            fila = cursor.fetchone()

        if fila is None:
            return None

        return Pedido(
            id=fila[0],
            tipo_cliente=fila[1],
            productos=json.loads(fila[2]),
            subtotal=fila[3],
            descuento=fila[4],
            impuesto=fila[5],
            total=fila[6],
        )