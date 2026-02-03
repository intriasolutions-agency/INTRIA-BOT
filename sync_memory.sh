#!/bin/bash

# Script de Sincronización Intria Bot
# Este script asegura que la memoria esté al día antes de empezar y guardada al terminar.

ACTION=$1

if [ "$ACTION" == "pull" ]; then
    echo "Sincronizando memoria desde GitHub..."
    git pull origin main
elif [ "$ACTION" == "push" ]; then
    echo "Guardando cambios en la memoria central..."
    git add memory/*.md MEMORY.md AGENTS.md TOOLS.md SOUL.md USER.md
    git commit -m "Auto-save: Sincronización de memoria entre instancias"
    git push origin main
else
    echo "Uso: ./sync_memory.sh [pull|push]"
fi
