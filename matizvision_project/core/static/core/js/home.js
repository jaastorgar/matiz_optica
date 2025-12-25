document.addEventListener("DOMContentLoaded", () => {

  /* ===============================
     MENÚ MÓVIL (HAMBURGUESA)
  =============================== */
  const burgerBtn = document.getElementById("burgerBtn");
  const mobileMenu = document.getElementById("mobileMenu");

  if (burgerBtn && mobileMenu) {
    burgerBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      mobileMenu.classList.toggle("show");
    });

    // Cerrar menú móvil al hacer click fuera
    document.addEventListener("click", (e) => {
      if (!mobileMenu.contains(e.target) && !burgerBtn.contains(e.target)) {
        mobileMenu.classList.remove("show");
      }
    });
  }


  /* ===============================
     DROPDOWN PERFIL USUARIO
  =============================== */
  const profileBtn = document.getElementById("profileBtn");
  const profileDropdown = document.getElementById("profileDropdown");

  if (profileBtn && profileDropdown) {

    profileBtn.addEventListener("click", (e) => {
      e.stopPropagation();

      const isOpen = profileDropdown.classList.toggle("show");
      profileBtn.setAttribute(
        "aria-expanded",
        isOpen ? "true" : "false"
      );
    });

    // Cerrar dropdown al hacer click fuera
    document.addEventListener("click", () => {
      profileDropdown.classList.remove("show");
      profileBtn.setAttribute("aria-expanded", "false");
    });
  }

});