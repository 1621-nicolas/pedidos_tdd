from fastapi.testclient import TestClient

from app.main import crear_app


def crear_cliente_prueba(tmp_path):
    db_path = tmp_path / "test_api.db"
    app = crear_app(str(db_path))
    return TestClient(app)


def test_post_pedidos_crea_pedido(tmp_path):
    # Arrange
    client = crear_cliente_prueba(tmp_path)

    datos = {
        "tipo_cliente": "VIP",
        "productos": [
            {
                "nombre": "Teclado",
                "precio": 100,
                "cantidad": 2
            },
            {
                "nombre": "Mouse",
                "precio": 50,
                "cantidad": 1
            }
        ]
    }

    # Act
    response = client.post("/pedidos", json=datos)

    # Assert
    assert response.status_code == 201

    pedido = response.json()

    assert pedido["id"] is not None
    assert pedido["tipo_cliente"] == "VIP"
    assert pedido["subtotal"] == 250
    assert pedido["descuento"] == 25
    assert pedido["impuesto"] == 40.5
    assert pedido["total"] == 265.5


def test_get_pedido_existente(tmp_path):
    # Arrange
    client = crear_cliente_prueba(tmp_path)

    datos = {
        "tipo_cliente": "REGULAR",
        "productos": [
            {
                "nombre": "Monitor",
                "precio": 300,
                "cantidad": 1
            }
        ]
    }

    pedido_creado = client.post("/pedidos", json=datos).json()

    # Act
    response = client.get(f"/pedidos/{pedido_creado['id']}")

    # Assert
    assert response.status_code == 200

    pedido = response.json()

    assert pedido["id"] == pedido_creado["id"]
    assert pedido["tipo_cliente"] == "REGULAR"
    assert pedido["subtotal"] == 300
    assert pedido["total"] == 354


def test_get_pedido_inexistente_devuelve_404(tmp_path):
    # Arrange
    client = crear_cliente_prueba(tmp_path)

    # Act
    response = client.get("/pedidos/999")

    # Assert
    assert response.status_code == 404


def test_post_pedido_con_cantidad_negativa_devuelve_400(tmp_path):
    # Arrange
    client = crear_cliente_prueba(tmp_path)

    datos = {
        "tipo_cliente": "VIP",
        "productos": [
            {
                "nombre": "Teclado",
                "precio": 100,
                "cantidad": -2
            }
        ]
    }

    # Act
    response = client.post("/pedidos", json=datos)

    # Assert
    assert response.status_code == 400