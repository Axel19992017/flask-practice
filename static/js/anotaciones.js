$(document).on("click", ".btn-Agregar", function (e) {
    limpiarInputs();
    $("#form-anotaciones").attr("action", "/Agregar");
    $("#modalAnotacion").modal("show");
});

$(document).on("click", ".btn-Editar", function (e) {
    const padre = $(this).closest(".card").children(".card-body");

    const id = $(padre).children(".id-nota").val();
    const titulo = $(padre).children(".card-head").children(".card-title").text();
    const contenido = $(padre).children(".card-text").text();
    console.log(id);
    console.log(titulo)
    console.log(contenido);

    $("#id").val(id)
    $("#titulo").val(titulo);
    $("#contenido").val(contenido);
    $("#form-anotaciones").attr("action", "/agregar");
    $("#modalAnotacion").modal("show");
});

function limpiarInputs() {
    $("#id").val("-1")
    $("#titulo").val("");
    $("#contenido").val("");
}

$(document).on("click", ".btn-Eliminar", function (e) {
    const padre = $(this).closest(".card").children(".card-body");
    const id = $(padre).children(".id-nota").val();
    $.confirm({
        title: 'Eliminar!',
        content: ` Desea eliminar esta nota
                <form action="/Eliminar" method="POST" class="text-left">
                    <div class="form-group">
                        <input class="form-control w-100" name="id" id="${id}" type="hidden"/>
                    </div>
                    <button class="btn btn-danger btn-sm" type="submit">Eliminar</button>
                </form>
                `,
        buttons: {
            cancel: function () {
                        //$.alert('Canceled!');
                    }
        }
    });

});