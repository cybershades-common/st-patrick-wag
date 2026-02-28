# Setup Checklist

Use this checklist to ensure everything is set up correctly.

## Pre-Setup

- [ ] Python 3.10+ installed
- [ ] PostgreSQL installed and running
- [ ] Virtual environment created
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)

## Database Setup

- [ ] PostgreSQL database created
- [ ] Database user created with proper permissions
- [ ] `.env` file created with database credentials
- [ ] `.env` file configured with SECRET_KEY
- [ ] Migrations run (`python manage.py migrate`)
- [ ] Superuser created (`python manage.py createsuperuser`)

## Static Files

- [ ] Static files collected (`python manage.py collectstatic`)
- [ ] `assets/` folder accessible (copied to `static/` or in `STATICFILES_DIRS`)
- [ ] `src/` folder accessible (copied to `static/` or in `STATICFILES_DIRS`)
- [ ] Static files loading correctly in browser

## Wagtail Admin Setup

- [ ] Can access admin at `/admin`
- [ ] Can log in with superuser
- [ ] Site created in Settings > Sites
- [ ] Home page created
- [ ] Header Content configured
- [ ] Footer Content configured
- [ ] Main Menu configured

## Content Setup

- [ ] Home page has content blocks
- [ ] Images uploaded to Wagtail Images
- [ ] Videos uploaded or linked
- [ ] Menu items created and linked
- [ ] All pages created (About, Identity, Learning, etc.)

## Testing

- [ ] Homepage loads correctly
- [ ] Header displays correctly
- [ ] Footer displays correctly
- [ ] Menu works correctly
- [ ] All links work
- [ ] Images display correctly
- [ ] CSS styles applied correctly
- [ ] JavaScript animations work
- [ ] Responsive design works on mobile

## Production Checklist (Before Deployment)

- [ ] `DEBUG=False` in production settings
- [ ] `SECRET_KEY` is secure and random
- [ ] `ALLOWED_HOSTS` configured
- [ ] Database credentials secure
- [ ] Static files served correctly (WhiteNoise/S3/CDN)
- [ ] Media files served correctly
- [ ] SSL certificate configured
- [ ] Backup strategy in place
- [ ] Error logging configured
- [ ] Performance monitoring set up

## Common Issues & Solutions

### Issue: Database connection error
**Solution**: 
- Check PostgreSQL is running
- Verify credentials in `.env`
- Ensure database exists

### Issue: Static files not loading
**Solution**:
- Run `python manage.py collectstatic`
- Check `STATIC_URL` and `STATIC_ROOT` in settings
- Verify files are in correct directories

### Issue: Template errors
**Solution**:
- Check template paths in `TEMPLATES` setting
- Verify context processors are included
- Check template tags are loaded

### Issue: Images not displaying
**Solution**:
- Check `MEDIA_URL` and `MEDIA_ROOT` settings
- Verify media files are uploaded
- Check file permissions

### Issue: Menu not appearing
**Solution**:
- Ensure Main Menu is created in admin
- Check template tag is loaded: `{% load menus_tags %}`
- Verify menu items have valid links

## Verification Commands

```bash
# Check Django version
python manage.py version

# Check for migration issues
python manage.py showmigrations

# Check static files
python manage.py collectstatic --dry-run

# Run checks
python manage.py check

# Test server
python manage.py runserver
```

## Getting Help

1. Check `setup_instructions.md` for detailed setup
2. Check `WAGTAIL_SETUP.md` for Wagtail-specific help
3. Check `QUICK_START.md` for quick commands
4. Review error messages in console/logs
5. Check Wagtail documentation: https://docs.wagtail.org/
