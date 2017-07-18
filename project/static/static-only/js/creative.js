(function($) {
    "use strict"; // Start of use strict

    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $(document).on('click', 'a.page-scroll', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: ($($anchor.attr('href')).offset().top - 50)
        }, 1250, 'easeInOutExpo');
        event.preventDefault();
    });

    // Highlight the top nav as scrolling occurs
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 51
    });

    // Closes the Responsive Menu on Menu Item Click
    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });

    // Offset for Main Navigation
    $('#mainNav').affix({
        offset: {
            top: 100
        }
    })

    // Initialize and Configure Scroll Reveal Animation
    window.sr = ScrollReveal();
    sr.reveal('.sr-icons', {
        duration: 600,
        scale: 0.3,
        distance: '0px'
    }, 200);
    sr.reveal('.sr-button', {
        duration: 1000,
        delay: 200
    });
    sr.reveal('.sr-contact', {
        duration: 600,
        scale: 0.3,
        distance: '0px'
    }, 300);

    // Initialize and Configure Magnific Popup Lightbox Plugin
    $('.popup-gallery').magnificPopup({
        delegate: 'a',
        type: 'image',
        tLoading: 'Loading image #%curr%...',
        mainClass: 'mfp-img-mobile',
        gallery: {
            enabled: true,
            navigateByImgClick: true,
            preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
        }
    });
    /*#####################
    Additional jQuery (required)
    #####################*/
        var boxheight = $('.carousel-inner').height();
    	var itemlength = $('.item').length;
    	var triggerheight = Math.round(boxheight/itemlength+1);
    	$('.list-group-item').height(triggerheight);

    	var clickEvent = false;
    	$('#myCarousel').carousel({
    		interval:   4000
    	}).on('click', '.list-group li', function() {
    			clickEvent = true;
    			$('.list-group li').removeClass('active');
    			$(this).addClass('active');
    	}).on('slid.bs.carousel', function(e) {
    		if(!clickEvent) {
    			var count = $('.list-group').children().length -1;
    			var current = $('.list-group li.active');
    			current.removeClass('active').next().addClass('active');
    			var id = parseInt(current.data('slide-to'));
    			if(count == id) {
    				$('.list-group li').first().addClass('active');
    			}
    		}
    		clickEvent = false;
    	});
})(jQuery); // End of use strict
