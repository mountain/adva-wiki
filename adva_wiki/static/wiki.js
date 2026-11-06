document.addEventListener("DOMContentLoaded", () => {
  if (!window.katex) return;
  document.querySelectorAll(".math").forEach((element) => {
    katex.render(element.textContent, element, {
      displayMode: element.classList.contains("block"),
      throwOnError: false,
      trust: false,
      maxSize: 20,
      maxExpand: 1000,
    });
  });
});
