$origen = "C:\Users\desarrollo\Verne Information Technology S.L\ENS 2022 - 2022 - ENS"
$destino = "D:\ENS"

Write-Host "Iniciando copia de archivos..."

$contador = 0
$totalArchivos = (Get-ChildItem -Path $origen -Recurse).Count

robocopy $origen $destino /E /COPY:DT /R:2 /W:2 /LOG:C:\ENS\copiado_log.txt

while ($contador -lt $totalArchivos) {
    $porcentaje = ($contador / $totalArchivos) * 100
    Write-Progress -Activity "Copia de archivos" -Status "Procesando archivos..." -PercentComplete $porcentaje
    Start-Sleep -Milliseconds 100
    $contador++
}

Write-Host "Copia de archivos finalizada"