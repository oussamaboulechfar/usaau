// DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    // Smooth Scroll for Explore Cities buttons using GSAP
    const scrollButtons = document.querySelectorAll('.scroll-to');
    scrollButtons.forEach(button => {
        button.addEventListener('click', (e) => {
            e.preventDefault();
            const targetId = button.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                if (typeof gsap !== 'undefined' && typeof ScrollToPlugin !== 'undefined') {
                    gsap.to(window, {
                        scrollTo: { y: targetSection, autoKill: false },
                        duration: 1.5,
                        ease: 'power2.out'
                    });
                } else {
                    targetSection.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // Slick Slider for Hero Section
    if ($('.hero-slider').length) {
        $('.hero-slider').on('init', function () {
            console.log('Slider initialized successfully');
        }).on('beforeChange', function (event, slick, currentSlide, nextSlide) {
            console.log('Changing from slide', currentSlide, 'to', nextSlide);
        }).slick({
            autoplay: true,
            autoplaySpeed: 4000,
            arrows: true,
            dots: true,
            fade: false,
            cssEase: 'linear',
            pauseOnHover: false,
            pauseOnFocus: false,
            infinite: true,
            speed: 500,
            slidesToShow: 1,
            slidesToScroll: 1
        });
    }

    // GSAP Animations for City Detail Page
    if (document.querySelector('.city-detail-section') && typeof gsap !== 'undefined') {
        const heroContent = document.querySelector('.hero-content');
        if (heroContent) {
            gsap.from(heroContent, {
                opacity: 0,
                y: 50,
                duration: 1,
                ease: 'power3.out'
            });
        }
        const cityDetailContent = document.querySelector('.city-detail-content');
        if (cityDetailContent) {
            gsap.from(cityDetailContent, {
                opacity: 0,
                y: 100,
                duration: 1.2,
                ease: 'power3.out',
                delay: 0.3
            });
        }
    }

    // GSAP Animations for Home Page
    if (document.querySelector('.cities-grid') && typeof gsap !== 'undefined') {
        const fadeUpElements = document.querySelectorAll('[data-gsap="fade-up"]');
        if (fadeUpElements.length) {
            gsap.from(fadeUpElements, {
                opacity: 0,
                y: 50,
                duration: 1,
                ease: 'power3.out'
            });
        }

        const zoomInElements = document.querySelectorAll('[data-gsap="zoom-in"]');
        if (zoomInElements.length) {
            gsap.from(zoomInElements, {
                scale: 0.8,
                opacity: 0,
                duration: 0.8,
                stagger: 0.2,
                scrollTrigger: {
                    trigger: '.cities-grid',
                    start: 'top 80%'
                }
            });
        }
    }
});

// Preloader
window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        setTimeout(() => {
            preloader.style.display = 'none';
        }, 1000);
    }
});

// Sticky Header
window.addEventListener('scroll', () => {
    const header = document.querySelector('.main-header');
    if (header) {
        header.classList.toggle('scrolled', window.scrollY > 50);
    }
});

// Back to Top
const backToTopButton = document.querySelector('.back-to-top');
if (backToTopButton) {
    window.addEventListener('scroll', () => {
        if (window.scrollY > 300) {
            backToTopButton.classList.add('visible');
        } else {
            backToTopButton.classList.remove('visible');
        }
    });
    backToTopButton.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}
