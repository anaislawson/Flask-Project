$(window).on("scroll", function() {
    if($(window).scrollTop() > $(window).height()) {
        $("nav").addClass("active");
    } else {
        //remove the background property so it comes transparent again (defined in your css)
       $("nav").removeClass("active");
    }
});


// Navigation Bar JS

$("#logo").click(function() {
    $('html, body').animate({
        scrollTop: $("#homepage-image").offset().top
    }, 2000);
});

$("#about-me").click(function() {
    $('html, body').animate({
        scrollTop: $("#about").offset().top
    }, 2000);
});

// About Me JS

$("#about-image").on("click", function() {
  $("#myModal").fadeIn();
});

$(".close").on("click", function() {
  $("#myModal").fadeOut();
});