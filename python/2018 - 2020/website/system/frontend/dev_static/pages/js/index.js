$(document).ready(function(){
    $('select').formSelect();

    $('.modal').modal();
        
    $('.sidenav').sidenav();

    $(".regular").slick({
      dots: false,
      infinite: true,
      slidesToShow: 5,
      slidesToScroll: 5
    });

    $('.single').slick();
    $('.flexslider').flexslider({
      animation: "slide"
    });
});