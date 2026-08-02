// ============================================================
// Lightbox Image Viewer
// ============================================================

document.addEventListener('DOMContentLoaded', function() {
    // Create lightbox element if it doesn't exist
    if (!document.querySelector('.lightbox')) {
        const lightbox = document.createElement('div');
        lightbox.className = 'lightbox';
        lightbox.setAttribute('role', 'dialog');
        lightbox.setAttribute('aria-label', 'Image viewer');
        lightbox.innerHTML = `
            <div class="lightbox-content">
                <button class="lightbox-close" aria-label="Close image viewer">
                    <i class="fas fa-times" aria-hidden="true"></i>
                </button>
                <img src="" alt="" class="lightbox-image">
                <p class="lightbox-caption"></p>
            </div>
        `;
        document.body.appendChild(lightbox);
    }
    
    const lightbox = document.querySelector('.lightbox');
    const lightboxImg = lightbox.querySelector('.lightbox-image');
    const lightboxCaption = lightbox.querySelector('.lightbox-caption');
    const closeBtn = lightbox.querySelector('.lightbox-close');
    
    // Add click handlers to all gallery images
    const galleryItems = document.querySelectorAll('.gallery-item');
    
    galleryItems.forEach(item => {
        item.addEventListener('click', function() {
            const img = this.querySelector('img');
            const caption = this.querySelector('.gallery-caption');
            
            if (img) {
                lightboxImg.src = img.src;
                lightboxImg.alt = img.alt;
                lightboxCaption.textContent = caption ? caption.textContent : img.alt;
                lightbox.classList.add('active');
                document.body.style.overflow = 'hidden';
                
                // Set focus to close button for accessibility
                closeBtn.focus();
            }
        });
        
        // Make gallery items keyboard accessible
        item.setAttribute('tabindex', '0');
        item.setAttribute('role', 'button');
        item.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });
    });
    
    // Close lightbox function
    function closeLightbox() {
        lightbox.classList.remove('active');
        document.body.style.overflow = '';
    }
    
    // Close button click
    closeBtn.addEventListener('click', closeLightbox);
    
    // Close on background click
    lightbox.addEventListener('click', function(e) {
        if (e.target === lightbox) {
            closeLightbox();
        }
    });
    
    // Close on Escape key
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && lightbox.classList.contains('active')) {
            closeLightbox();
        }
    });
    
    // Prevent image from closing lightbox when clicked
    lightboxImg.addEventListener('click', function(e) {
        e.stopPropagation();
    });
    
    // Add navigation arrows for multiple images (optional enhancement)
    let currentImageIndex = 0;
    const allImages = Array.from(galleryItems);
    
    function showImage(index) {
        if (index >= 0 && index < allImages.length) {
            currentImageIndex = index;
            const item = allImages[index];
            const img = item.querySelector('img');
            const caption = item.querySelector('.gallery-caption');
            
            lightboxImg.src = img.src;
            lightboxImg.alt = img.alt;
            lightboxCaption.textContent = caption ? caption.textContent : img.alt;
        }
    }
    
    // Arrow key navigation
    document.addEventListener('keydown', function(e) {
        if (!lightbox.classList.contains('active')) return;
        
        if (e.key === 'ArrowRight') {
            showImage(currentImageIndex + 1);
        } else if (e.key === 'ArrowLeft') {
            showImage(currentImageIndex - 1);
        }
    });
    
    // Update current index when opening lightbox
    galleryItems.forEach((item, index) => {
        item.addEventListener('click', function() {
            currentImageIndex = index;
        });
    });
});

// ============================================================
// Smooth Scroll to Sections
// ============================================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href === '#') return;
        
        const target = document.querySelector(href);
        if (target) {
            e.preventDefault();
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ============================================================
// Read Progress Indicator (Optional)
// ============================================================

function updateReadProgress() {
    const projectContent = document.querySelector('.project-content');
    if (!projectContent) return;
    
    const scrollTop = window.pageYOffset;
    const contentStart = projectContent.offsetTop;
    const contentHeight = projectContent.offsetHeight;
    const windowHeight = window.innerHeight;
    
    const scrollDistance = scrollTop - contentStart + windowHeight;
    const totalDistance = contentHeight + windowHeight;
    
    const progress = Math.min(Math.max((scrollDistance / totalDistance) * 100, 0), 100);
    
    // You can add a progress bar element and update it here
    // document.querySelector('.progress-bar').style.width = progress + '%';
}

window.addEventListener('scroll', updateReadProgress, { passive: true });
