// Resalta todas las secciones marcadas como importantes al cargar la página
document.addEventListener("DOMContentLoaded", function () {
    const highlights = document.querySelectorAll('.highlight-section');
    highlights.forEach(el => {
      el.style.boxShadow = '0 0 8px rgba(0, 87, 184, 0.2)';
    });
  });
  
  // Añadir botón para volver arriba
  const backToTop = document.createElement('button');
  backToTop.textContent = '↑ Subir';
  backToTop.style.position = 'fixed';
  backToTop.style.bottom = '30px';
  backToTop.style.right = '30px';
  backToTop.style.padding = '10px';
  backToTop.style.backgroundColor = '#0057b8';
  backToTop.style.color = 'white';
  backToTop.style.border = 'none';
  backToTop.style.borderRadius = '5px';
  backToTop.style.cursor = 'pointer';
  backToTop.style.display = 'none';
  
  backToTop.onclick = () => window.scrollTo({ top: 0, behavior: 'smooth' });
  
  document.body.appendChild(backToTop);
  
  window.addEventListener('scroll', () => {
    backToTop.style.display = window.scrollY > 300 ? 'block' : 'none';
  });
  