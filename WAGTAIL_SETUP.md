# Wagtail CMS Setup Guide

## Initial Wagtail Setup Steps

After running migrations and creating a superuser, follow these steps to set up your Wagtail site:

### 1. Create Site in Wagtail Admin

1. Log in to `/admin`
2. Go to **Settings > Sites**
3. Click **Add a site**
4. Set:
   - **Site name**: St Patrick's College
   - **Hostname**: localhost (or your domain)
   - **Port**: 8000 (or 80 for production)
   - **Is default site**: Yes
   - **Root page**: Select your Home page (create it first if needed)

### 2. Create Home Page

1. Go to **Pages** in the admin
2. Click **Add child page** under "Root"
3. Select **Home Page**
4. Fill in:
   - **Title**: Home
   - **Slug**: (auto-generated)
   - Add content blocks in the **Body** field
5. Click **Publish**

### 3. Set Up Header Content

1. Go to **Settings > Header Content**
2. Click **Add Header Content**
3. Configure:
   - Upload logo image
   - Set logo text (main and sub)
   - Set button texts and links
   - Add "Work with Us" items
   - Add "Quick Links" items
4. Click **Save**

### 4. Set Up Footer Content

1. Go to **Settings > Footer Content**
2. Click **Add Footer Content**
3. Configure all footer sections:
   - College information
   - Address and contact
   - Upload footer logos
   - Add explore links
   - Add quick links
   - Add social media links
   - Add footer bottom links
   - Set copyright and ABN
4. Click **Save**

### 5. Set Up Main Menu

1. Go to **Settings > Main Menu**
2. Click **Add Main Menu**
3. Add menu items:
   - Click **Add Menu Item**
   - Set label and link/page
   - Add sub-menu items if needed
   - Upload menu image
4. Click **Save**

### 6. Create Additional Pages

Create pages for:
- About
- Identity
- Learning
- Co-Curricular
- Community
- Enrolment

Use **Standard Page** type for internal pages.

### 7. Upload Media Assets

1. Go to **Images** in the admin
2. Upload all your images from `assets/images/`
3. Go to **Documents** to upload PDFs and other files
4. Go to **Documents** to upload videos (or use external URLs)

### 8. Configure Static Files

Ensure your static files are properly collected:

```bash
python manage.py collectstatic --noinput
```

Make sure your `assets/` and `src/` folders are accessible. You may need to copy them to `static/` or configure `STATICFILES_DIRS` in settings.

## Content Block Usage

### Hero Block
- Use for main hero sections
- Supports video or image background
- Includes title, description, and CTA button

### About Block
- Rich text content
- Image support
- Two buttons (can link to pages or external URLs)

### Strategic Block
- Background image support
- Heading and two paragraphs
- CTA button

### Academics Block
- Heading and description
- Two buttons
- Use with Academics Card Blocks for cards

### Co-Curricular Block
- Slider with multiple slides
- Each slide has title, description, button, and background image
- Navigation buttons for each slide

### Statistics Block
- Heading and description
- Multiple statistic cards
- Each card has description and value

### Testimonials Block
- Multiple testimonials
- Each has quote, author, and image
- Automatic slider functionality

### Latest News Block
- Heading and description
- Two buttons
- List of news items (each with title, date, image, link)

### CTA Block
- Call to action section
- Background image support
- Heading, description, and two buttons

## Tips

1. **Images**: Always optimize images before uploading
2. **Videos**: Use external hosting (YouTube, Vimeo) or upload to media folder
3. **Links**: Prefer linking to Wagtail pages over external URLs when possible
4. **SEO**: Fill in SEO fields for each page
5. **Preview**: Use the preview feature to see changes before publishing

## Troubleshooting

### Images not showing
- Check `MEDIA_URL` and `MEDIA_ROOT` settings
- Ensure media files are uploaded correctly
- Check file permissions

### Static files not loading
- Run `collectstatic` command
- Check `STATIC_URL` and `STATIC_ROOT` settings
- Verify static files are in correct directories

### Menu not appearing
- Ensure Main Menu is created and saved
- Check template tag is loaded: `{% load menus_tags %}`
- Verify menu items have valid links

### Content not saving
- Check database connection
- Verify user has proper permissions
- Check for validation errors in admin
