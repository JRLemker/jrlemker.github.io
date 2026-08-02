# Project Images Organization

This document explains how to organize images for the portfolio website with individual project pages.

## Folder Structure

```
assets/images/
├── profile.jpg                           # Your profile photo (800x800px)
├── matlab-app.jpg                        # Project card thumbnail
├── pendulum.jpg                          # Project card thumbnail
├── launch-controller.jpg                 # Project card thumbnail
├── rocketry-lab.jpg                      # Project card thumbnail
└── projects/                             # Detailed project images
    ├── matlab-app/
    │   ├── hero.jpg                     # Hero image (1200x600px)
    │   ├── interface-1.jpg              # Screenshot
    │   ├── interface-2.jpg              # Screenshot
    │   ├── workflow.jpg                 # Diagram/workflow
    │   ├── screenshot-1.jpg             # Additional screenshots
    │   ├── screenshot-2.jpg
    │   ├── screenshot-3.jpg
    │   └── screenshot-4.jpg
    ├── pendulum/
    │   ├── hero.jpg
    │   ├── design-1.jpg
    │   ├── design-2.jpg
    │   ├── assembly-1.jpg
    │   ├── assembly-2.jpg
    │   └── final.jpg
    ├── launch-controller/
    │   ├── hero.jpg
    │   ├── hardware-1.jpg
    │   ├── hardware-2.jpg
    │   ├── wiring.jpg
    │   └── operation.jpg
    └── rocketry-lab/
        ├── hero.jpg
        ├── facility-1.jpg
        ├── facility-2.jpg
        ├── team.jpg
        └── rockets.jpg
```

## Image Specifications

### Profile Photo
- **File:** `profile.jpg`
- **Size:** 800x800px (1:1 square)
- **Format:** JPG, optimized
- **Size:** <200KB
- **Content:** Professional headshot, good lighting

### Project Card Thumbnails
These appear on the home page and portfolio grid:
- **Size:** 1200x800px (3:2 ratio)
- **Format:** JPG, 85-90% quality
- **Size:** <200KB each
- **Content:** Representative image of the project

### Hero Images (Project Pages)
The large banner at the top of each project page:
- **Size:** 1200x600px (2:1 ratio)
- **Format:** JPG, optimized
- **Size:** <250KB
- **Content:** Most impressive/representative shot

### Gallery Images
Detailed photos throughout the project page:
- **Size:** 800x600px or 1200x900px (4:3 ratio)
- **Format:** JPG, 85% quality
- **Size:** <150KB each
- **Content:** Interface screenshots, hardware photos, diagrams

## Image Naming Conventions

Use descriptive, lowercase names with hyphens:
- ✅ `hero.jpg`
- ✅ `interface-main.jpg`
- ✅ `assembly-step-1.jpg`
- ❌ `IMG_1234.jpg`
- ❌ `Screenshot 2024.png`

## Optimization Tips

### Before Upload
1. **Resize** to exact dimensions needed
2. **Compress** using tools like:
   - TinyPNG (https://tinypng.com/)
   - ImageOptim (Mac)
   - Squoosh (https://squoosh.app/)
3. **Convert** PNG to JPG for photos
4. **Keep** PNG only for diagrams/text

### Image Quality Guidelines
- **Photos:** JPG at 85-90% quality
- **Screenshots:** JPG at 90% quality  
- **Diagrams:** PNG for sharp text
- **Target:** <200KB per image

## Using Placeholder Images Temporarily

If you don't have all images ready, use these placeholder services:

### Unsplash (High Quality Stock Photos)
```
https://source.unsplash.com/1200x800/?engineering
https://source.unsplash.com/1200x800/?rocket,aerospace
https://source.unsplash.com/1200x800/?electronics,circuit
https://source.unsplash.com/800x800/?portrait,professional
```

### Placeholder.com (Simple Colored Placeholders)
```
https://via.placeholder.com/1200x800/0066cc/ffffff?text=Project+Image
https://via.placeholder.com/800x800/0066cc/ffffff?text=Profile
```

## Taking Good Project Photos

### Hardware/Physical Projects
- Use good lighting (natural light or soft box)
- Clean background (white/gray backdrop)
- Show scale (include ruler or common object)
- Multiple angles (front, side, detail shots)

### Software/Interface Screenshots
- Full window capture in highest resolution
- Clean up desktop/tabs before screenshot
- Highlight important areas with annotations
- Use consistent theme/appearance

### Diagrams and Workflows
- Export at 2x resolution for retina displays
- Use high contrast colors
- Keep text large and readable
- Save as PNG for crisp lines

## Photo Credits

If using stock photos or others' imagery, add attribution:

```
Photo by [Photographer Name] on Unsplash
Image courtesy of [Source]
```

## Quick Setup Checklist

- [ ] Add profile.jpg (800x800px)
- [ ] Add 4 project card thumbnails (1200x800px)
- [ ] Create `projects/` subfolder
- [ ] Create project-specific folders
- [ ] Add hero.jpg to each project folder (1200x600px)
- [ ] Add 4-6 gallery images per project
- [ ] Optimize all images <200KB
- [ ] Test loading in browser
- [ ] Verify lightbox functionality

## Image Loading in Code

The website automatically handles:
- ✅ Lazy loading (images load as you scroll)
- ✅ Responsive sizing (images scale to fit)
- ✅ Lightbox viewer (click to enlarge)
- ✅ Error handling (graceful fallback if image missing)
- ✅ Alt text (from image attributes)

No additional code needed - just place images in the correct folders!
