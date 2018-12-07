$(document).ready(function () {

    $(".selec").click(function () {

        var marcado = $(".checkbox1").is(":checked");

        if (!marcado) {
            $(this).text("Seleccionado");


        } else {
            $(this).text("Seleccionar");

        }
    });

    $('#enviar').click(function () {

        if (!$('#inputUniversidad').val()) {
            alert("Error, Selecciona una universidad");
        }
        if (!$('#inputFacultad').val()) {
            alert("Error, Selecciona una facultad");
        }
        if (!$('#inputFacultad').val()) {
            alert("Error, Selecciona una facultad");
        }
    })
});







