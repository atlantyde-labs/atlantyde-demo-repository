# Pre-commit óptimo para desarrollo en ramas y local

A continuación encontrarás la configuración recomendada de hooks para mantener calidad de código, formato y cumplimiento de estándares en tu flujo de trabajo local y en branches.

---

## 1. Configuración (.pre-commit-config.yaml)
```yaml
# Copia este bloque en .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace        # Elimina espacios en blanco finales
      - id: end-of-file-fixer         # Asegura fin de archivo con línea vacía
      - id: check-yaml                # Valida sintaxis YAML
      - id: check-json                # Valida sintaxis JSON
      - id: check-added-large-files   # Previene commits de archivos muy grandes

  - repo: https://github.com/psf/black
    rev: 23.3.0
    hooks:
      - id: black                     # Formatea Python (PEP8)
        language_version: python3.10

  - repo: https://github.com/PyCQA/isort
    rev: 5.12.0
    hooks:
      - id: isort                     # Ordena imports en Python

  - repo: https://github.com/PyCQA/flake8
    rev: 6.0.0
    hooks:
      - id: flake8                    # Linter Python
        additional_dependencies: [flake8-bugbear]

  - repo: https://github.com/adrienverge/yamllint
    rev: v1.28.0
    hooks:
      - id: yamllint                  # Linter YAML

  - repo: https://github.com/markdownlint/markdownlint
    rev: v0.24.0
    hooks:
      - id: markdownlint              # Linter Markdown

  - repo: https://github.com/koalaman/shellcheck
    rev: v0.9.0
    hooks:
      - id: shellcheck                # Linter Shell (.sh)
        files: \\.(sh|bash)$
```

---
    
## 2. Guía de Instalación y Uso

### Requisitos
- Git ≥ 2.8  
- Python ≥ 3.8  
- pip  
- (Opcional) Node.js ≥ 14 si se añaden hooks basados en JS

### Instalación en local
1. Instala `pre-commit` globalmente (o en tu venv):
   ```bash
   pip install --upgrade pre-commit
   ```
2. Copia el archivo de configuración al root del repo:
   ```bash
   cp PRE-COMMIT_SETUP.md .pre-commit-config.yaml
   ```
3. Registra los hooks:
   ```bash
   pre-commit install
   ```
4. (Opcional) Registra hooks de `commit-msg`:
   ```bash
   pre-commit install --hook-type commit-msg
   ```

### Uso diario
- Al ejecutar `git commit`, los hooks se activan automáticamente.
- Para chequear todo de golpe:
  ```bash
  pre-commit run --all-files
  ```
- Para omitir hooks (solo en casos excepcionales):
  ```bash
  git commit --no-verify
  ```

### Integración en CI (GitHub Actions)
Añade este paso previo en tu workflow:
```yaml
- name: Run pre-commit hooks
  uses: actions/checkout@v3

- name: Setup Python
  uses: actions/setup-python@v4
  with:
    python-version: '3.10'

- name: Install pre-commit
  run: pip install pre-commit

- name: Ejecutar pre-commit
  run: pre-commit run --all-files
```

---
