# Path: scripts/generate_lab_ficha.py
# Autor: ATLANTYDE Founders Team
# Última modificación: 2025-04-23

import os
from datetime import datetime

def generate_lab_ficha(lab_number, title, resumen, puntos, autor="ATLANTYDE Founders Team"):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"docs/fichas/LAB{lab_number:04d}_FICHA.md"
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
{''.join(f"| {t['tarea']} | {t['puntos']} |\n" for t in puntos)}

## 🧠 Créditos
- Generado automáticamente por el sistema de trazabilidad ATLANTYDE.
- Autor: {autor}
- Fecha: {today}

"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] Ficha generada: {filename}")

# Ejemplo de uso
if __name__ == "__main__":
    lab_number = 2
    title = "Colaboración y Versionado con GitHub"
    resumen = "Aprender a colaborar en ramas, hacer commits firmados y abrir Pull Requests con lógica ATLANTYDE."
    puntos = [
        {"tarea": "Clonar repositorio y crear branch", "puntos": "10"},
        {"tarea": "Hacer commit firmado", "puntos": "15"},
        {"tarea": "Abrir PR con plantilla", "puntos": "10"},
        {"tarea": "Respetar estructura de carpetas", "puntos": "5"},
    ]
    generate_lab_ficha(lab_number, title, resumen, puntos)
