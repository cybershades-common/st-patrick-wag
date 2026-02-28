@echo off
echo Setting up St Patrick's College Wagtail Project...
echo.

echo Step 1: Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Failed to create virtual environment
    pause
    exit /b 1
)

echo Step 2: Activating virtual environment...
call venv\Scripts\activate.bat

echo Step 3: Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Failed to install dependencies
    pause
    exit /b 1
)

echo Step 4: Creating .env file if it doesn't exist...
if not exist .env (
    copy .env.example .env
    echo Please edit .env file with your database credentials
)

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Edit .env file with your database credentials
echo 2. Create PostgreSQL database
echo 3. Run: python manage.py migrate
echo 4. Run: python manage.py createsuperuser
echo 5. Run: python manage.py collectstatic
echo 6. Run: python manage.py runserver
echo.
pause
