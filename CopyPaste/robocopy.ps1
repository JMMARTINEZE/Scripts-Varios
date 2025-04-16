$origen = "C:\Users\desarrollo\Verne Information Technology S.L\ISO 27001 2022 - Proyecto ISO 27001 v.2022"
$destino = "D:\ISO"

Write-Host "Iniciando copia de archivos..."

robocopy $origen $destino /E /COPY:DT /R:2 /W:2 /LOG+:D:\ISO\copiado_log.txt

Write-Host "Copia de archivos finalizada"