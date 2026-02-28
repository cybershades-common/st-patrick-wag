# Quick Start Guide - Get Wagtail Running

## Is Wagtail Running?

**Check by opening your browser:**
- Try: **http://localhost:8000/admin**
- If you see a login page → Wagtail IS running ✅
- If you see "This site can't be reached" → Wagtail is NOT running ❌

## Get Wagtail Running (Windows)

### Option 1: Use the Batch File (Easiest)

1. **Double-click**: `START_WAGTAIL.bat`
2. It will:
   - Create virtual environment (if needed)
   - Install dependencies (if needed)
   - Start the server
3. Open browser: **http://localhost:8000/admin**

### Option 2: Manual Steps

1. **Open Command Prompt** in the project folder

2. **Create virtual environment** (first time only):
   ```cmd
   python -m venv venv
   ```

3. **Activate virtual environment**:
   ```cmd
   venv\Scripts\activate
   ```

4. **Install dependencies** (first time only):
   ```cmd
   pip install -r requirements.txt
   ```

5. **Create .env file** (first time only):
   - Copy `.env.example` to `.env`
   - Edit `.env` with your database credentials

6. **Set up database** (first time only):
   - Create PostgreSQL database
   - Update `.env` with database info

7. **Run migrations** (first time only):
   ```cmd
   python manage.py migrate
   ```

8. **Create superuser** (first time only):
   ```cmd
   python manage.py createsuperuser
   ```
   (Enter username, email, password)

9. **Collect static files** (first time only):
   ```cmd
   python manage.py collectstatic --noinput
   ```

10. **Start server**:
    ```cmd
    python manage.py runserver
    ```

11. **Open browser**:
    - Admin: http://localhost:8000/admin
    - Site: http://localhost:8000

## Adding Content - Quick Steps

### 1. Log In
- Go to: http://localhost:8000/admin
- Enter your superuser credentials

### 2. Set Up Header (Settings > Header Content)
- Upload logo
- Set button texts and links
- Add dropdown items

### 3. Set Up Footer (Settings > Footer Content)
- Fill in address and contact
- Upload logos
- Add links

### 4. Set Up Menu (Settings > Main Menu)
- Add menu items
- Link to pages

### 5. Create Home Page (Pages > Add child page)
- Select "Home Page"
- Add blocks in Body section
- Publish

### 6. Upload Images (Images menu)
- Upload all your images
- They'll be available in blocks

## Common Issues

### "Module not found" error
**Solution**: Activate virtual environment first
```cmd
venv\Scripts\activate
```

### "Database connection" error
**Solution**: 
- Check PostgreSQL is running
- Verify `.env` file has correct database credentials
- Make sure database exists

### "Static files not found" error
**Solution**: Run collectstatic
```cmd
python manage.py collectstatic --noinput
```

### Port 8000 already in use
**Solution**: Use different port
```cmd
python manage.py runserver 8080
```

## Need More Help?

- **Detailed Setup**: See `setup_instructions.md`
- **Adding Content**: See `HOW_TO_ADD_CONTENT.md`
- **Wagtail Setup**: See `WAGTAIL_SETUP.md`

## Quick Commands Reference

```cmd
# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic

# Start server
python manage.py runserver

# Check status
python manage.py check
```

---

**Ready to add content?** See `HOW_TO_ADD_CONTENT.md` for detailed instructions!
