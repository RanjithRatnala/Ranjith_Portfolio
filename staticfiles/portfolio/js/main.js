// Color schemes for each section
const colorSchemes = [
    { primary: 240, secondary: 260, accent: 280 }, // Blue/Purple - Hero
    { primary: 280, secondary: 300, accent: 320 }, // Purple/Magenta - About
    { primary: 320, secondary: 340, accent: 20 },  // Magenta/Pink - Experience
    { primary: 20, secondary: 40, accent: 60 },    // Red/Orange - Skills
    { primary: 60, secondary: 80, accent: 100 },   // Orange/Yellow - Projects
    { primary: 180, secondary: 200, accent: 220 }  // Teal/Blue - Resume
];

let isScrolling = false;
let currentSection = 0;
let isLightMode = false;

// Theme toggle functionality
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        isLightMode = !isLightMode;
        body.setAttribute('data-theme', isLightMode ? 'light' : 'dark');
        themeToggle.textContent = isLightMode ? '☀️' : '🌙';
        localStorage.setItem('theme', isLightMode ? 'light' : 'dark');
    });

    // Load saved theme
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        isLightMode = savedTheme === 'light';
        body.setAttribute('data-theme', savedTheme);
        themeToggle.textContent = isLightMode ? '☀️' : '🌙';
    }
}

// Create floating elements
function createFloatingElements() {
    const container = document.getElementById('floatingElements');
    if (!container) return;
    
    // Clear existing elements
    container.innerHTML = '';
    
    for (let i = 0; i < 20; i++) {
        const element = document.createElement('div');
        element.className = 'floating-element';
        element.style.left = Math.random() * 100 + '%';
        element.style.width = element.style.height = (Math.random() * 80 + 30) + 'px';
        element.style.animationDelay = Math.random() * 20 + 's';
        element.style.animationDuration = (Math.random() * 10 + 15) + 's';
        container.appendChild(element);
    }
}

// Update CSS variables for smooth color transitions
function updateColors(progress = 0) {
    const root = document.documentElement;
    
    if (currentSection >= colorSchemes.length) return;
    
    const currentHues = colorSchemes[currentSection];
    const nextHues = colorSchemes[Math.min(currentSection + 1, colorSchemes.length - 1)];
    
    const primaryHue = currentHues.primary + (nextHues.primary - currentHues.primary) * progress;
    const secondaryHue = currentHues.secondary + (nextHues.secondary - currentHues.secondary) * progress;
    const accentHue = currentHues.accent + (nextHues.accent - currentHues.accent) * progress;
    
    root.style.setProperty('--primary-hue', primaryHue);
    root.style.setProperty('--secondary-hue', secondaryHue);
    root.style.setProperty('--accent-hue', accentHue);
}

// Handle scroll events
function handleScroll() {
    if (isScrolling) return;
    
    isScrolling = true;
    requestAnimationFrame(() => {
        const scrollY = window.scrollY;
        const windowHeight = window.innerHeight;
        const documentHeight = document.documentElement.scrollHeight - windowHeight;
        
        // Update scroll indicator
        const scrollIndicator = document.getElementById('scrollIndicator');
        if (scrollIndicator && documentHeight > 0) {
            const scrollProgress = scrollY / documentHeight;
            scrollIndicator.style.width = (scrollProgress * 100) + '%';
        }
        
        // Determine current section
        const sections = document.querySelectorAll('.section');
        let newSection = 0;
        
        sections.forEach((section, index) => {
            const rect = section.getBoundingClientRect();
            if (rect.top <= windowHeight * 0.5 && rect.bottom >= windowHeight * 0.5) {
                newSection = index;
            }
        });
        
        // Update navigation active state
        document.querySelectorAll('.nav-link').forEach((link, index) => {
            link.classList.toggle('active', index === newSection);
        });
        
        // Calculate section progress for smooth color transitions
        const sectionRect = sections[newSection] ? sections[newSection].getBoundingClientRect() : null;
        if (sectionRect) {
            const sectionProgress = Math.max(0, Math.min(1, (windowHeight - sectionRect.top) / windowHeight));
            if (newSection !== currentSection) {
                currentSection = newSection;
            }
            updateColors(sectionProgress);
        }
        
        isScrolling = false;
    });
}

// Navigation link click handlers
document.querySelectorAll('.nav-link, .btn[href^="#"]').forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = link.getAttribute('href').substring(1);
        const targetSection = document.getElementById(targetId);
        if (targetSection) {
            window.scrollTo({
                top: targetSection.offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

// Animate skill bars when skills section is visible
function animateSkillBars() {
    const skillsSection = document.getElementById('skills');
    if (!skillsSection) return;
    const rect = skillsSection.getBoundingClientRect();
    
    if (rect.top < window.innerHeight && rect.bottom > 0) {
        document.querySelectorAll('.skill-progress').forEach(bar => {
            const width = bar.getAttribute('data-width');
            if (width) {
                bar.style.width = width + '%';
            }
        });
    }
}

// Smooth scrolling for better performance
let ticking = false;
window.addEventListener('scroll', () => {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            handleScroll();
            animateSkillBars();
            ticking = false;
        });
        ticking = true;
    }
});

