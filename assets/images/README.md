# Image Assets for Portfolio

This folder contains all image assets for the portfolio website.

## Required Images

### Profile Photo
- **Filename:** `profile.jpg`
- **Location:** `assets/images/profile.jpg`
- **Dimensions:** 800x800px (square)
- **Format:** JPG or PNG
- **Purpose:** Hero section profile image
- **Notes:** Professional headshot, good lighting, neutral background

### Project Images

All project images should be placed in `assets/images/` with the following specifications:

1. **matlab-app.jpg**
   - Dimensions: 1200x800px (3:2 aspect ratio)
   - Shows MATLAB app interface or related imagery
   
2. **pendulum.jpg**
   - Dimensions: 1200x800px (3:2 aspect ratio)
   - Shows inverted pendulum system or mechanical design
   
3. **launch-controller.jpg**
   - Dimensions: 1200x800px (3:2 aspect ratio)
   - Shows launch controller hardware or system
   
4. **rocketry-lab.jpg**
   - Dimensions: 1200x800px (3:2 aspect ratio)
   - Shows lab facility, rockets, or team working

## Image Optimization Tips

1. **Compress images** before uploading:
   - Use tools like TinyPNG, ImageOptim, or Squoosh
   - Target file size: <200KB per image
   
2. **Use appropriate formats**:
   - Photos: JPG (85-90% quality)
   - Graphics/illustrations: PNG
   - Modern browsers: WebP (provide JPG fallback)

3. **Responsive images** are already configured in the CSS:
   - Images will scale to fit their containers
   - Aspect ratios are maintained
   - Lazy loading is enabled for performance

## Placeholder Images

If you don't have images ready, you can use placeholder services temporarily:

```html
<!-- Example placeholder services -->
https://via.placeholder.com/800x800/0066cc/ffffff?text=Profile
https://via.placeholder.com/1200x800/0066cc/ffffff?text=Project
```

Or use Unsplash for high-quality stock photos:
```
https://source.unsplash.com/800x800/?portrait,engineer
https://source.unsplash.com/1200x800/?engineering,aerospace
```

## Adding Your Images

1. Save your profile photo as `profile.jpg` in this directory
2. Save project images with the filenames listed above
3. Ensure images are optimized for web
4. The website will automatically load them

## Alternative: Using Existing Images

If you have images in the old `Main/assets/img/` folder, you can either:
- Copy them to this location
- Update the image paths in `index.html` to point to the old location

## Image Credits

If using stock photos or imagery that requires attribution, list credits here:
- [Image name]: Credit to [Photographer/Source]
