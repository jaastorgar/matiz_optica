document.addEventListener("DOMContentLoaded", () => {

    const boton = document.getElementById("btnContinuar");

    boton.addEventListener("click", () => {
        const servicioID = boton.getAttribute("data-servicio");
        const fecha = document.getElementById("fecha").value;

        if (!fecha) {
            alert("Debes seleccionar una fecha.");
            return;
        }

        window.location.href = `/appointments/horas/${servicioID}/${fecha}/`;
    });

});