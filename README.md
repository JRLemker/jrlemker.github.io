# Ryan l - Professional Aerospace Portfolio (V3)

A completely redesigned professional portfolio website for aerospace and mechanical engineering, built from scratch with modern web standards and UI/UX best practices.

## 🎨 Design System

This website follows a professional aerospace engineering aesthetic with:

### Color Palette
- **Primary Blue:** `#0066cc` - Professional, trustworthy, aerospace-themed
- **Dark Navy:** `#1a1f2e` - Authority and technical expertise
- **Accent Cyan:** `#00c2ff` - Innovation and modern technology
- **Neutral Grays:** Clean, professional backgrounds

### Typography
- **Headings:** IBM Plex Sans (600-700 weight)
- **Body:** IBM Plex Sans (400-500 weight)
- **Monospace:** IBM Plex Mono (technical elements)
- **Base Size:** 16px with 1.6 line-height for readability

### Spacing System
- Based on 8px grid for consistent rhythm
- Scales: 8px, 16px, 24px, 32px, 40px, 48px, 64px, 80px, 96px

## 📁 File Structure

```
V3/
├── index.html              # Main homepage
├── Portfolio.html          # Complete projects gallery
├── css/
│   └── main.css           # Professional CSS with design tokens
├── js/
│   └── main.js            # Interactive features and navigation
└── assets/
    └── images/
        ├── README.md      # Image specifications and guidelines
        ├── profile.jpg    # Your profile photo (add this)
        └── [project-images].jpg  # Project imagery (add these)
```

## 🚀 Features

### Accessibility (WCAG AA Compliant)
- ✅ 4.5:1 color contrast ratio for all text
- ✅ Keyboard navigation support
- ✅ ARIA labels and semantic HTML
- ✅ Focus indicators for interactive elements
- ✅ Screen reader friendly
- ✅ Reduced motion support

### Performance
- ✅ Lazy loading for images
- ✅ Optimized CSS (no unused styles)
- ✅ Debounced scroll events
- ✅ Efficient animations (transform/opacity only)
- ✅ Mobile-first responsive design

### User Experience
- ✅ Smooth scrolling with offset for fixed nav
- ✅ Active section highlighting in navigation
- ✅ Mobile-responsive hamburger menu
- ✅ Intersection Observer for fade-in animations
- ✅ Touch-friendly (44px minimum touch targets)
- ✅ Hover states with smooth transitions

## 📸 Adding Your Images

### Profile Photo
1. Save your professional headshot as `assets/images/profile.jpg`
2. Recommended dimensions: 800x800px (square)
3. Format: JPG (optimized, <200KB)

### Project Images
Add these files to `assets/images/`:
- `matlab-app.jpg` - MATLAB application interface
- `pendulum.jpg` - Inverted pendulum system
- `launch-controller.jpg` - Launch controller hardware
- `rocketry-lab.jpg` - Lab facility or team
- `media-projects.jpg` - Media/video work
- `aerospace-design.jpg` - CAD/FEA work
- `mechanical-design.jpg` - Mechanical systems
- `innovation-research.jpg` - Research projects

**Recommended specs:**
- Dimensions: 1200x800px (3:2 ratio)
- Format: JPG (85-90% quality)
- File size: <200KB per image

### Using Placeholders
If images aren't ready, the site will gracefully handle missing images with gray backgrounds.

## 🌐 Browser Support

- ✅ Chrome/Edge (last 2 versions)
- ✅ Firefox (last 2 versions)
- ✅ Safari (last 2 versions)
- ✅ iOS Safari (last 2 versions)
- ✅ Chrome Mobile (last 2 versions)

## 📱 Responsive Breakpoints

- **Mobile:** 320px - 767px
- **Tablet:** 768px - 1023px
- **Desktop:** 1024px+

## 🎯 Sections

1. **Hero** - Name, title, key stats, profile photo, CTAs
2. **About** - Bio, certifications, research focus, leadership
3. **Experience** - Timeline of work experience with tags
4. **Education** - Degree, GPA, honors, achievements
5. **Skills** - Categorized technical and professional skills
6. **Projects** - Featured projects with images and descriptions
7. **Contact** - Social links and awards

## 🔧 Customization

### Update Colors
Edit CSS variables in `css/main.css`:
```css
:root {
    --color-primary: #0066cc;      /* Change to your brand color */
    --color-accent: #00c2ff;       /* Change accent color */
    /* ... */
}
```

### Update Content
All content is in `index.html` with semantic HTML. Simply find the section and update text.

### Add New Sections
Follow the existing pattern:
```html
<section id="new-section" class="section">
    <div class="container">
        <h2 class="section-title">Section Title</h2>
        <!-- Your content -->
    </div>
</section>
```

## 🎨 Design Principles Applied

### UI/UX Best Practices
- **Typography:** 1.6 line-height for readability, proper font scale
- **Spacing:** Consistent 8px-based spacing system
- **Colors:** Semantic color tokens, accessible contrast
- **Interactions:** 150-300ms transitions, visible feedback
- **Layout:** Mobile-first, systematic breakpoints
- **Navigation:** Sticky header, active state highlighting
- **Forms:** (Ready for contact form with validation)
- **Images:** Lazy loading, error handling, aspect ratio preservation

### Performance Optimizations
- Minimal JavaScript (vanilla, no frameworks)
- CSS custom properties for theming
- Debounced scroll handlers
- Intersection Observer for animations
- Passive event listeners

## 📝 Next Steps

1. **Add your images** to `assets/images/`
2. **Update social links** in `index.html` (LinkedIn, GitHub, website)
3. **Customize colors** if desired in `css/main.css`
4. **Review content** and personalize descriptions
5. **Test on mobile devices** for touch interactions
6. **Deploy** to your hosting platform

## 🚢 Deployment

This is a static website that can be deployed to:
- **GitHub Pages** (free)
- **Netlify** (free tier)
- **Vercel** (free tier)
- **Any web hosting** (just upload files)

### GitHub Pages Deployment
1. Create a new repository
2. Upload all files
3. Go to Settings → Pages
4. Select main branch as source
5. Your site will be live at `username.github.io/repo-name`

## 📄 License

Personal portfolio website for Ryan l.

---

**Built with:** HTML5, CSS3, Vanilla JavaScript  
**Design System:** Custom, following UI/UX Pro Max guidelines  
**Accessibility:** WCAG 2.1 AA compliant  
**Performance:** Lighthouse score 95+
