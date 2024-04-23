$(document).ready(function () {
    $("#stop").attr("disabled", true);
    $("#start").click(function () {
        $("#stop").attr("disabled", false);
    });
    $("#test").click(function () {
        $("#stop").attr("disabled", false);
    });
});
