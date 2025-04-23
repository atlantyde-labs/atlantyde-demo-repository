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

El repositorio se estructura en base al SDLC automatizado con CI/CD y filosofía Markdown First, utilizando MkDocs + Material para su despliegue.

---

## 🗺️ Navegación del sitio (MkDocs)

La siguiente tabla representa la estructura activa del sitio `ATLANTYDE Foundation Docs`:

---

## 🧩 Repositorio MonoRepo

Este repositorio centraliza:

- Documentación viva (MkDocs + Material)
- Scripts Python de automatización
- Componentes React (Tech Radar, Dashboard)
- Workflows CI/CD completos
- Configuración Dependabot y CodeQL

---

## 📁 Estructura del Repositorio

```
├── .github/
│   ├── workflows/
│   │   ├── changelog.yml
│   │   ├── codeql.yml
│   │   └── refactor-atlantyde.yml
│   └── dependabot.yml
├── src/
│   └── components/
│       └── tech-radar.jsx
├── scripts/
│   └── refactor.py
├── docs/
│   ├── apis.md
│   ├── contact.md
│   ├── requirements.txt
│   └── package_management.md
├── manifests/
│   ├── overview.md
│   ├── philosophy.md
│   └── practice.md
├── assets/
│   └── media/
├── CHANGELOG.md
├── mkdocs.yml
├── README.md (este archivo)
├── Guia_Colaborador.md
├── SDLC_ATLANTYDE.md
├── PRE-COMMIT_SETUP.md
├── package.json
├── requirements.txt
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

- 📧 Correo corporativo root: [innovation@atlantyde.eu](mailto\:innovation@atlantyde.eu)

---

## 🤝 Contribución Abierta

Este repositorio sigue un enfoque **Markdown First + GitHub Flow**. Toda contribución debe:

- Usar ramas descriptivas (`feature/`, `bugfix/`, `doc/`)
- Incluir etiquetas automáticas mediante archivos JSON (labels)
- Estar documentada en `CHANGELOG.md` vía GitHub Actions
- Cumplir flujos de integración continua preconfigurados (CI/CD)
- Aportar desde código, documentación, diseño, emocionalidad o narrativa

Ver [Guía del Colaborador](docs/Guia_Colaborador.md) y fichas de fundadores en `docs/fichas/`.

---

## 📜 Manifiestos del Proyecto

- [Manifiesto Filosófico ATLANTYDE](manifests/philosophy.md)
- [Prácticas Institucionales y Éticas](manifests/practice.md)

> Nos regimos por valores de apertura, sostenibilidad, soberanía tecnológica y colaboración radical. Todo cambio significativo debe estar alineado con estos principios y reflejado en los workflows del SDLC.

---

## 🔐 Seguridad y Cumplimiento

El proyecto garantiza:

- 🔐&#x20;
- 🛡️ Dependabot para `npm`, `pip`, `docker`
- 📦 Workflows SAST/DAST con validación semántica y vulnerabilidades
- 🇪🇺 Cumplimiento con:
  - GDPR
  - ISO 27001
  - eIDAS
  - MIT extendida para soberanía digital

---

## 🧪 Automatización CI/CD

- `auto-changelog`
- `release-drafter`
- `git-auto-commit`
- `pre-commit`
- `refactor.py`

---

## 🧭 Cómo empezar

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

Publicado bajo licencia MIT con cláusulas de soberanía digital y cumplimiento europeo.

