# St Patrick's College Website

A modern, responsive website for St Patrick's College built with Bootstrap 5, LESS, and vanilla JavaScript.

## 🚀 Features

- Fully responsive design (mobile-first approach)
- Bootstrap 5 grid system
- LESS preprocessor for styling
- GSAP animations
- Modern, accessible UI/UX
- Optimized for performance

## 📁 Project Structure

```
st-patrick/
├── assets/
│   ├── fonts/          # Helvetica Neue LT Pro font files
│   ├── icons/          # SVG icons and logos
│   └── images/         # Image assets
├── src/
│   ├── scripts/        # JavaScript files
│   └── styles/         # LESS source files
├── index.html          # Main HTML file
└── package.json        # Dependencies and scripts
```

## 🛠️ Setup & Development

### Prerequisites

- Node.js (v14 or higher)
- npm

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/st-patrick.git
cd st-patrick
```

2. Install dependencies:
```bash
npm install
```

3. Compile LESS to CSS:
```bash
npm run less:compile
```

4. For development with auto-compilation:
```bash
npm run less:watch
```

## 📝 Available Scripts

- `npm run less:compile` - Compile LESS to CSS
- `npm run less:watch` - Watch and auto-compile LESS files
- `npm run less:minify` - Compile and minify CSS

## 🌐 GitHub Pages Deployment

### Option 1: Automatic Deployment (Recommended)

1. Push your code to GitHub
2. Go to repository Settings → Pages
3. Select source branch (usually `main` or `master`)
4. Select `/ (root)` as the folder
5. Click Save

Your site will be available at: `https://yourusername.github.io/st-patrick/`

### Option 2: Using GitHub Actions

The repository includes a GitHub Actions workflow that automatically deploys to GitHub Pages when you push to the main branch.

## 📦 Build Notes

- Base font size: 16px (1rem = 16px)
- All measurements use rem, vh, or vw units
- Bootstrap 5 classes used extensively
- No inline styles or scripts
- Background images added through HTML only
- Mobile-first responsive design

## 🎨 Design System

- **Primary Colors**: Blue (#10069f), Yellow (#ffdd00), Gold variations
- **Typography**: Helvetica Neue LT Pro
- **Breakpoints**: 
  - Mobile: < 576px
  - Tablet: 768px
  - Desktop: 992px
  - Large: 1200px

## 📄 License

ISC

## 👥 Contributing

This is a private project. For contributions, please contact the repository owner.