// Download PDF Button Functionality
const downloadPdfBtn = document.getElementById('downloadPdfBtn');
if (downloadPdfBtn) {
    downloadPdfBtn.addEventListener('click', function(e) {
        e.preventDefault();
        alert('Please upload your resume file through the Django admin panel.');
    });
}

// Email Resume Button Functionality
const emailResumeBtn = document.getElementById('emailResumeBtn');
if (emailResumeBtn) {
    emailResumeBtn.addEventListener('click', function(e) {
        e.preventDefault();
        
        // Get email from Django template context or use default
        const toEmail = document.querySelector('meta[name="contact-email"]')?.content || 'your-email@example.com';
        
        const emailSubject = 'Inquiry from your Portfolio - Resume Request';
        const emailBody = 'Hello,\n\nI came across your portfolio and was very impressed. Could you please send me a copy of your resume?\n\nThank you,\n[Your Name]';
        
        window.location.href = `mailto:${toEmail}?subject=${encodeURIComponent(emailSubject)}&body=${encodeURIComponent(emailBody)}`;
    });
}

// Initialize on DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    createFloatingElements();
    handleScroll(); // Initial call to set colors and active links
    
    // Set initial skill bar widths to 0 for animation
    document.querySelectorAll('.skill-progress').forEach(bar => {
        bar.style.width = '0%';
    });
    animateSkillBars(); // Check if visible on load
    
    // GSAP Animations
    if (typeof gsap !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        // Hero Animation
        gsap.from('.hero .subtitle', { opacity: 0, y: -20, duration: 0.8, delay: 0.2 });
        gsap.from('.hero h1', { opacity: 0, y: -20, duration: 1, delay: 0.4 });
        gsap.from('.hero .description', { opacity: 0, y: -20, duration: 1, delay: 0.6 });
        gsap.from('.hero .cta-buttons .btn', { opacity: 0, y: 20, stagger: 0.2, duration: 0.8, delay: 0.8 });

        // General Section Animation
        gsap.utils.toArray('.section-title, .about-text p, .about-image, .experience-item, .skill-category, .project-card, .resume-content').forEach(elem => {
            gsap.from(elem, {
                scrollTrigger: {
                    trigger: elem,
                    start: 'top 85%',
                    toggleActions: 'play none none none'
                },
                opacity: 0,
                y: 50,
                duration: 1,
            });
        });
    }
});

// Add mouse movement parallax effect
document.addEventListener('mousemove', (e) => {
    const mouseX = e.clientX / window.innerWidth;
    const mouseY = e.clientY / window.innerHeight;
    
    document.querySelectorAll('.floating-element').forEach((element, index) => {
        const speed = (index % 5 + 1) * 0.1;
        const x = (mouseX - 0.5) * speed * 50;
        const y = (mouseY - 0.5) * speed * 50;
        
        // Use GSAP for smoother animation if available
        if (typeof gsap !== 'undefined') {
            gsap.to(element, {
                x: x,
                y: y,
                duration: 0.5,
                ease: 'power1.out'
            });
        } else {
            element.style.transform = `translate(${x}px, ${y}px)`;
        }
    });
});

// Mobile menu functionality
const mobileMenuBtn = document.getElementById('mobileMenuBtn');
const navLinks = document.querySelector('.nav-links');
let isMobileMenuOpen = false;

if (mobileMenuBtn && navLinks) {
    mobileMenuBtn.addEventListener('click', () => {
        isMobileMenuOpen = !isMobileMenuOpen;
        if (isMobileMenuOpen) {
            navLinks.style.display = 'flex';
            navLinks.style.flexDirection = 'column';
            navLinks.style.position = 'absolute';
            navLinks.style.top = '100%';
            navLinks.style.left = '0';
            navLinks.style.right = '0';
            navLinks.style.background = 'var(--navbar-bg)';
            navLinks.style.padding = '20px';
            navLinks.style.backdropFilter = 'blur(20px)';
            mobileMenuBtn.textContent = '✕';
        } else {
            navLinks.style.display = 'none';
            mobileMenuBtn.textContent = '☰';
        }
    });
}

// Close mobile menu when clicking a link or outside
document.addEventListener('click', (e) => {
    if (!isMobileMenuOpen) return;
    const isLink = e.target.closest('.nav-link');
    const isNavContainer = e.target.closest('.nav-container');
    if (isLink || !isNavContainer) {
        isMobileMenuOpen = false;
        if (navLinks) {
            navLinks.style.display = 'none';
        }
        if (mobileMenuBtn) {
            mobileMenuBtn.textContent = '☰';
        }
    }
});

// Add resize handler
window.addEventListener('resize', () => {
    handleScroll();
    if (window.innerWidth > 768) {
        if (navLinks) {
            navLinks.style.display = 'flex';
            navLinks.style.flexDirection = 'row';
            navLinks.style.position = 'static';
            navLinks.style.background = 'none';
            navLinks.style.padding = '0';
        }
        isMobileMenuOpen = false;
        if (mobileMenuBtn) mobileMenuBtn.textContent = '☰';
    } else if (!isMobileMenuOpen) {
        if (navLinks) navLinks.style.display = 'none';
    }
}); 