# Quick Start Guide

## Windows Setup (PowerShell)

```powershell
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file (copy from .env.example and edit)
# Edit .env with your database credentials

# 5. Create PostgreSQL database
# Use pgAdmin or psql:
# CREATE DATABASE stpatricks_db;

# 6. Run migrations
python manage.py migrate

# 7. Create superuser
python manage.py createsuperuser

# 8. Collect static files
python manage.py collectstatic --noinput

# 9. Run server
python manage.py runserver
```

## macOS/Linux Setup

```bash
# 1. Create virtual environment
python3 -m venv venv

# 2. Activate virtual environment
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file
cp .env.example .env
# Edit .env with your database credentials

# 5. Create PostgreSQL database
createdb stpatricks_db
# Or use psql:
# CREATE DATABASE stpatricks_db;

# 6. Run migrations
python manage.py migrate

# 7. Create superuser
python manage.py createsuperuser

# 8. Collect static files
python manage.py collectstatic --noinput

# 9. Run server
python manage.py runserver
```

## First Time Admin Setup

1. Visit `http://localhost:8000/admin`
2. Log in with your superuser credentials
3. Go to **Settings > Sites** and create a site
4. Go to **Pages** and create a Home Page
5. Go to **Settings > Header Content** and configure header
6. Go to **Settings > Footer Content** and configure footer
7. Go to **Settings > Main Menu** and set up navigation

## Access Points

- **Website**: http://localhost:8000
- **Admin Panel**: http://localhost:8000/admin
- **Wagtail Admin**: http://localhost:8000/admin (same as above)

## Common Commands

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Run development server
python manage.py runserver

# Run with custom port
python manage.py runserver 8080
```

## Troubleshooting

### Database Connection Error
- Check PostgreSQL is running
- Verify credentials in `.env` file
- Ensure database exists

### Static Files Not Loading
- Run `python manage.py collectstatic`
- Check `STATIC_URL` in settings
- Verify files in `static/` directory

### Module Not Found
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt`
- Check Python version (3.10+)

### Port Already in Use
- Use different port: `python manage.py runserver 8080`
- Or stop the process using port 8000
