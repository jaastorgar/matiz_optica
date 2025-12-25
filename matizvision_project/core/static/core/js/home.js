document.addEventListener("DOMContentLoaded", () => {

  /* ===============================
     ACTIVE LINK AUTOMÁTICO
  =============================== */
  const navLinks = document.querySelectorAll(".nav-link");
  const currentPath = window.location.pathname;

  navLinks.forEach(link => {
    link.classList.remove("active");

    const linkPath = new URL(link.href).pathname;

    // Home exacto
    if (linkPath === "/" && currentPath === "/") {
      link.classList.add("active");
    }

    // Reservar cita
    else if (linkPath.includes("appointments") && currentPath.includes("appointments")) {
      link.classList.add("active");
    }

    // Tienda
    else if (linkPath.includes("shop") && currentPath.includes("shop")) {
      link.classList.add("active");
    }
  });


  /* ===============================
     DROPDOWN PERFIL USUARIO
  =============================== */
  const profileBtn = document.getElementById("profileBtn");
  const profileDropdown = document.getElementById("profileDropdown");

  if (profileBtn && profileDropdown) {
    profileBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      const isOpen = profileDropdown.classList.toggle("show");
      profileBtn.setAttribute("aria-expanded", isOpen ? "true" : "false");
    });

    document.addEventListener("click", () => {
      profileDropdown.classList.remove("show");
      profileBtn.setAttribute("aria-expanded", "false");
    });
  }


  /* ===============================
     MENÚ MÓVIL
  =============================== */
  const burgerBtn = document.getElementById("burgerBtn");
  const mobileMenu = document.getElementById("mobileMenu");

  if (burgerBtn && mobileMenu) {
    burgerBtn.addEventListener("click", (e) => {
      e.stopPropagation();
      mobileMenu.classList.toggle("show");
    });

    document.addEventListener("click", (e) => {
      if (!mobileMenu.contains(e.target) && !burgerBtn.contains(e.target)) {
        mobileMenu.classList.remove("show");
      }
    });
  }

});