# Database Setup Guide

## The Error

You're getting this error:
```
FATAL: database "stpatricks_db" does not exist
```

This means PostgreSQL database hasn't been created yet.

## Solution Options

### Option 1: Use SQLite (Easiest - Recommended for Development)

SQLite is easier to set up and perfect for development. You can switch to PostgreSQL later for production.

**Steps:**

1. **Update manage.py** to use SQLite settings:
   ```python
   # Change this line in manage.py:
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stpatricks.settings.dev')
   
   # To this:
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stpatricks.settings.dev_sqlite')
   ```

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

3. **Done!** No database setup needed.

**Note:** SQLite file (`db.sqlite3`) will be created automatically in your project root.

### Option 2: Create PostgreSQL Database

If you want to use PostgreSQL (required for production):

#### Method A: Using pgAdmin (GUI)

1. Open **pgAdmin**
2. Connect to your PostgreSQL server
3. Right-click on **Databases** → **Create** → **Database**
4. Name: `stpatricks_db`
5. Click **Save**

#### Method B: Using psql (Command Line)

1. Open Command Prompt or PowerShell
2. Connect to PostgreSQL:
   ```bash
   psql -U postgres
   ```
3. Enter your PostgreSQL password
4. Run these commands:
   ```sql
   CREATE DATABASE stpatricks_db;
   CREATE USER postgres WITH PASSWORD 'postgres';
   GRANT ALL PRIVILEGES ON DATABASE stpatricks_db TO postgres;
   \q
   ```

#### Method C: Using SQL Command File

1. Create a file `create_db.sql`:
   ```sql
   CREATE DATABASE stpatricks_db;
   CREATE USER postgres WITH PASSWORD 'postgres';
   GRANT ALL PRIVILEGES ON DATABASE stpatricks_db TO postgres;
   ```

2. Run it:
   ```bash
   psql -U postgres -f create_db.sql
   ```

### After Creating Database

1. **Make sure `.env` file has correct settings:**
   ```env
   DB_NAME=stpatricks_db
   DB_USER=postgres
   DB_PASSWORD=postgres
   DB_HOST=localhost
   DB_PORT=5432
   ```

2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

## Quick Fix Script

I've created `CREATE_DATABASE.bat` to help you choose between options.

Just run:
```bash
CREATE_DATABASE.bat
```

## Recommended Approach

**For Development:** Use SQLite (Option 1) - it's much easier!
- No database server needed
- No configuration needed
- Works immediately
- Perfect for local development

**For Production:** Use PostgreSQL (Option 2)
- Better performance
- More features
- Required for production deployments

## Troubleshooting

### PostgreSQL not running
- Start PostgreSQL service
- Check if it's installed
- Verify connection settings

### Permission denied
- Check PostgreSQL user permissions
- Verify password in `.env` file
- Make sure user has CREATE DATABASE privilege

### Port 5432 in use
- Check if another PostgreSQL instance is running
- Change port in `.env` if needed

## Next Steps After Database Setup

1. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```

3. **Collect static files:**
   ```bash
   python manage.py collectstatic --noinput
   ```

4. **Start server:**
   ```bash
   python manage.py runserver
   ```
