$ErrorActionPreference = "Stop"

Write-Host "========================================"
Write-Host " EJECUTANDO PRUEBAS DEL PROYECTO"
Write-Host "========================================"

pytest `
    --cov=app `
    --cov-report=term-missing `
    --cov-report=html `
    -v

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "LAS PRUEBAS FALLARON"
    exit 1
}

Write-Host ""
Write-Host "========================================"
Write-Host " TODAS LAS PRUEBAS PASARON"
Write-Host "========================================"
Write-Host ""
Write-Host "Reporte HTML generado en:"
Write-Host "htmlcov/index.html"

exit 0