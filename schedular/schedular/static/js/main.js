$(document).ready(function() {

  $(document).on('click', 'a[rel~=confirm]', function(e) {
    e.preventDefault();
    var theHREF = $(this).attr("href");

    $.confirm({
      'title': 'Confirm Action',
      'message': 'Are you sure you want to do this?  It cannot be undone.',
      'buttons': {
        'Yes': {
          'class': 'btn-default',
          'action': function() {
            window.location.href = theHREF;
          }
        },
        'No': {
          'class': 'btn-default'
        }
      }
    });
  });

  var themeColorUser = $('#id_color_page').val();
  $('body').css("color", themeColorUser);
  var themeColor = $('body').css('color');

  // Set even table rows bg color
  var tableRowOpacity = ', 0.1)';
  var tableRowBg = themeColor.replace('rgb', 'rgba').replace(')', tableRowOpacity);
  $('.widget-table__row:nth-child(even)').css('background-color', tableRowBg);

  // RGB to HSL converter
  function rgb2hsl(rgbArr) {
    var r1 = rgbArr[0] / 255;
    var g1 = rgbArr[1] / 255;
    var b1 = rgbArr[2] / 255;

    var maxColor = Math.max(r1, g1, b1);
    var minColor = Math.min(r1, g1, b1);
    //Calculate L:
    var L = (maxColor + minColor) / 2;
    var S = 0;
    var H = 0;
    if (maxColor !== minColor) {
      //Calculate S:
      if (L < 0.5) {
        S = (maxColor - minColor) / (maxColor + minColor);
      } else {
        S = (maxColor - minColor) / (2.0 - maxColor - minColor);
      }
      //Calculate H:
      if (r1 === maxColor) {
        H = (g1 - b1) / (maxColor - minColor);
      } else if (g1 === maxColor) {
        H = 2.0 + (b1 - r1) / (maxColor - minColor);
      } else {
        H = 4.0 + (r1 - g1) / (maxColor - minColor);
      }
    }

    L = L * 100;
    S = S * 100;
    H = H * 60;
    if (H < 0) {
      H += 360;
    }
    var result = [H, S, L];
    return result;
  }
  // Theme editor
  var userColorRGB = themeColor.match(/\d+/g);
  var userColorHSL = rgb2hsl(userColorRGB);
  var userColorH = Math.round(parseFloat(userColorHSL[0]));
  var userColorS = Math.round(parseFloat(userColorHSL[1]));
  var userColorL = Math.round(parseFloat(userColorHSL[2]));
  var userColorRangeH = $('#themeSliderH');
  var userColorRangeS = $('#themeSliderS');

  userColorRangeH.val(userColorH);
  userColorRangeS.val(userColorS);

  userColorRangeS.css('color', 'hsl(' + userColorH + ', ' + '100%, ' + userColorL + '%)');

  userColorRangeH.on("input", function() {
    $('body').css('color', 'hsl(' + this.value + ', ' + userColorS + '%, ' + userColorL + '%)');
    userColorH = this.value;
    $('#id_color_page').val($('body').css("color"));
    userColorRangeS.css('color', 'hsl(' + this.value + ', ' + '100%, ' + userColorL + '%)');
  });

  userColorRangeS.on("input", function() {
    $('body').css('color', 'hsl(' + userColorH + ', ' + this.value + '%, ' + userColorL + '%)');
    userColorS = this.value;
    $('#id_color_page').val($('body').css("color"));
  });

});
