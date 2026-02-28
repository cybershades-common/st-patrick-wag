@echo off
echo ========================================
echo Checking Wagtail Status
echo ========================================
echo.

REM Check if virtual environment exists
if exist "venv\Scripts\activate.bat" (
    echo [OK] Virtual environment exists
) else (
    echo [X] Virtual environment NOT found
    echo     Run: python -m venv venv
)

REM Check if dependencies are installed
call venv\Scripts\activate.bat 2>nul
python -c "import django; import wagtail" 2>nul
if errorlevel 1 (
    echo [X] Dependencies NOT installed
    echo     Run: pip install -r requirements.txt
) else (
    echo [OK] Dependencies installed
)

REM Check if .env exists
if exist ".env" (
    echo [OK] .env file exists
) else (
    echo [X] .env file NOT found
    echo     Create .env file with database credentials
)

REM Check if migrations have been run
python manage.py showmigrations 2>nul | findstr /C:"[X]" >nul
if errorlevel 1 (
    echo [X] Migrations NOT run
    echo     Run: python manage.py migrate
) else (
    echo [OK] Migrations have been run
)

REM Check if server is running
curl -s http://localhost:8000/admin >nul 2>&1
if errorlevel 1 (
    echo [X] Server is NOT running
    echo     Run: python manage.py runserver
    echo     Or use: START_WAGTAIL.bat
) else (
    echo [OK] Server appears to be running
    echo     Admin: http://localhost:8000/admin
    echo     Site: http://localhost:8000
)

echo.
echo ========================================
echo Status Check Complete
echo ========================================
pause
