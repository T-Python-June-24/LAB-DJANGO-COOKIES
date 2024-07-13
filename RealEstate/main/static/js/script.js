document.addEventListener("DOMContentLoaded", function () {
  const lightModeButton = document.getElementById("light-mode-toggle");
  const darkModeButton = document.getElementById("dark-mode-toggle");

  lightModeButton.addEventListener("click", function () {
    document.body.classList.remove("dark-mode");
    
  });

  darkModeButton.addEventListener("click", function () {
    document.body.classList.add("dark-mode");
  });
});
