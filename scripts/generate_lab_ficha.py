# Path: scripts/generate_lab_ficha.py
# Autor: ATLANTYDE Founders Team
# Última modificación: 2025-04-23

import os
import sys
import json
from datetime import datetime

def generate_lab_ficha(lab_number, title, resumen, puntos, autor="ATLANTYDE Founders Team"):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"docs/fichas/LAB{lab_number:04d}_FICHA.md"

    # Construir la tabla Markdown
    tabla_puntos = "".join(f"| {t['tarea']} | {t['puntos']} |\n" for t in puntos)

    content = f"""<!--
Path: {filename}
Autor: {autor}
Última modificación: {today}
-->

# 🧾 Ficha Resumen – LAB {lab_number:04d}: {title}

## 🎯 Objetivo
{resumen}

## 🧪 Evaluación
| Tarea                                    | Puntos |
|------------------------------------------|--------|
{tabla_puntos}
## 🧠 Créditos
- Generado automáticamente por el sistema de trazabilidad ATLANTYDE.
- Autor: {autor}
- Fecha: {today}
"""

    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] Ficha generada: {filename}")

# CLI: `python generate_lab_ficha.py 2`
if __name__ == "__main__":
    # Uso rápido con valores por defecto
    lab_number = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    title = "Colaboración y Versionado con GitHub"
    resumen = "Aprender a colaborar en ramas, hacer commits firmados y abrir Pull Requests con lógica ATLANTYDE."
    puntos = [
        {"tarea": "Clonar repositorio y crear branch", "puntos": "10"},
        {"tarea": "Hacer commit firmado", "puntos": "15"},
        {"tarea": "Abrir PR con plantilla", "puntos": "10"},
        {"tarea": "Respetar estructura de carpetas", "puntos": "5"},
    ]
    generate_lab_ficha(lab_number, title, resumen, puntos)
