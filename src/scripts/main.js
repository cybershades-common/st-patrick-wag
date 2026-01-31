// Menu functionality
document.addEventListener('DOMContentLoaded', function () {
    const header = document.getElementById('header');
    const menuToggle = document.getElementById('menuToggle');
    const megaMenu = document.getElementById('megaMenu');
    const menuOverlay = document.getElementById('menuOverlay');
    const hamburger = document.getElementById('hamburger');
    const menuText = menuToggle.querySelector('.menu-text');
    const menuMainItems = document.querySelectorAll('.menu-main-item');
    const menuSubItems = document.querySelectorAll('.menu-sub-item');
    const footerArrowUp = document.getElementById('footerArrowUp');

    const btnEnquire = document.querySelector('.btn-enquire');
    const dropdownWrappers = document.querySelectorAll('.dropdown-wrapper');

    let isMenuOpen = false;
    let isHeaderHidden = false;
    let lastScrollY = window.scrollY;
    let scrollTicking = false;

    function openMenu() {
        isMenuOpen = true;
        header.classList.add('menu-open');
        header.classList.remove('header-hidden');
        isHeaderHidden = false;
        megaMenu.classList.add('active');
        menuOverlay.classList.add('active');
        hamburger.classList.add('active');
        menuText.textContent = 'CLOSE';
        document.body.style.overflow = 'hidden';

        btnEnquire.style.display = 'inline-flex';
        dropdownWrappers.forEach(wrapper => {
            wrapper.style.display = 'flex';
        });

        gsap.to(megaMenu, {
            opacity: 1,
            duration: 0.3,
            ease: 'power2.out'
        });

    }

    function closeMenu() {
        isMenuOpen = false;
        header.classList.remove('menu-open');
        hamburger.classList.remove('active');
        menuText.textContent = 'MENU';

        megaMenu.classList.remove('active');
        menuOverlay.classList.remove('active');
        document.body.style.overflow = '';

        btnEnquire.style.display = 'none';
        dropdownWrappers.forEach(wrapper => {
            wrapper.style.display = 'none';
        });

        updateHeaderOnScroll();
    }

    menuToggle.addEventListener('click', function () {
        if (isMenuOpen) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    menuOverlay.addEventListener('click', closeMenu);

    function updateHeaderOnScroll() {
        const currentScrollY = window.scrollY;
        const headerHeight = header.offsetHeight || 0;
        const delta = currentScrollY - lastScrollY;

        if (!isMenuOpen) {
            if (currentScrollY > 0) {
                header.classList.add('header-scrolled');
            } else {
                header.classList.remove('header-scrolled');
            }

            if (currentScrollY > headerHeight && delta > 0) {
                if (!isHeaderHidden) {
                    header.classList.add('header-hidden');
                    isHeaderHidden = true;
                }
            } else if (delta < -5 || currentScrollY <= headerHeight) {
                if (isHeaderHidden) {
                    header.classList.remove('header-hidden');
                    isHeaderHidden = false;
                }
            }
        }

        lastScrollY = currentScrollY;
        scrollTicking = false;
    }

    window.addEventListener('scroll', function () {
        if (!scrollTicking) {
            window.requestAnimationFrame(updateHeaderOnScroll);
            scrollTicking = true;
        }
    });
    updateHeaderOnScroll();

    gsap.registerPlugin(ScrollTrigger);

    // Hero animations
    function initHeroAnimations() {
        const heroGradient = document.querySelector('.hero-gradient');
        if (heroGradient) {
            gsap.set(heroGradient, {
                x: '-10%',
                y: '5vh',
                opacity: 0,
                visibility: 'visible'
            });

            gsap.to(heroGradient, {
                x: '-15vw',
                y: '35vh',
                opacity: 0.9,
                duration: 3.3,
                ease: 'power2.out',
                scrollTrigger: {
                    trigger: '.hero',
                    start: 'top 95%',
                    toggleActions: 'play none none reverse'
                }
            });
        }

        gsap.fromTo('.header-logo',
            { y: -50, opacity: 0 },
            { y: 0, opacity: 1, duration: 0.6, delay: 0.2, ease: 'power2.out' }
        );

        gsap.fromTo('.header-nav',
            { y: -50, opacity: 0 },
            { y: 0, opacity: 1, duration: 0.6, delay: 0.3, ease: 'power2.out' }
        );

        const heroTitleText = document.querySelector('.hero-title');
        if (heroTitleText) {
            gsap.fromTo(heroTitleText,
                { y: 100, opacity: 0 },
                { y: 0, opacity: 1, duration: 1, delay: 0.5, ease: 'power3.out' }
            );
        }

        gsap.fromTo('.hero-text p',
            { x: 50, opacity: 0 },
            { x: 0, opacity: 1, duration: 0.8, delay: 0.8, ease: 'power2.out' }
        );

        gsap.fromTo('.hero-text button',
            { x: 50, opacity: 0 },
            { x: 0, opacity: 1, duration: 0.8, delay: 1, ease: 'power2.out' }
        );
    }

    initHeroAnimations();

    
    if (footerArrowUp) {
        footerArrowUp.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // Latest News Swiper
    function initLatestNewsSwiper() {
        const swiperEl = document.querySelector('.latest-news-swiper');
        if (!swiperEl) return;

        // Wait for Swiper to be available
        if (typeof Swiper === 'undefined') {
            setTimeout(initLatestNewsSwiper, 100);
            return;
        }

        const prevBtn = document.querySelector('.latest-news-prev');
        const nextBtn = document.querySelector('.latest-news-next');

        const swiper = new Swiper('.latest-news-swiper', {
            slidesPerView: 'auto',
            spaceBetween: 19,
            speed: 600,
            loop: false,
            freeMode: false,
            watchSlidesProgress: true,
            breakpoints: {
                992: {
                    slidesPerView: 'auto',
                    spaceBetween: 19,
                }
            },
            on: {
                init: function() {
                    updateCardSizes();
                },
                slideChange: function() {
                    updateCardSizes();
                },
                slideChangeTransitionStart: function() {
                    updateCardSizes();
                }
            }
        });

        function updateCardSizes() {
            const slides = swiperEl.querySelectorAll('.swiper-slide');
            const activeIndex = swiper.activeIndex;
            
            slides.forEach((slide, index) => {
                if (index === activeIndex) {
                    slide.classList.add('swiper-slide-active');
                } else {
                    slide.classList.remove('swiper-slide-active');
                }
            });
            
            setTimeout(() => {
                if (swiper && swiper.update) {
                    swiper.update();
                }
            }, 50);
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                swiper.slidePrev();
            });
        }
        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                swiper.slideNext();
            });
        }
    }

    // Initialize Swiper after everything is loaded
    function initSwiperWhenReady() {
        if (typeof Swiper !== 'undefined') {
            initLatestNewsSwiper();
        } else {
            setTimeout(initSwiperWhenReady, 100);
        }
    }
    
    // Try to initialize immediately, or wait for load
    if (document.readyState === 'complete') {
        initSwiperWhenReady();
    } else {
        window.addEventListener('load', initSwiperWhenReady);
        setTimeout(initSwiperWhenReady, 500);
    }
});
