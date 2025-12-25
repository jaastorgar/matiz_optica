document.addEventListener("DOMContentLoaded", () => {

  const modal = document.getElementById("product-modal");
  const modalBody = document.getElementById("modal-body");

  function openModal(html) {
    modalBody.innerHTML = html;
    modal.style.display = "flex";
    document.body.style.overflow = "hidden";
  }

  function closeModal() {
    modal.style.display = "none";
    modalBody.innerHTML = "";
    document.body.style.overflow = "";
  }

  // Click en productos
  document.addEventListener("click", (e) => {
    const card = e.target.closest(".open-modal");
    if (!card) return;

    const url = card.dataset.url;
    if (!url) return;

    fetch(url, {
      headers: { "X-Requested-With": "XMLHttpRequest" }
    })
      .then(res => res.text())
      .then(html => openModal(html))
      .catch(err => console.error("Modal error:", err));
  });

  // Cerrar con X
  document.addEventListener("click", (e) => {
    if (e.target.closest(".modal-close")) closeModal();
  });

  // Cerrar haciendo click fuera
  modal.addEventListener("click", (e) => {
    if (e.target === modal) closeModal();
  });

  // Escape
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeModal();
  });

});