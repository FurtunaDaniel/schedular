$(document).ready(function () {
$('.student-option').click(function(){
$('.student-option').removeClass('active');
  $(this).toggleClass('active') 
})
$( "#datepicker" ).datepicker();
})
