simpleDOM('#all-filter').bind('input', function(event){
  var inp = simpleDOM(this);
  simpleDOM('.search-name').each(function(){
    if(simpleDOM(this).attr('data-name').toLowerCase().indexOf(inp[0].value.toLowerCase()) === -1){
      simpleDOM(this).hide();
    } else {
      simpleDOM(this).css("display", "list-item");
    }
  });
});
simpleDOM('.tab').bind('click', function(event){
  $(".tab").removeClass("active");
  $(this).addClass("active");
  $(".tab-pane").hide();
  $($(this.firstElementChild).attr("href")).show();
  event.preventDefault();
});
