 $(function() {
    $( "#slider-range-min" ).slider({
      range: "min",
      value: 50,
      min: 0,
      max: 100,
      slide: function( event, ui ) {
        $( "#amount" ).val( "$" + ui.value + ",000");
        $(".a, .b, .c, .d").width(ui.value + "%");
      }
    });
    $(".ui-slider-handle").text("<>");
    $( "#amount" ).val( "$" + $( "#slider-range-min" ).slider( "value") + ",000");
  });