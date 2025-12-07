document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("loginForm");

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

    function validarEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    form.addEventListener("submit", function (e) {
        const emailInput = form.email;
        const passwordInput = form.password;

        removeError(emailInput);
        removeError(passwordInput);

        let valido = true;

        if (!validarEmail(emailInput.value)) {
            showError(emailInput, "Correo electrónico no válido.");
            valido = false;
        }

        if (!passwordInput.value) {
            showError(passwordInput, "La contraseña es obligatoria.");
            valido = false;
        }

        if (!valido) {
            e.preventDefault();
        }
    });
});