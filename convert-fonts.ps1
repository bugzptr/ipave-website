# PowerShell script to convert TTF fonts to WOFF2
# This script runs the Python conversion script

Write-Host "Converting TTF fonts to WOFF2..." -ForegroundColor Cyan
Write-Host ""

python convert-fonts-to-woff2.py

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "Conversion completed successfully!" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "Conversion failed. Check the error messages above." -ForegroundColor Red
    exit $LASTEXITCODE
}



