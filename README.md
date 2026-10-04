# Módulo de Pedidos con TDD, Pruebas Unitarias, de Integración y Automatización

## Descripción

Este proyecto implementa un módulo de procesamiento de pedidos para una plataforma de comercio electrónico. La solución fue desarrollada aplicando TDD (Test-Driven Development) y cubre lógica de negocio, persistencia, API REST, pruebas unitarias, pruebas de integración, test doubles, automatización y cobertura.

El módulo permite calcular el subtotal de un pedido, aplicar descuentos según el tipo de cliente, calcular el impuesto del 18 %, obtener el total final, persistir pedidos con un identificador único y recuperarlos mediante una API REST.

## Tecnologías utilizadas

- Python
- pytest
- pytest-cov
- FastAPI
- SQLite
- Git
- GitHub Actions

Se eligió Python junto con pytest porque permite escribir pruebas de forma clara y directa, facilita la aplicación del patrón AAA y dispone de herramientas sencillas para pruebas unitarias, integración y cobertura. FastAPI se utilizó para exponer los endpoints REST y SQLite para implementar una persistencia real sin requerir un servidor de base de datos externo.

## Reglas de negocio

| Regla | Comportamiento |
|---|---|
| Subtotal | Suma de precio × cantidad de cada producto |
| Cliente REGULAR | Sin descuento |
| Cliente VIP | 10 % de descuento sobre el subtotal |
| Cliente MAYORISTA | 20 % si el subtotal es mayor a 500; de lo contrario 5 % |
| Impuesto | 18 % sobre el monto después del descuento |
| Total | Monto con descuento + impuesto |
| Cantidad negativa | Genera un error de validación |
| Persistencia | Cada pedido se guarda con un ID único |

## Estructura del proyecto

```text
pedidos_tdd/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── pedido_service.py
│   └── repository.py
├── tests/
│   ├── integration/
│   │   ├── test_api.py
│   │   ├── test_pedido_service_integration.py
│   │   └── test_repository.py
│   ├── unit/
│   │   ├── test_pedido_service.py
│   │   └── test_pedido_service_fake.py
│   ├── fakes.py
│   └── test_framework.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── requirements.txt
├── run_tests.ps1
└── README.md
```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/1621-nicolas/pedidos_tdd.git
cd pedidos_tdd
```

Crear el entorno virtual:

### Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Instalar las dependencias:

```powershell
pip install -r requirements.txt
```

## Ejecución de pruebas

Para ejecutar toda la suite:

```powershell
pytest -v
```

La suite incluye pruebas unitarias, pruebas con FakeRepository y pruebas de integración con SQLite y FastAPI.

## Automatización y cobertura

El proyecto incluye el script:

```text
run_tests.ps1
```

Para ejecutarlo:

```powershell
.\run_tests.ps1
```

El script:

- ejecuta todas las pruebas;
- genera cobertura en terminal;
- genera un reporte HTML;
- devuelve un código de salida distinto de cero si alguna prueba falla.

El reporte HTML se genera en:

```text
htmlcov/index.html
```

Para abrirlo en Windows:

```powershell
Start-Process .\htmlcov\index.html
```

## Cobertura obtenida

La ejecución automatizada alcanzó una cobertura total del 100 % sobre el paquete `app`.

| Archivo | Sentencias | Sin cubrir | Cobertura |
|---|---:|---:|---:|
| app/__init__.py | 0 | 0 | 100 % |
| app/main.py | 33 | 0 | 100 % |
| app/models.py | 11 | 0 | 100 % |
| app/pedido_service.py | 40 | 0 | 100 % |
| app/repository.py | 24 | 0 | 100 % |
| **TOTAL** | **108** | **0** | **100 %** |

## API REST

Iniciar la aplicación:

```powershell
uvicorn app.main:app --reload
```

La documentación interactiva de FastAPI queda disponible en:

```text
http://127.0.0.1:8000/docs
```

### POST /pedidos

Crea y persiste un pedido.

Ejemplo:

```json
{
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
```

Respuesta esperada:

```json
{
  "id": 1,
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
  ],
  "subtotal": 250,
  "descuento": 25,
  "impuesto": 40.5,
  "total": 265.5
}
```

### GET /pedidos/{id}

Recupera un pedido por su identificador.

Si el pedido no existe, la API devuelve HTTP 404.

Si se intenta crear un pedido con una cantidad negativa, la API devuelve HTTP 400.

## Casos de prueba implementados

| Tipo | Prueba | Propósito |
|---|---|---|
| Unitaria | test_framework_funciona | Verificar la configuración inicial de pytest |
| Unitaria | test_calcular_subtotal_pedido_vacio | Validar subtotal 0 para lista vacía |
| Unitaria | test_calcular_subtotal_con_productos | Validar suma de precio × cantidad |
| Unitaria | test_descuento_cliente_vip | Validar descuento VIP del 10 % |
| Unitaria | test_descuento_mayorista_menor_a_500 | Validar 5 % para mayorista por debajo de 500 |
| Unitaria | test_descuento_mayorista_exactamente_500 | Validar el caso límite de subtotal igual a 500 |
| Unitaria | test_descuento_mayorista_mayor_a_500 | Validar 20 % para mayorista por encima de 500 |
| Unitaria | test_calcular_impuesto_y_total | Validar impuesto y total |
| Unitaria | test_descuento_cliente_regular | Validar ausencia de descuento |
| Unitaria | test_calcular_subtotal_con_cantidad_negativa | Validar rechazo de cantidades negativas |
| Unitaria con fake | test_crear_y_recuperar_pedido_con_fake_repository | Aislar el servicio de la persistencia real |
| Integración | test_guardar_y_recuperar_pedido | Validar SQLite |
| Integración | test_pedido_persiste_en_nueva_instancia_del_repositorio | Validar persistencia real |
| Integración | test_obtener_pedido_inexistente_devuelve_none | Validar consulta inexistente |
| Integración | test_guardar_dos_pedidos_asigna_ids_unicos | Validar IDs únicos |
| Integración | test_crear_y_recuperar_pedido_desde_servicio | Validar servicio + SQLite |
| API | test_post_pedidos_crea_pedido | Validar POST /pedidos |
| API | test_get_pedido_existente | Validar GET /pedidos/{id} |
| API | test_get_pedido_inexistente_devuelve_404 | Validar HTTP 404 |
| API | test_post_pedido_con_cantidad_negativa_devuelve_400 | Validar HTTP 400 |

Actualmente la solución contiene 20 pruebas.

## TDD y ciclo RED-GREEN-REFACTOR

El historial de Git evidencia el desarrollo guiado por pruebas. Primero se agregaron pruebas que representaban el comportamiento esperado (RED), después se implementó el código mínimo necesario para hacerlas pasar (GREEN) y finalmente se realizaron refactorizaciones sin alterar el comportamiento observado por las pruebas.

Entre las refactorizaciones realizadas se encuentran la separación de la validación del cálculo del subtotal, el reemplazo de valores mágicos por constantes de negocio, la extracción de la selección del porcentaje de descuento, la extracción del cálculo del monto con descuento y la encapsulación de la generación de IDs del FakeRepository.

Ejemplos de commits:

```text
test: agregar prueba RED para subtotal de pedido vacio
feat: implementar subtotal cero para pedido vacio

