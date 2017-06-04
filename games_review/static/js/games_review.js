/**
 * Created by oliver on 04/06/17.
 */

var hoverIn = function() {
    //$(this).css("height","unset");
    $(this).find(".img-container").fadeIn(500);
};

var hoverOut = function () {
    $(this).find(".img-container").fadeOut(100);
};

$(function () {
    $('li.game-item').hover(hoverIn, hoverOut);
});