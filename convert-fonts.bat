@echo off
REM Batch script to convert TTF fonts to WOFF2
REM This script runs the Python conversion script

echo Converting TTF fonts to WOFF2...
echo.

python convert-fonts-to-woff2.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Conversion completed successfully!
    pause
) else (
    echo.
    echo Conversion failed. Check the error messages above.
    pause
    exit /b %ERRORLEVEL%
)




