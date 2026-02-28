@echo off
echo ========================================
echo PostgreSQL Database Setup
echo ========================================
echo.
echo This script will help you create the database.
echo.
echo Option 1: Create database using psql command
echo Option 2: Use SQLite for development (easier)
echo.
set /p choice="Enter choice (1 or 2): "

if "%choice%"=="1" goto create_postgres
if "%choice%"=="2" goto use_sqlite
goto end

:create_postgres
echo.
echo Creating PostgreSQL database...
echo.
echo You need to run this SQL command in PostgreSQL:
echo.
echo CREATE DATABASE stpatricks_db;
echo CREATE USER postgres WITH PASSWORD 'postgres';
echo GRANT ALL PRIVILEGES ON DATABASE stpatricks_db TO postgres;
echo.
echo You can do this by:
echo 1. Opening pgAdmin
echo 2. Or running: psql -U postgres
echo 3. Then executing the SQL commands above
echo.
echo After creating the database, make sure your .env file has:
echo DB_NAME=stpatricks_db
echo DB_USER=postgres
echo DB_PASSWORD=postgres
echo DB_HOST=localhost
echo DB_PORT=5432
echo.
pause
goto end

:use_sqlite
echo.
echo Switching to SQLite for development...
echo.
echo This will update your settings to use SQLite instead of PostgreSQL.
echo SQLite is easier for development but PostgreSQL is needed for production.
echo.
set /p confirm="Continue with SQLite? (y/n): "
if /i not "%confirm%"=="y" goto end

echo.
echo Updating settings to use SQLite...
echo.
REM Create a dev_sqlite.py settings file
(
echo from .base import *
echo.
echo # Use SQLite for development
echo DATABASES = {
echo     'default': {
echo         'ENGINE': 'django.db.backends.sqlite3',
echo         'NAME': BASE_DIR / 'db.sqlite3',
echo     }
echo }
) > stpatricks\settings\dev_sqlite.py

echo Settings file created: stpatricks\settings\dev_sqlite.py
echo.
echo To use SQLite, update manage.py to use dev_sqlite instead of dev:
echo Change: stpatricks.settings.dev
echo To: stpatricks.settings.dev_sqlite
echo.
pause
goto end

:end
echo.
echo Done!
echo.
