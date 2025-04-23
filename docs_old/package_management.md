
# Gestión de Versionado y Dependencias en ATLANTYDE Foundation

Este documento establece la base técnica y estratégica para el control de versiones y dependencias de los entornos fundamentales del proyecto **ATLANTYDE Foundation**, repositorio fundacional, institucional, neuroeducativo y divulgativo de la organización.

---

## 1. package.json (Node.js / React)

```json
{
  "name": "atlantyde-foundation",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "lint": "eslint --ext .js,.jsx src/"
  },
  "dependencies": {
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "recharts": "^2.6.0"
  },
  "devDependencies": {
    "eslint": "^8.0.0",
    "react-scripts": "^5.0.0"
  },
  "engines": {
    "node": ">=14.0.0"
  }
}
```

## 2. requirements.txt (Python)

```text
django==4.2.0
pandas==2.0.3
mkdocs==1.5.2
mkdocs-material==9.1.1
mkdocs-git-revision-date-localized-plugin==0.15.0
typing_extensions>=4.5.0
```

## 3. docs/requirements.txt (MkDocs)

```text
mkdocs==1.5.2
mkdocs-material==9.1.1
mkdocs-git-revision-date-localized-plugin==0.15.0
```

## 4. Lockfiles y Control

- Node: `package-lock.json`
- Python: opcional `requirements.lock` con `pip-compile`
- MkDocs: usa `docs/requirements.txt`

## 5. Workflows CI

```yaml
- name: Instalar dependencias Node
  run: npm ci

- name: Instalar dependencias Python
  run: pip install --upgrade pip && pip install -r requirements.txt

- name: Instalar dependencias MkDocs
  run: pip install -r docs/requirements.txt
```

Con estas prácticas se garantiza:
- Versionado semántico desde el inicio.
- Flujo CI reproducible y auditable.
- Estandarización bajo ATLANTYDE Foundation.
