function makeid(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() *
            charactersLength));
    }
    return result;
}




/*******homepage words animation */
const homepage_hero_title_tl = gsap.timeline({ paused: true });

if ($('.home-page').length) {
    const homepage_hero_title = document.querySelectorAll(".left-block h1, .right-block h1");
    //homepage_hero_title_tl;
    homepage_hero_title.forEach(h1 => {
        const ht_lines = new SplitText(h1, { type: "lines", linesClass: "title-div", mask: "lines", });
        homepage_hero_title_tl.from(ht_lines.lines, {
            y: 100,
            opacity: 0,
            duration: 1.5,
            mask: "lines",
            ease: "back.out(1.7)",
            onComplete: function () {
                if($('.hero-video').length){
                    var hero_video = $('.hero-video')[0];
                    hero_video.muted= true;
                    hero_video.play();
                }
                
            }
        }, "0.5");
    });



    // Split text into words
    const homepage_title_split = new SplitText(".hero-section .right-block span", { type: "words", wordsClass: "dynamic-word" });
    const words = homepage_title_split.words;
    gsap.set(words, { y: 100, opacity: 0 });
    var dynamic_words_tl = gsap.timeline();
    words.forEach((word, i) => {

        dynamic_words_tl.to(word, {
            duration: 0.8,
            y: 0,
            opacity: 1,
            ease: "back.out(0.7)",
        }).to(word, {
                duration: 0.5,
                y: -100,
                opacity: 0,
                ease: "power2.in",
                onComplete: function () {
                    if (i === words.length - 1) {
                        dynamic_words_tl.restart();
                    }
                }
            }, "+=0.8")
    });
}

var menu_tl = gsap.timeline({ paused: true });
menu_tl
.from('.menu-bottom-line', {
    width: 0,
    duration: 4,
})
// Starts at 1 second into the timeline
.from('.hero-section .logo', {
    scale: 0.6,
    opacity: 0,
    duration: 1.5,
}, 1)
// Starts at 2.5 seconds into the timeline
.from('.header li, .header .brand, .header .menu-icon', {
    y: -50,
    opacity: 0,
    duration: 1,
    ease: "power3.out",
    onStart: function () {
        homepage_hero_title_tl.play();
    }
}, 2.5);
$(window).on('load', function () {
    menu_tl.play();
});




$(function () {
    if ($('.gallery-slider').length) {
        $('.gallery-slider').each(function () {
            let gallery_id = "gallery-" + makeid(10);
            $(this).attr('id', gallery_id);
            lightGallery(document.querySelector('#' + gallery_id), {
                thumbnail: true,
                selector: '.item',
                licenseKey: 'A8DB462B-20964EBE-95B89530-6E0512EB',
                subHtmlSelectorRelative: true
            });
            $('#' + gallery_id).owlCarousel({
                loop: true,
                nav: true,
                dots: false,
                responsive: {
                    0: {
                        items: 1
                    },
                }
            });
        });
    }

    if ($("#hero-video-popup").length) {
        lightGallery(document.querySelector('#hero-video-popup'), {
            plugins: [lgVideo],
            licenseKey: 'A8DB462B-20964EBE-95B89530-6E0512EB',
            speed: 500,
            selector: 'a',
            videojs: true,
            autoplayFirstVideo: true,
            download: false,
            counter: false,
            videojsOptions: {
                muted: true,
            },
        });
    }

    $('.video-with-play-btn').each(function () {
        var $section = $(this);
        var $video = $section.find('video');
        var $overlay = $section.find('.overlay');
        var $playBtn = $section.find('.play-btn');

        $playBtn.on('click', function (e) {
            e.preventDefault();
            $overlay.fadeOut(300); // hide overlay smoothly
            $video.get(0).play();  // play the video
        });

        // Optional: if user pauses video, show overlay again
        $video.on('pause', function () {
            $overlay.fadeIn(300);
        });
    });

    if ($("#marqueeTrack").length) {
        const track = $("#marqueeTrack");
        const trackWidth = track[0].scrollWidth;

        // GSAP animation
        const marqueeAnim = gsap.to(track, {
            x: -trackWidth / 3, // slide by one set of text
            duration: 15,
            ease: "linear",
            repeat: -1
        });

        // Pause on hover
        $(".scrolling-title").hover(
            function () { marqueeAnim.pause(); },   // mouse enter
            function () { marqueeAnim.resume(); }  // mouse leave
        );
    }

});



