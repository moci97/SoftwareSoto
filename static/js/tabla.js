

$(document).ready(function () {

    $(".selec").click(function () {

        var marcado = $(".checkbox1").is(":checked");

        if (!marcado) {
            $(this).text("Seleccionado");


        } else {
            $(this).text("Seleccionar");

        }
    });


});







