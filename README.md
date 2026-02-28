# St Patrick's College - Wagtail CMS Website

A comprehensive Wagtail CMS implementation of the St Patrick's College website, converted from a static HTML frontend to a fully content-managed system.

## Features

- **Wagtail CMS 6.0+** - Latest version of Wagtail
- **PostgreSQL Database** - Production-ready database
- **Content Holder System** - Manageable header and footer content
- **StreamField Blocks** - Flexible page content building
- **Responsive Design** - Mobile-first approach
- **Modern UI/UX** - Bootstrap 5 + Custom CSS
- **Animation Support** - GSAP ScrollTrigger animations

## Project Structure

```
st-patricks-wag/
├── assets/                 # Static assets (icons, images, videos, fonts)
├── src/                    # Source files (CSS, JS)
├── static/                 # Collected static files (Django)
├── media/                  # User uploaded files (Wagtail)
├── templates/             # Django/Wagtail templates
│   ├── base.html          # Base template
│   ├── includes/          # Header, footer, menu includes
│   ├── blocks/            # StreamField block templates
│   └── home/              # Page templates
├── stpatricks/            # Main Django project
│   ├── settings/         # Django settings (base, dev, production)
│   ├── urls.py           # URL configuration
│   └── wsgi.py           # WSGI application
├── home/                  # Home app
│   ├── models.py         # Page models
│   ├── blocks.py         # StreamField blocks
│   └── migrations/       # Database migrations
├── content_holders/       # Header/Footer content
│   ├── models.py         # Content holder models
│   └── migrations/       # Database migrations
├── menus/                 # Menu system
│   ├── models.py         # Menu models
│   └── migrations/       # Database migrations
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── setup_instructions.md # Detailed setup guide
```

## Quick Start

### 1. Prerequisites

- Python 3.10+
- PostgreSQL 12+
- pip and virtualenv

### 2. Setup Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Database

Create a PostgreSQL database:

```sql
CREATE DATABASE stpatricks_db;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE stpatricks_db TO postgres;
```

### 5. Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=stpatricks_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

WAGTAILADMIN_BASE_URL=http://localhost:8000
BASE_URL=http://localhost:8000
```

### 6. Run Migrations

```bash
python manage.py migrate
```

### 7. Create Superuser

```bash
python manage.py createsuperuser
```

### 8. Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### 9. Run Development Server

```bash
python manage.py runserver
```

Visit `http://localhost:8000` for the site and `http://localhost:8000/admin` for the admin.

## Content Management

### Header Content

Manage header settings via **Settings > Header Content**:
- Logo and logo text
- Book Tour and Enquire buttons
- Work with Us dropdown items
- Quick Links dropdown items

### Footer Content

Manage footer settings via **Settings > Footer Content**:
- College information
- Address and contact details
- Footer logos (Centenary, Old Boys, EREA)
- Explore links
- Quick links
- Social media links
- Footer bottom links
- Copyright and ABN

### Main Menu

Configure navigation via **Settings > Main Menu**:
- Create main menu items
- Add sub-menu items
- Link to pages or external URLs
- Add menu images

### Page Content

Pages use StreamField blocks for flexible content:
- **Hero Block** - Hero section with video/image
- **About Block** - About section with content and image
- **Strategic Block** - Strategic section with background image
- **Academics Block** - Academics section
- **Co-Curricular Block** - Co-curricular activities slider
- **Statistics Block** - Statistics cards
- **Parents Community Block** - Community section
- **Testimonials Block** - Testimonials slider
- **Latest News Block** - News items
- **CTA Block** - Call to action section

## Development

### Running Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Creating New Blocks

1. Add block class to `home/blocks.py`
2. Create template in `templates/blocks/`
3. Add to StreamField in `home/models.py`

### Static Files

Static files are served from:
- `static/` - Collected static files
- `assets/` - Original assets (copied to static during collectstatic)
- `src/` - Source CSS/JS files

## Production Deployment

1. Set `DEBUG=False` in production settings
2. Update `SECRET_KEY` with a secure random key
3. Configure proper database credentials
4. Set up static file serving (WhiteNoise, S3, or CDN)
5. Configure media file serving
6. Set proper `ALLOWED_HOSTS`
7. Use production WSGI server (Gunicorn)
8. Set up reverse proxy (Nginx)

## Technologies Used

- **Django 5.0+** - Web framework
- **Wagtail 6.0+** - CMS
- **PostgreSQL** - Database
- **Bootstrap 5** - CSS framework
- **GSAP** - Animation library
- **Swiper** - Slider library

## License

Copyright © 2025 St Patrick's College Strathfield

## Support

For setup assistance, refer to `setup_instructions.md` for detailed instructions.
