# Guía del Colaborador ATLANTYDE Labs

Bienvenido a ATLANTYDE Labs. Esta guía te ayudará a integrarte rápidamente y entender la arquitectura, herramientas y flujos de trabajo del proyecto.

---

## 1. Requisitos Previos

- Git ≥ 2.8
- Node.js ≥ 14 (para frontend)
- Python ≥ 3.10 (para scripts y CI)
- pip
- pre-commit (instalado global o en tu virtualenv)
- gh-cli (GitHub CLI) para despliegue y gestión de issues/pull requests

---

## 2. Clonación del Repositorio

```bash
gh auth login
gh repo clone <YourOrg>/atlantyde-labs.git
cd atlantyde-labs
``` 

---

## 3. Configuración Local

1. Instala dependencias Python y Node:
   ```bash
   python -m pip install --upgrade pip
   pip install pandas
   npm install
   ```
2. Instala y configura **pre-commit**:
   ```bash
   pip install pre-commit
   pre-commit install
   pre-commit install --hook-type commit-msg
   ```

---

## 4. Flujo de Branching & GitHub Actions

### 4.1 Estrategia de Branching

- **main**: rama protegida, siempre estable.
- **feature/**: desarrollo de nuevas funcionalidades.
- **hotfix/**: correcciones urgentes en producción.
- **release/**: preparación de versiones.

### 4.2 Workflows Automáticos

- **CHANGELOG** (`.github/workflows/changelog.yml`): genera y actualiza el `CHANGELOG.md` en cada push/PR.
- **Refactor ATLANTYDE** (`.github/workflows/refactor-atlantyde.yml`): ejecuta el script de refactorización y commit automático.

Para ejecutar manualmente:
```bash
gh workflow run generate-changelog.yml --repo <YourOrg>/atlantyde-labs
gh workflow run refactor-atlantyde.yml --repo <YourOrg>/atlantyde-labs
``` 

---

## 5. Estructura de Carpetas

```
.atlantyde-labs/
├─ .github/workflows/
├─ scripts/
│  └─ refactor.py
├─ src/components/
│  └─ tech-radar.jsx
├─ docs/
│  ├─ apis.md
│  └─ contact.md
├─ manifests/
│  ├─ overview.md
│  ├─ philosophy.md
│  └─ practice.md
├─ assets/
│  └─ media/
├─ .pre-commit-config.yaml
├─ mkdocs.yml
├─ CHANGELOG.md
├─ README.md
├─ SDLC_ATLANTYDE.md
└─ PRE-COMMIT_SETUP.md
```

---

## 6. Componentes Principales

### 6.1 TechRadar

- Archivo: `src/components/tech-radar.jsx`
- **Propiedades**:
  - `org`: nombre de la organización en GitHub.
  - `criteria`: array de objetos `{ label, query, color }` para métricas.

```jsx
<TechRadar
  org="ATLANTYDE-Labs"
  criteria={[
    { label: 'Stars', query: r => r.stargazers_count, color: '#8884d8' },
    { label: 'Forks', query: r => r.forks_count, color: '#82ca9d' }
  ]}
/>
```

### 6.2 Script de Refactorización

- Ubicación: `scripts/refactor.py`
- Ejecuta: organización de archivos, eliminación de duplicados, clasificación en `docs`, `src`, `assets`, `manifests`.

```bash
python scripts/refactor.py
```

---

## 7. Documentación y Navegación MkDocs

### 7.1 mkdocs.yml Unificado

```yaml
site_name: ATLANTYDE Labs
repo_url: https://github.com/YourOrg/atlantyde-labs
nav:
  - Home: index.md
  - Manifesto:
      - Introducción: manifests/overview.md
      - Filosofía: manifests/philosophy.md
      - Práctica: manifests/practice.md
  - Guías:
      - SDLC ATLANTYDE: SDLC_ATLANTYDE.md
      - Pre-commit: PRE-COMMIT_SETUP.md
      - APIs: docs/apis.md
      - Contacto: docs/contact.md
  - Autom. & DevOps:
      - Workflows CI: .github/workflows/README.md
      - Refactor Script: scripts/refactor.py
      - Tech Radar: src/components/tech-radar.jsx
  - Changelog: CHANGELOG.md
plugins:
  - search
  - mkdocs-git-revision-date-localized-plugin
theme:
  name: material
  palette:
    primary: 'indigo'
    accent: 'indigo'
```

### 7.2 Despliegue del Sitio

```bash
pip install mkdocs-material mkdocs-git-revision-date-localized-plugin
mkdocs build
mkdocs serve
# Para publicar en GitHub Pages:
mkdocs gh-deploy --clean
```

---

## 8. Buenas Prácticas

- Usa mensajes de commit claros y descriptivos.
- Ejecución de `pre-commit run --all-files` antes de push.
- Etiqueta releases semánticos (`vX.Y.Z`).
- Revisa el CHANGELOG.md tras cada integración.

---
