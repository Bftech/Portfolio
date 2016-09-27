var lastA = "";

$(".viewer_element a").click(function () {
  if ($(this).parent().attr("id") == lastA) {
    $(this).toggleClass("hovered");
    $(".viewer_element").not($(this).parent()).toggleClass("folded");
    $(this).parent().toggleClass("unfolded");
    $("#navbar").toggleClass("hidden");
  } else {
    $(".viewer_element").removeClass("unfolded");
    $(".viewer_element").addClass("folded");
    $(".viewer_element a").removeClass("hovered");
    $(this).parent().removeClass("folded");
    $(this).parent().addClass("unfolded");
    $(this).addClass("hovered");
    $("#navbar").addClass("hidden");
  }
  lastA = $(this).parent().attr("id");
});

$("#navbar a").click(function() {
  $("#navbar").toggleClass("show");
});
