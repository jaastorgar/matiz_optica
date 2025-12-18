document.addEventListener("DOMContentLoaded", () => {
  const modal = document.getElementById("product-modal");
  const modalBody = document.getElementById("modal-body");
  const closeBtn = document.querySelector(".modal-close");
  const backdrop = document.querySelector(".modal-backdrop");

  function openModalWithHTML(html) {
    modalBody.innerHTML = html;
    modal.classList.add("show");
    document.body.style.overflow = "hidden";
  }

  function closeModal() {
    modal.classList.remove("show");
    modalBody.innerHTML = "";
    document.body.style.overflow = "";
  }

  // Cerrar modal
  if (closeBtn) closeBtn.addEventListener("click", closeModal);
  if (backdrop) backdrop.addEventListener("click", closeModal);

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
  });

  // Delegación (mejor que forEach, y evita clicks raros)
  document.addEventListener("click", (e) => {
    const card = e.target.closest(".open-modal");
    if (!card) return;

    // Evita navegar si el user hace click en un link interno del card
    const isLink = e.target.closest("a");
    if (isLink) return;

    const url = card.dataset.url;

    // ✅ Guardas anti /shop/null
    if (!url || url === "null" || url === "undefined") {
      console.warn("Tarjeta sin data-url válida:", card);
      return;
    }

    fetch(url, {
      headers: { "X-Requested-With": "XMLHttpRequest" },
    })
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.text();
      })
      .then((html) => openModalWithHTML(html))
      .catch((err) => {
        console.error("Error cargando modal:", err);
      });
  });

  // Cerrar con click en cualquier elemento con data-modal-close dentro del modal
  document.addEventListener("click", (e) => {
    if (e.target.closest("[data-modal-close]")) closeModal();
  });
});