document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("registerForm");

    /* ===========================================
        VALIDACIÓN DE CAMPOS
    =========================================== */

    function showError(input, message) {
        removeError(input);

        const error = document.createElement("div");
        error.classList.add("error-message");
        error.innerText = message;

        input.insertAdjacentElement("afterend", error);
    }

    function removeError(input) {
        const next = input.nextElementSibling;
        if (next && next.classList.contains("error-message")) {
            next.remove();
        }
    }

    const validarRun = run => /^\d{7,8}$/.test(run);
    const validarDv = dv => /^[0-9kK]{1}$/.test(dv);
    const validarEmail = email => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

    /* ===========================================
        REGIONES → CIUDADES → COMUNAS
    =========================================== */

    const dataChile = {
        "Región Metropolitana": {
            "Santiago": ["Santiago Centro", "Providencia", "Las Condes", "Ñuñoa", "Maipú", "Puente Alto"],
            "Cordillera": ["Puente Alto", "San José de Maipo", "Pirque"]
        },
        "Valparaíso": {
            "Valparaíso": ["Valparaíso", "Viña del Mar", "Concón"],
            "Marga Marga": ["Quilpué", "Villa Alemana"]
        },
        "Biobío": {
            "Concepción": ["Concepción", "Talcahuano", "Hualpén"],
            "Los Ángeles": ["Los Ángeles", "Mulchén"]
        }
    };

    const regionSelect = document.getElementById("regionSelect");
    const citySelect = document.getElementById("citySelect");
    const comunaSelect = document.getElementById("comunaSelect");

    function cargarRegiones() {
        Object.keys(dataChile).forEach(region => {
            const option = document.createElement("option");
            option.value = region;
            option.textContent = region;
            regionSelect.appendChild(option);
        });
    }

    regionSelect.addEventListener("change", () => {
        citySelect.innerHTML = '<option value="">Seleccione ciudad</option>';
        comunaSelect.innerHTML = '<option value="">Seleccione comuna</option>';

        const region = regionSelect.value;

        if (region && dataChile[region]) {
            Object.keys(dataChile[region]).forEach(ciudad => {
                const option = document.createElement("option");
                option.value = ciudad;
                option.textContent = ciudad;
                citySelect.appendChild(option);
            });
        }
    });

    citySelect.addEventListener("change", () => {
        comunaSelect.innerHTML = '<option value="">Seleccione comuna</option>';

        const region = regionSelect.value;
        const ciudad = citySelect.value;

        if (region && ciudad && dataChile[region][ciudad]) {
            dataChile[region][ciudad].forEach(comuna => {
                const option = document.createElement("option");
                option.value = comuna;
                option.textContent = comuna;
                comunaSelect.appendChild(option);
            });
        }
    });

    cargarRegiones();

    /* ===========================================
        VALIDAR ANTES DE ENVIAR FORMULARIO
    =========================================== */

    form.addEventListener("submit", function (e) {
        let valido = true;

        const run = form.run;
        const dv = form.dv;
        const email = form.email;
        const pass1 = form.password1;
        const pass2 = form.password2;
        const telefono = form.phone;

        [run, dv, email, pass1, pass2, telefono].forEach(removeError);

        if (!validarRun(run.value)) {
            showError(run, "RUN inválido (7-8 dígitos).");
            valido = false;
        }

        if (!validarDv(dv.value)) {
            showError(dv, "DV inválido.");
            valido = false;
        }

        if (!validarEmail(email.value)) {
            showError(email, "Correo no válido.");
            valido = false;
        }

        if (pass1.value.length < 8) {
            showError(pass1, "Contraseña mínima de 8 caracteres.");
            valido = false;
        }

        if (pass1.value !== pass2.value) {
            showError(pass2, "Las contraseñas no coinciden.");
            valido = false;
        }

        if (!/^\d{8,12}$/.test(telefono.value)) {
            showError(telefono, "Teléfono inválido.");
            valido = false;
        }

        if (!valido) e.preventDefault();
    });

});