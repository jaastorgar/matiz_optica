document.addEventListener("DOMContentLoaded", () => {

  /* ===============================
     ELEMENTOS
  =============================== */
  const burgerBtn = document.getElementById("burgerBtn");
  const mobileMenu = document.getElementById("mobileMenu");

  const profileBtn = document.getElementById("profileBtn");
  const profileDropdown = document.getElementById("profileDropdown");

  /* ===============================
     BURGER MENU (MÓVIL)
  =============================== */
  if (burgerBtn && mobileMenu) {
    burgerBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      mobileMenu.classList.toggle("show");

      // Cierra profile si está abierto
      if (profileDropdown) {
        profileDropdown.classList.remove("show");
      }
    });
  }

  /* ===============================
     PROFILE DROPDOWN
  =============================== */
  if (profileBtn && profileDropdown) {
    profileBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      profileDropdown.classList.toggle("show");

      // Cierra menú móvil si está abierto
      if (mobileMenu) {
        mobileMenu.classList.remove("show");
      }
    });
  }

  /* ===============================
     CLICK GLOBAL (CIERRE)
  =============================== */
  document.addEventListener("click", (e) => {

    // Cerrar mobile menu
    if (
      mobileMenu &&
      burgerBtn &&
      !mobileMenu.contains(e.target) &&
      !burgerBtn.contains(e.target)
    ) {
      mobileMenu.classList.remove("show");
    }

    // Cerrar profile dropdown
    if (
      profileDropdown &&
      profileBtn &&
      !profileDropdown.contains(e.target) &&
      !profileBtn.contains(e.target)
    ) {
      profileDropdown.classList.remove("show");
    }
  });

});