test: agregar prueba RED para subtotal con productos
feat: implementar calculo de subtotal con productos

test: agregar prueba RED para descuento cliente VIP
feat: implementar descuento del 10 por ciento para cliente VIP

test: agregar pruebas RED para descuento mayorista
feat: implementar descuento mayorista segun subtotal

test: agregar prueba RED para impuesto y total
feat: implementar calculo de impuesto y total

refactor: separar validacion del calculo de subtotal
refactor: reemplazar valores magicos por constantes de negocio
refactor: aislar seleccion del porcentaje de descuento
refactor: extraer calculo del monto con descuento
refactor: encapsular generacion de IDs del FakeRepository
```

## Integración continua

El archivo:

```text
.github/workflows/tests.yml
```

configura GitHub Actions para ejecutar las pruebas y generar el reporte de cobertura automáticamente en cada push y pull request.

El workflow instala las dependencias, ejecuta pytest con cobertura y publica el reporte HTML como artefacto.

## Reflexión

Al aplicar TDD aprendí a escribir las pruebas antes de desarrollar el código de producción y a pensar primero en el comportamiento esperado de cada función. El ciclo RED permitió comprobar que cada prueba detectaba realmente una funcionalidad todavía no implementada. En la fase GREEN se agregó únicamente el código necesario para hacer pasar las pruebas. Posteriormente, la fase REFACTOR permitió mejorar la estructura del código sin modificar su comportamiento.

Una de las principales dificultades fue manejar correctamente los descuentos según el tipo de cliente y comprobar los casos límite, especialmente el subtotal exactamente igual a 500. También fue necesario organizar correctamente la persistencia para que las pruebas fueran repetibles y no dependieran de información generada anteriormente.

pytest facilitó la ejecución y lectura de los resultados, mientras que pytest-cov permitió medir la cobertura del código. El uso de un FakeRepository permitió comprobar la lógica del servicio sin depender de SQLite. Las pruebas de integración confirmaron que los componentes reales podían trabajar juntos y las pruebas de API permitieron verificar las respuestas HTTP.

El desarrollo permitió comprobar que una suite de pruebas automatizada brinda mayor confianza al modificar o refactorizar el código. Además, la integración con GitHub Actions permite verificar automáticamente que el proyecto continúa funcionando después de nuevos cambios.

## Repositorio

Repositorio del proyecto:

https://github.com/1621-nicolas/pedidos_tdd
