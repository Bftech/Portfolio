
$(".viewer_element a").click(function () {
  $(this).toggleClass("hovered");
  $(".viewer_element").toggleClass("folded");
  $(this).parent().toggleClass("unfolded");
})
