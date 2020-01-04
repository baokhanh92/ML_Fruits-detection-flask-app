function readURL(input) {
  console.log(input);
  if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function(e) {
      $(".text-select").hide();
      $(".spinner-border").removeClass("d-none");
      $("#catOrDog").attr("src", e.target.result);
      $("#send").click();
    };

    reader.readAsDataURL(input.files[0]);
  }
}

$("#file").change(function() {
  readURL(this);
});

$(".new_Btn").bind("click", function() {
  $("#file").click();
});

$(".alert").bind("click", function() {
  $(".alert").hide();
});

$(".wrong").bind("click", function() {
  $(".alert").removeClass("d-none");
  $(".wrong").hide();
});
