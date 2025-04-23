#!/usr/bin/env python3
"""
Script de refactorización ATLANTYDE:
- Estructura de directorios: /docs, /src, /assets, /manifests
- Clasificación de archivos según extensión
- Eliminación de duplicados (basado en hash MD5)
- Centralización de manifiestos en /manifests
"""
import os
import shutil
import pandas as pd

# Configuración de rutas
BASE_DIR = os.getcwd()
METADATA_CSV = os.path.join(BASE_DIR, 'file_metadata.csv')

# Directorios de destino
DIR_DOCS = os.path.join(BASE_DIR, 'docs')
DIR_SRC = os.path.join(BASE_DIR, 'src')
DIR_ASSETS = os.path.join(BASE_DIR, 'assets')
DIR_MANIFESTS = os.path.join(BASE_DIR, 'manifests')

# Extensiones por categoría
EXT_DOCS = {'.md', '.html', '.pdf', '.txt'}
EXT_CODE = {'.py', '.js', '.java', '.ts', '.go', '.rb', '.cs'}
EXT_ASSETS = {'.png', '.jpg', '.jpeg', '.svg', '.zip', '.rar', '.docx', '.xlsx', '.pptx'}

# Crear directorios si no existen
for d in [DIR_DOCS, DIR_SRC, DIR_ASSETS, DIR_MANIFESTS]:
    os.makedirs(d, exist_ok=True)

# Leer metadata generada
df = pd.read_csv(METADATA_CSV)

# Procesar cada archivo
processed_hashes = set()
for idx, row in df.iterrows():
    rel_path = row['path']
    file_hash = row['hash']
    ext = row['extension']

    src_path = os.path.join(BASE_DIR, rel_path)
    if not os.path.isfile(src_path):
        continue

    # Saltar duplicados ya movidos
    if pd.notna(file_hash) and file_hash in processed_hashes:
        os.remove(src_path)
        continue

    # Determinar carpeta destino
    if 'manifest' in os.path.basename(rel_path).lower():
        target_dir = DIR_MANIFESTS
    elif ext in EXT_DOCS:
        target_dir = DIR_DOCS
    elif ext in EXT_CODE:
        target_dir = DIR_SRC
    else:
        target_dir = DIR_ASSETS

    # Crear subruta destino manteniendo subcarpetas internas
    dest_path = os.path.join(target_dir, os.path.basename(rel_path))
    base, extension = os.path.splitext(dest_path)
    counter = 1
    while os.path.exists(dest_path):
        dest_path = f"{base}_{counter}{extension}"
        counter += 1

    # Mover archivo
    shutil.move(src_path, dest_path)

    # Registrar hash movido
    if pd.notna(file_hash):
        processed_hashes.add(file_hash)

print("Refactorización completada. Estructura: /docs, /src, /assets, /manifests.")