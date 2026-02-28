@echo off
echo ========================================
echo St Patrick's College - Wagtail CMS
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Virtual environment not found!
    echo.
    echo Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        echo Make sure Python is installed and in PATH
        pause
        exit /b 1
    )
    echo Virtual environment created!
    echo.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if dependencies are installed
python -c "import django" 2>nul
if errorlevel 1 (
    echo Dependencies not installed!
    echo.
    echo Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
    echo Dependencies installed!
    echo.
)

REM Check if .env exists
if not exist ".env" (
    echo WARNING: .env file not found!
    echo.
    echo Creating .env file from template...
    if exist ".env.example" (
        copy .env.example .env
        echo .env file created. Please edit it with your database credentials.
        echo.
    ) else (
        echo Creating basic .env file...
        (
            echo SECRET_KEY=django-insecure-change-this-in-production
            echo DEBUG=True
            echo ALLOWED_HOSTS=localhost,127.0.0.1
            echo.
            echo DB_NAME=stpatricks_db
            echo DB_USER=postgres
            echo DB_PASSWORD=postgres
            echo DB_HOST=localhost
            echo DB_PORT=5432
            echo.
            echo WAGTAILADMIN_BASE_URL=http://localhost:8000
            echo BASE_URL=http://localhost:8000
        ) > .env
        echo .env file created. Please edit it with your database credentials.
        echo.
    )
)

REM Check if migrations have been run
python manage.py showmigrations 2>nul | findstr /C:"[ ]" >nul
if errorlevel 1 (
    echo.
    echo ========================================
    echo FIRST TIME SETUP REQUIRED
    echo ========================================
    echo.
    echo You need to:
    echo 1. Create PostgreSQL database
    echo 2. Update .env file with database credentials
    echo 3. Run migrations: python manage.py migrate
    echo 4. Create superuser: python manage.py createsuperuser
    echo 5. Collect static files: python manage.py collectstatic
    echo.
    echo Press any key to continue with migrations check...
    pause >nul
    echo.
)

echo ========================================
echo Starting Wagtail Development Server
echo ========================================
echo.
echo Server will start at: http://localhost:8000
echo Admin panel: http://localhost:8000/admin
echo.
echo Press CTRL+C to stop the server
echo.
echo ========================================
echo.

python manage.py runserver
