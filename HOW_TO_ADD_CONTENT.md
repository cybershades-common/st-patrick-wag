# How to Add Content in Wagtail

## First: Get Wagtail Running

### Step 1: Check if Wagtail is Running

Open your browser and try to access:
- **Admin Panel**: http://localhost:8000/admin
- **Website**: http://localhost:8000

If you see an error or "This site can't be reached", Wagtail is **NOT running**.

### Step 2: Start Wagtail (If Not Running)

Open your terminal/command prompt in the project directory and run:

```bash
# 1. Activate virtual environment (if not already activated)
# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# 2. Make sure you're in the project root directory
# (where manage.py is located)

# 3. Start the server
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Step 3: Initial Setup (First Time Only)

If this is your first time, you need to:

1. **Create Database Tables**:
   ```bash
   python manage.py migrate
   ```

2. **Create Admin User**:
   ```bash
   python manage.py createsuperuser
   ```
   (Enter username, email, and password when prompted)

3. **Collect Static Files**:
   ```bash
   python manage.py collectstatic --noinput
   ```

4. **Create Site** (in admin):
   - Go to http://localhost:8000/admin
   - Settings > Sites > Add a site
   - Set hostname: `localhost`, port: `8000`
   - Mark as default site

## Adding Content - Step by Step

### 1. Log In to Wagtail Admin

1. Go to: **http://localhost:8000/admin**
2. Enter your superuser credentials
3. You'll see the Wagtail admin dashboard

### 2. Set Up Header Content

1. In the admin, click **Settings** in the left menu
2. Click **Header Content**
3. Click **Add Header Content** (or edit existing)
4. Fill in:
   - **Logo**: Upload your college crest logo
   - **Logo Text Main**: "ST PATRICK'S"
   - **Logo Text Sub**: "COLLEGE"
   - **Book Tour Text**: "Book a Tour"
   - **Book Tour Link**: URL for booking
   - **Enquire Text**: "Enquire Today"
   - **Enquire Link**: URL for enquiries
5. Add **Work with Us Items**:
   - Click "Add Work with Us Item"
   - Enter label and link
   - Repeat for each item
6. Add **Quick Links Items**:
   - Click "Add Quick Link Item"
   - Enter label and link
   - Repeat for each item
7. Click **Save**

### 3. Set Up Footer Content

1. Go to **Settings > Footer Content**
2. Click **Add Footer Content** (or edit existing)
3. Fill in all sections:
   - **College Information**: Name and mission statement
   - **Address**: All address lines
   - **Contact**: Phone and contact link
   - **Footer Logos**: Upload Centenary, Old Boys, EREA logos
   - **Explore Links**: Add links (Home, About, etc.)
   - **Quick Links**: Add quick links
   - **Social Media Links**: Add Facebook, Instagram, LinkedIn
   - **Footer Bottom Links**: Add Policies, Complaints, etc.
   - **Footer Text**: Copyright, ABN, marquee text
4. Click **Save**

### 4. Set Up Main Menu

1. Go to **Settings > Main Menu**
2. Click **Add Main Menu**
3. Add menu items:
   - Click **Add Menu Item**
   - Enter **Label**: "Home"
   - Select **Page** or enter **Link**
   - Upload **Menu Image** (optional)
   - Add **Sub Menu Items** if needed
   - Click **Save**
4. Repeat for each menu item (About, Identity, Learning, etc.)

### 5. Create Home Page

1. Go to **Pages** in the left menu
2. Click **Add child page** (under Root)
3. Select **Home Page**
4. Fill in:
   - **Title**: "Home"
   - **Slug**: (auto-generated, or customize)
5. In the **Body** section, add blocks:

#### Adding Hero Block:
1. Click **+** in the Body section
2. Select **Hero**
3. Fill in:
   - **Title Line 1**: "Let your"
   - **Title Line 2**: "light shine."
   - **Description**: Your hero description
   - **Button Text**: "Welcome to St Patrick's"
   - **Button Link/Page**: Link or select page
   - **Video File** or **Background Image**: Upload
   - **Poster Image**: For video
4. Click **Save**

#### Adding About Block:
1. Click **+** to add another block
2. Select **About**
3. Fill in:
   - **Heading**: Use rich text editor (can use underline spans)
   - **Content**: Your about content
   - **Image**: Upload about image
   - **Button 1 & 2**: Text and links
4. Click **Save**

#### Adding Other Blocks:
- **Strategic Block**: Heading, paragraphs, button, background image
- **Academics Block**: Heading, description, buttons
- **Academics Card Block**: Title and image (add multiple)
- **Co-Curricular Block**: Label, slides (each with title, description, button, image)
- **Statistics Block**: Heading, description, button, statistic cards
- **Parents Community Block**: Heading, description, button, background image
- **Testimonials Block**: Multiple testimonials (quote, author, image)
- **Latest News Block**: Heading, description, buttons, news items
- **CTA Block**: Heading, description, buttons, background image

6. Once all blocks are added, click **Publish** (top right)

### 6. Create Additional Pages

1. Go to **Pages**
2. Click **Add child page** under Root (or under a parent page)
3. Select **Standard Page**
4. Fill in:
   - **Title**: Page name
   - **Intro**: Optional intro text
   - **Body**: Add blocks (same as Home Page)
5. Click **Publish**

### 7. Upload Images

1. Go to **Images** in the left menu
2. Click **Add an image**
3. Upload your images from `assets/images/`
4. Add **Title** and **Alt text** for each
5. Click **Save**

### 8. Upload Documents/Videos

1. Go to **Documents** in the left menu
2. Click **Add a document**
3. Upload PDFs, videos, etc.
4. Add title and description
5. Click **Save**

## Quick Reference: Block Types

| Block | Use For | Key Fields |
|-------|---------|------------|
| **Hero** | Main hero section | Title, description, video/image, button |
| **About** | About section | Heading, content, image, 2 buttons |
| **Strategic** | Strategic section | Heading, 2 paragraphs, button, background |
| **Academics** | Academics intro | Heading, description, 2 buttons |
| **Academics Card** | Academic cards | Title, image (use multiple) |
| **Co-Curricular** | Activities slider | Label, slides (title, desc, button, image) |
| **Statistics** | Stats section | Heading, description, cards (desc, value) |
| **Parents Community** | Community section | Heading, description, button, background |
| **Testimonials** | Testimonials slider | Multiple (quote, author, image) |
| **Latest News** | News section | Heading, description, buttons, news items |
| **CTA** | Call to action | Heading, description, 2 buttons, background |

## Tips for Adding Content

1. **Use Page Links When Possible**: Instead of external URLs, link to Wagtail pages for better management
2. **Optimize Images**: Compress images before uploading for better performance
3. **Use Rich Text**: The About block heading supports rich text - you can use underline spans
4. **Preview Before Publishing**: Use the preview button to see how content looks
5. **Save Drafts**: Click "Save draft" to save without publishing
6. **Reuse Images**: Once uploaded, images can be reused across pages

## Common Workflow

1. **Upload Assets First**: Upload all images, videos, documents
2. **Set Up Site Structure**: Configure header, footer, menu
3. **Create Pages**: Create all pages (Home, About, etc.)
4. **Add Content**: Add blocks to each page
5. **Link Everything**: Link menu items to pages
6. **Publish**: Publish pages when ready

## Troubleshooting

### Can't Access Admin
- Make sure server is running: `python manage.py runserver`
- Check URL: http://localhost:8000/admin
- Verify superuser exists: `python manage.py createsuperuser`

### Images Not Showing
- Check image is uploaded in Images section
- Verify image is selected in block
- Check MEDIA_URL in settings

### Menu Not Appearing
- Ensure Main Menu is created in Settings
- Check menu items have valid links
- Verify template includes menu

### Blocks Not Saving
- Check for validation errors (red text)
- Ensure required fields are filled
- Try saving draft first

## Next Steps After Adding Content

1. **Test on Frontend**: Visit http://localhost:8000 to see your content
2. **Check Responsive**: Test on mobile/tablet
3. **Test Links**: Verify all links work
4. **Check Animations**: Ensure GSAP animations work
5. **Optimize**: Compress images, optimize performance

---

**Need Help?** Check the other documentation files:
- `setup_instructions.md` - Detailed setup
- `WAGTAIL_SETUP.md` - Wagtail-specific setup
- `QUICK_START.md` - Quick commands
