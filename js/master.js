$("#navbar a").click(function () {
  $("#page_background").toggleClass("blurred",true);
  $(".viewer").toggleClass("hidden",true);
  $("#"+this.innerHTML.toLowerCase()+"_viewer").toggleClass("hidden",false);
})
