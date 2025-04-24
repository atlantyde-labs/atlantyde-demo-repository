# 🚀 Guía de Despliegue del Micrositio ATLANTYDE

Este repositorio contiene la documentación viva y técnica del ecosistema educativo ATLANTYDE, lista para publicarse como sitio web accesible mediante las siguientes opciones:

---

## 🧪 Opción 1: mkdocs serve (modo local para pruebas)

### Requisitos:
- Python 3.7+
- `pip install mkdocs mkdocs-material`

### Comando:

```bash
mkdocs serve
```

Esto lanzará el sitio en `http://127.0.0.1:8000/`

---

## 🌐 Opción 2: Publicar en GitHub Pages (automático)

### Requisitos:
- GitHub Actions habilitado
- Un repositorio público o privado con GitHub Pages activado

### Comando:

```bash
mkdocs gh-deploy
```

> Asegúrate de que tu repo tiene configurado Pages desde `gh-pages` branch.

---

## ⚙️ Opción 3: Publicar en Netlify

### Pasos:
1. Crea cuenta en https://netlify.com
2. Enlaza tu repo GitHub con botón "New site from Git"
3. Configura:
   - Build command: `mkdocs build`
   - Publish directory: `site/`

---

## ⚡ Opción 4: Publicar en Vercel

Vercel no soporta directamente mkdocs pero puedes hacer:

### Alternativa:
1. Usar `mkdocs build` para generar carpeta `site/`
2. Crear `vercel.json`:

```json
{
  "public": true,
  "rewrites": [{ "source": "/(.*)", "destination": "/index.html" }]
}
```

3. Usa el CLI de Vercel o sube vía interfaz gráfica
4. Define `output directory: site/`

---

## 🧾 Estructura de Documentación

- `index.md` – Página inicial
- `mkdocs_atlantyde_complete.yml` – Navegación y estructura
- `rfc-template-atlantyde.md` – Plantilla oficial de propuestas
- Archivos `*.docx`, `*.pdf`, `*.zip` enlazados desde Markdown

---

## 🧩 Licencia

Este sitio está publicado bajo [Creative Commons Atribución 4.0 Internacional](https://creativecommons.org/licenses/by/4.0/)

---

**Creado por:** Jaime Silva Kbza  
**Asistido por:** CLO 🤝

