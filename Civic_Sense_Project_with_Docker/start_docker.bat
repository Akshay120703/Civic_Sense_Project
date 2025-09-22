@echo off
echo 🐳 Starting Civic Sense Project with Docker...
echo.

REM Check if Docker is running
docker version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not running. Please start Docker Desktop first.
    pause
    exit /b 1
)

echo ✅ Docker is running
echo.

REM Start the project
echo 🚀 Starting containers...
docker-compose up -d

if %errorlevel% equ 0 (
    echo.
    echo ✅ Project started successfully!
    echo.
    echo 🌐 Access your application at:
    echo    Main App: http://localhost:8080
    echo    phpMyAdmin: http://localhost:8081
    echo.
    echo 📋 To stop the project, run: docker-compose down
    echo 📋 To view logs, run: docker-compose logs
    echo.
    pause
) else (
    echo ❌ Failed to start the project
    echo 📋 Check the logs with: docker-compose logs
    pause
)