document.addEventListener("DOMContentLoaded", function () {

    const mainMenuWrap = document.querySelector(".main-menu-wrap");
    if (!mainMenuWrap) return;

    const mainMenuItems = mainMenuWrap.querySelectorAll(".main-menu-items .ancestor > a[data-link]");
    const submenuContainer = mainMenuWrap.querySelector(".submenu-container");
    const submenus = $(".submenu-items");

    mainMenuItems.forEach(menuItem => {
        const linkData = menuItem.getAttribute("data-link");
        menuItem.addEventListener("click", (e) => {
            e.preventDefault(); // prevent default navigation

            // Hide all submenus first
            submenus.hide();

            if (linkData) {
                const targetSubmenu = submenuContainer.querySelector(`.${linkData}`);
                if (targetSubmenu) {
                    targetSubmenu.style.display = "block";
                    const submenuItems = targetSubmenu.querySelectorAll("li.level2");

                    // ✅ Kill any existing tweens on submenuItems before starting new one
                    gsap.killTweensOf(submenuItems);

                    // Reset their initial state before playing animation again
                    gsap.set(submenuItems, { x: -30, autoAlpha: 0 });

                    // Fresh animation each time
                    gsap.to(submenuItems, {
                        x: 0,
                        autoAlpha: 1,
                        duration: 0.4,
                        stagger: 0.08,
                        ease: "power2.out"
                    });
                }
            }
            return false;
        });
        menuItem.addEventListener("dblclick", (e) => {
            window.location.href = menuItem.getAttribute("href");
        });

    });



    const currentUrl = window.location.pathname;
    const menuLinks = document.querySelectorAll(".menu-wrap a");

    menuLinks.forEach(link => {
        const href = link.getAttribute("href");
        if (href === currentUrl) {
            link.classList.add("active");

            // Find parent submenu
            const submenu = link.closest(".submenu-items");
            if (submenu) {
                const parentLink = submenu.getAttribute("data-parent-link");
                if (parentLink) {
                    const mainLink = document.querySelector(`.main-menu a[data-link="${parentLink}"]`);
                    if (mainLink) {
                        // ✅ Trigger your existing vanilla JS click handler
                        //mainLink.dispatchEvent(new ("click"));
                        console.log("click");

                        console.log(href + " ----- " + currentUrl);
                        mainLink.classList.add("active");
                    }
                }
            }
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const currentUrl = window.location.pathname;
    const mainMenuWrap = document.querySelector(".main-menu-wrap");
    if (!mainMenuWrap) return;

    const mainMenuItems = mainMenuWrap.querySelectorAll(".main-menu-items .ancestor > a[data-link]");
    const submenuContainer = mainMenuWrap.querySelector(".submenu-container");
    const submenus = document.querySelectorAll(".submenu-items");

    // --- Common function to open submenu ---
    function openSubmenu(linkData) {
        submenus.forEach(sm => (sm.style.display = "none"));
        if (!linkData) return;

        const targetSubmenu = submenuContainer?.querySelector(`.${linkData}`);
        if (targetSubmenu) {
            targetSubmenu.style.display = "block";
            const submenuItems = targetSubmenu.querySelectorAll("li.level2");

            gsap.killTweensOf(submenuItems);
            gsap.set(submenuItems, { x: -30, autoAlpha: 0 });
            gsap.to(submenuItems, {
                x: 0,
                autoAlpha: 1,
                duration: 0.4,
                stagger: 0.08,
                ease: "power2.out"
            });
        }
    }

    // --- Click & double click setup ---
    mainMenuItems.forEach(menuItem => {
        const linkData = menuItem.getAttribute("data-link");
        let clickTimer = null;

        menuItem.addEventListener("click", (e) => {
            e.preventDefault();
            // Wait briefly to see if a double-click happens
            openSubmenu(linkData);
        });

        menuItem.addEventListener("dblclick", (e) => {
            e.preventDefault();
            window.location.href = menuItem.getAttribute("href");
        });
    });

    // --- Auto active class + submenu open ---
    const menuLinks = document.querySelectorAll(".menu-wrap a");
    menuLinks.forEach(link => {
        const href = link.getAttribute("href");
        if (href === currentUrl) {
            link.classList.add("active");

            const submenu = link.closest(".submenu-items");
            if (submenu) {
                const parentLink = submenu.getAttribute("data-parent-link");
                if (parentLink) {
                    const mainLink = document.querySelector(`.main-menu a[data-link="${parentLink}"]`);
                    if (mainLink) {
                        // ✅ only simulate opening submenu (not navigating)
                        const linkData = mainLink.getAttribute("data-link");
                        openSubmenu(linkData);
                        mainLink.classList.add("active");
                    }
                }
            }else{
                const selfLinkData = link.getAttribute("data-link");
                if (selfLinkData) {
                    // ✅ Trigger submenu open for itself
                    openSubmenu(selfLinkData);
                    link.classList.add("active");
                }

            }

        }
    });
});









$(document).ready(function () {








    /*******homepage words animation end */


    const $menuIcon = $(".menu-icon");
    const $menuWrap = $(".menu-wrap");
    const $mainContent = $("#main-content");
    var megamenu_tl = gsap.timeline({ paused: true });

    megamenu_tl.to($menuWrap, {
        height: "100vh",
        duration: 0.75,
        ease: "power3.out",
    });

    // Play it when you need to

    // GSAP open animation (Top → Down)
    function openMenu() {
        $menuWrap.addClass("active");
        gsap.fromTo($menuWrap,
            { y: "-100%", opacity: 0 },
            { y: "0%", opacity: 1, duration: 0.6, ease: "power3.out" }
        );
        $("body").addClass("menu-open");
        $menuIcon.attr("aria-expanded", "true");

        if ($mainContent.length) $mainContent.attr("aria-hidden", "true");
    }

    // GSAP close animation (Down → Up)
    function closeMenu() {
        gsap.to($menuWrap, {
            y: "-100%",
            opacity: 0,
            duration: 0.5,
            ease: "power3.in",
            onComplete: function () {
                $menuWrap.removeClass("active");
            }
        });
        $("body").removeClass("menu-open");
        $menuIcon.attr("aria-expanded", "false");
        if ($mainContent.length) $mainContent.removeAttr("aria-hidden");
    }


    // Triggers

    $menuIcon.on("click", function () {
        if ($(this).hasClass('open')) {
            megamenu_tl.timeScale(1.3).reverse();
            $('body').removeClass('menu-active');
            $(this).removeClass('open');
        } else {
            megamenu_tl.play();
            $('body').addClass('menu-active');
            $(this).addClass('open');
        }

    });
    // $closeButton.on("click", function () {

    // });
    // Escape key
    $(document).on("keydown", function (e) {
        if (e.key === "Escape" && $menuWrap.hasClass("active")) {
            closeMenu();
        }
    });

    // Click outside
    $(document).on("click", function (e) {
        if ($menuWrap.hasClass("active") &&
            !$menuWrap.is(e.target) &&
            $menuWrap.has(e.target).length === 0 &&
            !$menuIcon.is(e.target)) {
            closeMenu();
        }
    });

    var owl = $('.center-image-slider .owl-carousel');
    owl.owlCarousel({
        center: true,
        items: 1,
        nav: true,
        loop: true,
        dots: false,
        margin: 21,
        responsive: {
            600: {
                items: 1.75
            }
        }
    });

    // Get total slides (excluding cloned)
    var totalSlides = owl.find('.owl-item:not(.cloned)').length;
    $('.total-slides').text(totalSlides);

    // Update current slide number on change
    owl.on('changed.owl.carousel', function (event) {
        var currentSlide = (event.item.index - event.relatedTarget._clones.length / 2) % totalSlides + 1;
        if (currentSlide <= 0) currentSlide = totalSlides; // fix negative index
        $('.current-slide').text(currentSlide);
    });

    // Set initial slide number
    var startSlide = owl.find('.owl-item.active').first().index() - owl.find('.owl-item.cloned').length / 2 + 1;
    if (startSlide <= 0) startSlide = totalSlides;
    $('.current-slide').text(startSlide);

    $('.card-grid-with-title').each(function () {
        var card_gridowl = $(this).find('.owl-carousel');
        card_gridowl.owlCarousel({
            nav: false,
            loop: true,
            dots: false,
            margin: 20,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 2
                },
                1024: {
                    items: 4
                }
            }
        });
        $(this).find('.custom-owl-prev').click(function () {
            card_gridowl.trigger('prev.owl.carousel');
        });

        $(this).find('.custom-owl-next').click(function () {
            card_gridowl.trigger('next.owl.carousel');
        });
    });

    if ($('.card-grid-with-title-and-text').length) {
        $('.card-grid-with-title-and-text').each(function () {
            var card_gridowlText = $(this).find('.owl-carousel');
            card_gridowlText.owlCarousel({
                nav: false,
                loop: true,
                dots: false,
                margin: 20,
                responsive: {
                    0: {
                        items: 1
                    },
                    768: {
                        items: 2
                    },
                    1024: {
                        items: 4
                    }
                }
            });

            $(this).find('.custom-owl-prev').click(function () {
                card_gridowlText.trigger('prev.owl.carousel');
            });

            $(this).find('.custom-owl-next').click(function () {
                card_gridowlText.trigger('next.owl.carousel');
            });
        });

        function stopVideo($item) {
            var video = $item.find('video').get(0);
            if (video) {
                video.pause();
                video.currentTime = 0;
                video.controls = false;
                video.muted = true;

                // Show poster image again
                $item.find('video').hide();
                $item.find('img').show();
            }
        }

        function playVideo($item, unmute = false) {
            var video = $item.find('video').get(0);
            if (video) {
                // Hide poster image when playing video
                $item.find('img').hide();
                $item.find('video').show();

                video.muted = !unmute;
                video.controls = true;
                video.play();
            }
        }

        // Hover functionality
        $('.card-grid-with-title-and-text .item').hover(
            function () {
                var currentItem = $(this);
                // Skip if this item is set as current
                if (currentItem.hasClass('current')) return;

                // Stop all other non-current videos
                $('.card-grid-with-title-and-text .item').not('.current').each(function () {
                    stopVideo($(this));
                });

                playVideo(currentItem, true); // muted preview
            },
            function () {
                var currentItem = $(this);

                // Do nothing if it’s a "current" (clicked) item
                if (currentItem.hasClass('current')) return;

                stopVideo(currentItem);
            }
        );

        // Play button click → set as current (user-controlled playback)
        $('.card-grid-with-title-and-text .video-play-btn').on('click', function (e) {
            e.preventDefault();
            var currentItem = $(this).closest('.item');

            if (currentItem.hasClass('current')) {
                stopVideo(currentItem);
                currentItem.removeClass('current');
                return;
            }

            // Remove current class from others and reset their videos
            $('.card-grid-with-title-and-text .item').removeClass('current').each(function () {
                stopVideo($(this));
            });

            // Mark this one as current
            currentItem.addClass('current');

            playVideo(currentItem, true);
        });
    }

    $('.latest-blog-section').each(function () {
        var card_blogowl = $(this).find('.owl-carousel');
        if (card_blogowl) {
            card_blogowl.owlCarousel({
                nav: false,
                loop: true,
                dots: false,
                margin: 20,
                responsive: {
                    0: {
                        items: 1
                    },
                    768: {
                        items: 2
                    },
                    1024: {
                        items: 4
                    }
                }
            });
            $(this).find('.custom-owl-prev').click(function () {
                card_blogowl.trigger('prev.owl.carousel');
            });

            $(this).find('.custom-owl-next').click(function () {
                card_blogowl.trigger('next.owl.carousel');
            });
        }
    });

    $('.fullwidth-media-section').each(function () {
        var fullwidth_slider = $(this);
        if ($(fullwidth_slider).length) {
            fullwidth_slider.owlCarousel({
                nav: true,
                loop: true,
                dots: false,
                margin: 20,
                items: 1
            });

            $(this).find('.custom-owl-prev').click(function () {
                fullwidth_slider.trigger('prev.owl.carousel');
            });

            $(this).find('.custom-owl-next').click(function () {
                fullwidth_slider.trigger('next.owl.carousel');
            });
        }
    });






    gsap.registerPlugin(ScrollTrigger);
    gsap.registerPlugin(SplitText);
    // Generic fade/slide UP for .anim--text-js

    gsap.utils.toArray(".anim-title-js").forEach(el => {
        gsap.from(el, {
            scrollTrigger: {
                trigger: el,
                start: "top bottom",
                toggleActions: "play none none reverse"
            },
            y: 50,
            opacity: 0,
            duration: 1,
            ease: "power3.out",
        });
    });

    gsap.utils.toArray(".anim-text-js").forEach(el => {
        gsap.from(el, {
            scrollTrigger: {
                trigger: el,             // trigger each element individually
                start: "top 80%",        // animation starts when element enters viewport
                toggleActions: "play none none reverse",
                markers: false           // set to true to debug
            },
            y: 50,
            opacity: 0,
            duration: 1,
            ease: "power3.out"
        });
    });

    // Text Animation from LEFT
    gsap.utils.toArray(".anim-from-left-text-js").forEach(el => {
        gsap.from(el, {
            scrollTrigger: {
                trigger: el,
                start: "top 85%",
                toggleActions: "play none none reverse"
            },
            x: -80, // animate from left
            opacity: 0,
            duration: 1,
            ease: "power3.out"
        });
    });

    // Text Animation from RIGHT
    gsap.utils.toArray(".anim-from-right-text-js").forEach(el => {
        gsap.from(el, {
            scrollTrigger: {
                trigger: el,
                start: "top 85%",
                toggleActions: "play none none reverse"
            },
            x: 80, // animate from right
            opacity: 0,
            duration: 1,
            ease: "power3.out"
        });
    });

    // Animate all grid items
    gsap.utils.toArray(".anim-grid-js").forEach(row => {
        const blocks = row.querySelectorAll(".grid-item");

        if (blocks.length > 0) {
            gsap.from(blocks, {
                scrollTrigger: {
                    trigger: row,          // trigger animation when this row enters viewport
                    start: "top 80%",      // adjust when animation starts
                    toggleActions: "play none none reverse",
                    markers: false          // set true to debug
                },
                y: 50,                    // slide up from 50px below
                opacity: 0,               // fade in
                duration: 0.8,
                ease: "power3.out",
                stagger: 0.2              // animate items one by one
            });
        }
    });



    // Menu sticky
    let lastScroll = 0;
    const header = document.querySelector("header.header");

    ScrollTrigger.create({
        start: "top top",
        end: 99999,
        onUpdate: (self) => {
            const currentScroll = self.scroll();

            if (currentScroll > lastScroll && currentScroll > 150) {
                // scrolling down
                gsap.to(header, { y: -300, duration: 0.4, ease: "power2.out" });
                header.classList.remove("is-sticky");
            } else {
                // scrolling up
                gsap.to(header, { y: 0, duration: 0.4, ease: "power2.out" });
                if (currentScroll > 150) {
                    header.classList.add("is-sticky");
                } else {
                    header.classList.remove("is-sticky");
                }

            }

            lastScroll = currentScroll;
        }

    });

    
    



    $('.main-menu-wrap .has-tertiary-menu > a .icon').on('click', function(e) {
        e.preventDefault();

        var $parentLi = $(this).parent();
        var $currentMenu = $parentLi.find('.tertiary-menu-list');

        // Toggle clicked menu
        if ($parentLi.hasClass('active')) {
            gsap.to($currentMenu, {height: 0, opacity: 0, duration: 0.4, ease: "power2.out"});
            $parentLi.removeClass('active');
            return;
        }

        // Close any other open menus
        $('.has-tertiary-menu.active').not($parentLi).each(function() {
            var $openMenu = $(this).find('.tertiary-menu-list');
            gsap.to($openMenu, {height: 0, opacity: 0, duration: 0.4, ease: "power2.out"});
            $(this).removeClass('active');
        });

        // Open clicked menu
        $parentLi.addClass('active');
        gsap.fromTo($currentMenu,
            {height: 0, opacity: 0},
            {height: "auto", opacity: 1, duration: 0.4, ease: "power2.out"}
        );
    });
});