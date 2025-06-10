function showTab(id) {
  document.querySelectorAll(".tab-content").forEach(section => {
    section.classList.remove("active");
  });
  document.getElementById(id).classList.add("active");
}
