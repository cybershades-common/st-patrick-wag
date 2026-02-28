# St Patrick's College - Wagtail CMS Setup Instructions

## Prerequisites

- Python 3.10 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- virtualenv (or venv)

## Step 1: Create Virtual Environment

```bash
# On Windows
python -m venv venv

# Activate virtual environment
# On Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# On Windows (Command Prompt)
venv\Scripts\activate.bat

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Set Up PostgreSQL Database

1. Create a PostgreSQL database:
```sql
CREATE DATABASE stpatricks_db;
CREATE USER postgres WITH PASSWORD 'postgres';
GRANT ALL PRIVILEGES ON DATABASE stpatricks_db TO postgres;
```

2. Or update database settings in `.env` file (create from `.env.example`):
```
DB_NAME=stpatricks_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## Step 4: Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Django Settings
SECRET_KEY=your-secret-key-here-change-this-in-production
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Settings
DB_NAME=stpatricks_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

# Wagtail Settings
WAGTAILADMIN_BASE_URL=http://localhost:8000
BASE_URL=http://localhost:8000
```

## Step 5: Run Migrations

```bash
python manage.py migrate
```

## Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

## Step 7: Collect Static Files

```bash
python manage.py collectstatic --noinput
```

## Step 8: Copy Static Assets

Copy your existing static files to the static directory:

```bash
# The assets folder should be copied to static/assets
# The src folder should be copied to static/src
```

## Step 9: Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` to see your site.

Visit `http://localhost:8000/admin` to access the Wagtail admin.

## Step 10: Initial Setup in Wagtail Admin

1. Log in to the Wagtail admin at `/admin`
2. Go to Settings > Header Content and configure your header
3. Go to Settings > Footer Content and configure your footer
4. Go to Settings > Main Menu and set up your navigation menu
5. Create a Home Page:
   - Go to Pages
   - Click "Add child page"
   - Select "Home Page"
   - Fill in the title and add content blocks
   - Publish the page

## Project Structure

```
st-patricks-wag/
├── assets/              # Static assets (icons, images, videos, fonts)
├── src/                 # Source files (CSS, JS)
├── static/              # Collected static files (Django)
├── media/               # User uploaded files (Wagtail)
├── templates/            # Django/Wagtail templates
│   ├── base.html
│   ├── includes/
│   └── blocks/
├── stpatricks/          # Main Django project
│   ├── settings/
│   ├── urls.py
│   └── wsgi.py
├── home/                # Home app
│   ├── models.py
│   ├── blocks.py
│   └── migrations/
├── content_holders/     # Header/Footer content
│   ├── models.py
│   └── migrations/
├── menus/               # Menu system
│   ├── models.py
│   └── migrations/
├── manage.py
└── requirements.txt
```

## Content Management

### Header Content
- Accessible via Settings > Header Content
- Configure logo, buttons, dropdown menus
- Work with Us and Quick Links items

### Footer Content
- Accessible via Settings > Footer Content
- Configure address, contact info, links
- Social media links
- Footer logos

### Main Menu
- Accessible via Settings > Main Menu
- Create menu items with sub-items
- Link to pages or external URLs

### Pages
- Create pages using the Wagtail admin
- Use StreamField blocks to build page content
- Available blocks:
  - Hero Block
  - About Block
  - Strategic Block
  - Academics Block
  - Co-Curricular Block
  - Statistics Block
  - Parents Community Block
  - Testimonials Block
  - Latest News Block
  - CTA Block

## Production Deployment

1. Set `DEBUG=False` in production settings
2. Update `SECRET_KEY` with a secure random key
3. Configure proper database credentials
4. Set up static file serving (e.g., WhiteNoise, S3, CDN)
5. Configure media file serving
6. Set up proper ALLOWED_HOSTS
7. Use a production WSGI server (e.g., Gunicorn)
8. Set up reverse proxy (e.g., Nginx)

## Troubleshooting

### Database Connection Issues
- Verify PostgreSQL is running
- Check database credentials in `.env`
- Ensure database exists

### Static Files Not Loading
- Run `python manage.py collectstatic`
- Check `STATIC_URL` and `STATIC_ROOT` settings
- Verify static files are in the correct directories

### Template Errors
- Check that all template tags are loaded correctly
- Verify context processors are in settings
- Check template paths in `TEMPLATES` setting
