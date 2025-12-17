document.addEventListener("DOMContentLoaded", () => {
  // Mobile menu
  const burgerBtn = document.getElementById("burgerBtn");
  const mobileMenu = document.getElementById("mobileMenu");

  if (burgerBtn && mobileMenu) {
    burgerBtn.addEventListener("click", () => {
      mobileMenu.classList.toggle("show");
    });
  }

  // Profile dropdown
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
});