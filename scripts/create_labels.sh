#!/bin/bash
# Path: scripts/create_labels.sh
# Autor: ATLANTYDE Founders Team
# Última modificación: 2025-04-23

echo "🔍 Verificando y creando etiquetas necesarias..."

# Definición de etiquetas requeridas
declare -A labels
labels["fundador"]="#0066cc"
labels["visual"]="#a643c6"
labels["backlog"]="#999999"
labels["activación"]="#f39c12"
labels["stakeholder"]="#16a085"
labels["educacion"]="#2980b9"

# Crear cada etiqueta si no existe
for label in "${!labels[@]}"; do
  if ! gh label list | grep -wq "$label"; then
    echo "➕ Creando etiqueta: $label"
    gh label create "$label" --color "${labels[$label]}" --description "Etiqueta generada automáticamente para contribuciones fundacionales"
  else
    echo "✅ Etiqueta ya existe: $label"
  fi
done
