if (Test-Path "docs\index.html") {
    Write-Host "El archivo de despliegue fue generado correctamente."
} else {
    Write-Error "No existe docs\index.html"
    exit 1
}