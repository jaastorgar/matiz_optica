document.addEventListener("DOMContentLoaded", () => {

  const data = window.RESERVAS_DATA || [];
  const list = document.getElementById("reservas-list");
  const template = document.getElementById("reserva-template");
  const tabs = document.querySelectorAll(".reservas-tabs button");

  function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
  }

  function render(estado) {
    list.innerHTML = "";

    const filtradas = data.filter(r => r.estado === estado);

    if (!filtradas.length) {
      list.innerHTML = `<p class="empty">No hay citas en esta sección.</p>`;
      return;
    }

    filtradas.forEach(r => {
      const clone = template.content.cloneNode(true);

      clone.querySelector(".servicio").textContent = r.servicio;
      clone.querySelector(".fecha").textContent = r.fecha;
      clone.querySelector(".hora").textContent = r.hora;

      const estadoSpan = clone.querySelector(".estado");
      estadoSpan.textContent = r.estado_label;
      estadoSpan.className = `estado ${r.estado}`;

      const actions = clone.querySelector(".reserva-actions");

      /* ===============================
         ACCIONES POR ESTADO
      =============================== */

      if (r.estado === "pendiente") {
        actions.innerHTML = `
          <form method="POST" action="/appointments/confirmar-cita/${r.id}/">
            <input type="hidden" name="csrfmiddlewaretoken" value="${getCSRFToken()}">
            <button type="submit" class="btn confirmar">
              Confirmar
            </button>
          </form>

          <a href="/appointments/fecha/${r.servicio_id}/" class="btn outline">
            Reagendar
          </a>
        `;
      }

      if (r.estado === "confirmada") {
        actions.innerHTML = `
          <span class="confirmada-text">
            Hora confirmada
          </span>
        `;
      }

      if (r.estado === "atendida") {
        actions.innerHTML = `
          <span class="finalizada">
            Atendida
          </span>
        `;
      }

      list.appendChild(clone);
    });
  }

  /* ===============================
     TABS
  =============================== */
  tabs.forEach(btn => {
    btn.addEventListener("click", () => {
      tabs.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      render(btn.dataset.tab);
    });
  });

  // Inicial
  render("pendiente");
});