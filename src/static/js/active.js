(function ($) {
    "use strict";

    const $window = $(window),
        $body = $('body')

    /* Header Sticky */
    function headerSticky() {
        if ($window.scrollTop() > 350) {
            $('.sticky-header').addClass('is-sticky');
        } else {
            $('.sticky-header').removeClass('is-sticky');
        }
    }

    /* Mobile Sub Menu Toggle Function */
    const $mobileSubMenuToggle = $('.mobile-sub-menu-toggle')
    $mobileSubMenuToggle.on('click', function () {
        const $this = $(this),
            $mobileSubMenuToggleClass = '.mobile-sub-menu-toggle',
            $mobileSubMenuClass = '.mobile-sub-menu';
        if ($this.hasClass('active')) {
            $this.removeClass('active').closest('li').removeClass('active').find($mobileSubMenuToggleClass).removeClass('active').closest('li').removeClass('active').find($mobileSubMenuClass).slideUp()
        } else {
            $this.addClass('active').siblings($mobileSubMenuClass).slideDown()
            $this.closest('li').addClass('active').siblings().find($mobileSubMenuToggleClass).removeClass('active').closest('li').removeClass('active').find($mobileSubMenuClass).slideUp()
        }
    })


    /* Swiper Slider */
    const productCarousel = new Swiper('.product-carousel', {
        loop: true,
        slidesPerView: 1,
        spaceBetween: 15,
        pagination: {
            el: '.product-carousel .swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.product-carousel .swiper-button-next',
            prevEl: '.product-carousel .swiper-button-prev',
        },
        breakpoints: {
            576: {
                slidesPerView: 2
            },
            768: {
                slidesPerView: 2,
                spaceBetween: 30
            },
            992: {
                slidesPerView: 3,
                spaceBetween: 30
            },
            1200: {
                slidesPerView: 4,
                spaceBetween: 30
            }
        }
    });

})(jQuery);	



