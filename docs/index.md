# 🧠 ATLANTYDE Foundation

**Repositorio fundacional, institucional, neuroeducativo y divulgativo** de la iniciativa ATLANTYDE, liderada por un colectivo visionario de fundadores que fusionan tecnología, ética, sostenibilidad y colaboración radical.

---

## 🚀 Misión

Construir una **plataforma colaborativa** y de código abierto que impulse la innovación digital, el talento descentralizado y el cumplimiento normativo europeo, todo bajo una visión humanista y atlante.

---

## 🧬 Filosofía del Proyecto

- **Open Source by Design**: desde el inicio.
- **Compliance First**: cumplimiento automático (GDPR, ISO 27001, eIDAS).
- **Neuroeducación & LMS-ready**: preparado para aprendizaje interactivo.
- **DevSecOps completo**: SDLC automatizado con GitHub Actions.

ATLANTYDE nace bajo una ética radicalmente abierta y humanista. Promovemos:

- La colaboración descentralizada como pilar de innovación
- El cumplimiento como práctica viva
- La documentación como narrativa común
- El código como herramienta civilizatoria

---

## 📘 Documentación Viva

Este entorno sigue una estructura `Markdown First`, desplegada con **MkDocs + Material Theme**. Toda la documentación técnica, estratégica, institucional y educativa se encuentra bajo la carpeta `/docs/` y es navegable mediante la estructura lateral del sitio.

---

## 📁 Estructura del Repositorio

```
├── .github/
│   ├── workflows/
│   │   ├── changelog.yml
│   │   ├── codeql.yml
│   │   └── deploy-pages.yml
│   └── dependabot.yml
├── assets/
│   ├── css/
│   ├── images/
│   ├── js/
│   └── branding/
├── docs/
│   ├── index.md
│   ├── contacto.md
│   ├── apis.md
│   ├── package_management.md
│   ├── guías/
│   │   ├── Guia_Branding_Atlantyde.md
│   │   ├── Guia_Visual_Founders.md
│   │   └── Guia_Colaborador.md
│   ├── fichas/
│   │   ├── LOKY_FICHA.md
│   │   └── CULEBRA_FICHA.md
│   ├── compliance/
│   │   ├── panel_badges.md
│   │   └── onepager-servicios.md
│   ├── dev/
│   │   ├── markdown-first.md
│   │   ├── github-actions.md
│   │   └── deploy_github_pages.md
│   ├── labs/
│   │   ├── lab_010.md
│   │   ├── lab_011.md
│   │   └── LAB0001_ONBOARDING.md
│   ├── legal/
│   │   └── licencia.md
│   ├── memoria/
│   │   └── Memoria_Estrategica_ATLANTYDE.md
│   ├── governance/
│   │   └── founders_manifesto.md
│   ├── onboarding/
│   │   ├── loky_creativo.md
│   │   ├── angel_beta.md
│   │   └── onboarding_completo.md
│   ├── creativo/
│   │   ├── avatares.md
│   │   └── estilo.md
│   └── about/
│       └── contacto.md
├── scripts/
│   └── refactor.py
├── src/
│   └── components/
│       └── tech-radar.jsx
├── SDLC_ATLANTYDE.md
├── README.md
├── mkdocs.yml
├── requirements.txt
├── package.json
└── .pre-commit-config.yaml
```

---

## 🧠 Fundadores

| Alias Épico | Nombre Formal                                | Rol Estratégico                    |
| ----------- | -------------------------------------------- | ---------------------------------- |
| **Kabehz**  | **Jaime Silva**                              | CEO, CIO, Creador del Manifiesto   |
| **Culebra** | **Ángel Cumbreño**                           | Facilitador Emocional y Finanzas   |
| **MrLoky**  | **José Antonio López**                       | Director Creativo y Full Stack Dev |
| *(Futuros)* | **Iñigo Gortazar** / **Alba RS (Supernova)** | Legal Tech y Cultura Narrativa     |

---

## 📢 Contacto

- 📧 innovation@atlantyde.eu

---

## 🤝 Contribución Abierta

Este repositorio sigue un enfoque **Markdown First + GitHub Flow**. Toda contribución debe:

- Usar ramas descriptivas (`feature/`, `bugfix/`, `doc/`)
- Incluir etiquetas automáticas mediante archivos JSON (labels)
- Estar documentada en `CHANGELOG.md` vía GitHub Actions
- Cumplir flujos de integración continua preconfigurados (CI/CD)
- Aportar desde código, documentación, diseño, emocionalidad o narrativa

Ver la [Guía del Colaborador](guias/Guia_Colaborador.md) y fichas de fundadores en `docs/fichas/`.

---

## 📜 Manifiestos del Proyecto

- [Manifiesto Filosófico ATLANTYDE](../manifests/philosophy.md)
- [Prácticas Institucionales y Éticas](../manifests/practice.md)

> Nos regimos por valores de apertura, sostenibilidad, soberanía tecnológica y colaboración radical. Todo cambio significativo debe estar alineado con estos principios y reflejado en los workflows del SDLC.

---

## 🔐 Seguridad y Cumplimiento

El proyecto garantiza:

- 🔐 CodeQL activado
- 🛡️ Dependabot para `npm`, `pip`, `docker`
- 📆 Workflows SAST/DAST
- 🇪🇺 Compliance: GDPR, ISO 27001, eIDAS
- 🗒️ Licencia MIT extendida para soberanía digital

---

## 🧪 Automatización CI/CD

- `auto-changelog`
- `release-drafter`
- `git-auto-commit`
- `pre-commit`
- `refactor.py`

---

## 🧽 ¿Cómo empezar?

```bash
git clone https://github.com/atlantyde-labs/atlantyde-foundation.git
cd atlantyde-foundation
npm install
pip install -r requirements.txt
pre-commit install
mkdocs serve
```

---

## 🌊 Licencia

Publicado bajo licencia **MIT** con cláusulas extendidas de cumplimiento europeo y soberanía digital.
