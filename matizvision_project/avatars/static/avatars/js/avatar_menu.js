document.addEventListener("DOMContentLoaded", () => {
  const avatarContainers = document.querySelectorAll(".avatar-lottie");

  avatarContainers.forEach(container => {
    const animationPath = container.dataset.lottieUrl;

    if (!animationPath) return;

    lottie.loadAnimation({
      container: container,
      renderer: "svg",
      loop: true,
      autoplay: true,
      path: animationPath
    });
  });
});