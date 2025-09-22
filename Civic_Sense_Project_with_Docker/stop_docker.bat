@echo off
echo 🛑 Stopping Civic Sense Project...
echo.

REM Stop the project
docker-compose down

if %errorlevel% equ 0 (
    echo ✅ Project stopped successfully!
    echo.
    echo 📋 To start again, run: start_docker.bat
    echo 📋 To remove all data, run: docker-compose down -v
) else (
    echo ❌ Failed to stop the project
    echo 📋 Try running: docker-compose down --remove-orphans
)

echo.
pause
