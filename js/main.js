!function(i){"use strict";i(window).on("load",(function(){i("#preloader-active").delay(450).fadeOut("slow"),i("body").delay(450).css({overflow:"visible"})}));var e=i("ul#navigation");e.length&&e.slicknav({prependTo:".mobile_menu",closedSymbol:"+",openedSymbol:"-"}),function(){var e=i(".slider-active");function o(e){e.each((function(){var e=i(this),o=e.data("delay"),t="animated "+e.data("animation");e.css({"animation-delay":o,"-webkit-animation-delay":o}),e.addClass(t).one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend",(function(){e.removeClass(t)}))}))}e.on("init",(function(e,t){o(i(".single-slider:first-child").find("[data-animation]"))})),e.on("beforeChange",(function(e,t,s,a){o(i('.single-slider[data-slick-index="'+a+'"]').find("[data-animation]"))})),e.slick({autoplay:!1,autoplaySpeed:1e4,dots:!1,fade:!0,arrows:!1,prevArrow:'<button type="button" class="slick-prev"><i class="ti-shift-left"></i></button>',nextArrow:'<button type="button" class="slick-next"><i class="ti-shift-right"></i></button>',responsive:[{breakpoint:1024,settings:{slidesToShow:1,slidesToScroll:1,infinite:!0}},{breakpoint:991,settings:{slidesToShow:1,slidesToScroll:1,arrows:!1}},{breakpoint:767,settings:{slidesToShow:1,slidesToScroll:1,arrows:!1}}]})}();var o=i(".h1-testimonial-active");o.length&&o.slick({dots:!1,infinite:!0,speed:1e3,autoplay:!0,loop:!0,arrows:!1,prevArrow:'<button type="button" class="slick-prev"><i class="ti-angle-left"></i></button>',nextArrow:'<button type="button" class="slick-next"><i class="ti-angle-right"></i></button>',slidesToShow:1,slidesToScroll:1,responsive:[{breakpoint:1024,settings:{slidesToShow:1,slidesToScroll:1,infinite:!0,dots:!1,arrow:!1}},{breakpoint:600,settings:{slidesToShow:1,slidesToScroll:1,arrows:!1}},{breakpoint:480,settings:{slidesToShow:1,slidesToScroll:1,arrows:!1}}]});var t=i(".completed-active");t.length&&t.owlCarousel({slidesToShow:2,slidesToScroll:1,loop:!0,autoplay:!0,speed:3e3,smartSpeed:2e3,nav:!1,dots:!1,margin:15,autoplayHoverPause:!0,responsive:{0:{items:1},768:{items:2},992:{items:2},1200:{items:3}}});var s=i("select");s.length&&s.niceSelect(),i(window).on("scroll",(function(){i(window).scrollTop()<245?i(".header-sticky").removeClass("sticky-bar"):i(".header-sticky").addClass("sticky-bar")})),i(window).on("scroll",(function(){i(window).scrollTop()<245?i(".header-sticky").removeClass("sticky"):i(".header-sticky").addClass("sticky")})),i.scrollUp({scrollName:"scrollUp",topDistance:"300",topSpeed:300,animation:"fade",animationInSpeed:200,animationOutSpeed:200,scrollText:'<i class="ti-arrow-up"></i>',activeOverlay:!1}),i("[data-background]").each((function(){i(this).css("background-image","url("+i(this).attr("data-background")+")")})),(new WOW).init(),i("#mc_embed_signup").find("form").ajaxChimp();var a=i(".single_gallery_part, .img-pop-up");a.length&&a.magnificPopup({type:"image",gallery:{enabled:!0}})}(jQuery);